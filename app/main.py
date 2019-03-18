"""
Main app loop for a kivy based application.

@author="Toby James, Krishan Jethwa,
Enrico Zammit Lonardelli, Davit Endeladze"
"""

import sys
import os

# Allow environment variables to be passed as command line arguments
# In the form ENV_VARIABLE=value

for env_variable in sys.argv[1:]:
    try:
        os.environ[env_variable.split("=")[0]] = env_variable.split("=")[1]
    except(IndexError) as e:  # Passed value has no equals
        pass

import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle

from comm import search, add, show
from productview import ProductView

kivy.require('1.10.1')


class RootWidget(ScreenManager):

    def return_home(self, *args):
        self.current = "1"

    def switch_screen(self, button, *args):
        response_list = show().json()['data']

        self.list_dropdown = DropDown(size_hint=(1, 1))

        for item in response_list:
            self.list_dropdown.add_widget(ProductView(dict(name=item[0],
                                                           price=item[1],
                                                           provider=item[2]),
                                                      size_hint_y=None,
                                                      height=144,
                                                      pos_hint={'center_x':
                                                                0.5},
                                                      color=(0, 0, 0, 1),
                                                      background_color=(255,
                                                                        255,
                                                                        255,
                                                                        255)))

        buy_button = Button(text="Home",
                            size_hint_y=None,
                            height=144,
                            pos_hint={'center_x': 0.5},
                            color=(0, 0, 0, 1),
                            background_color=(255, 255, 255, 255))

        buy_button.bind(on_press=self.return_home)

        self.list_dropdown.add_widget(buy_button)
        self.current = "list"
        try:
            self.list_screen.add_widget(self.list_dropdown)
        except Exception:
            pass
        self.dropdown.dismiss()

    def send_search(self, term, response_list, button, *args) -> type(None):

        new_screen = "search"

        response_dict = search(term)['data']

        if response_dict is None:
            return None

        else:
            response_list.append(response_dict)
            for item in response_list:
                item_view = ProductView(item,
                                        color=(0, 0, 0, 1),
                                        background_color=(255, 255, 255, 255))
                self.search_screen.add_widget(item_view)
                response_list.pop(response_list.index(item))

            self.current = new_screen
            self.dropdown.dismiss()
        self.search_screen.add_widget(button)

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super().__init__(**kwargs)

        self.home_button1 = Button(text="Home",
                                   pos_hint={'center_x': 0.5,
                                             'center_y': 0.95},
                                   size_hint_y=None,
                                   height=144)

        self.home_button2 = Button(text="Home",
                                   pos_hint={'center_x': 0.5,
                                             'center_y': 0.95},
                                   size_hint_y=None,
                                   height=144)

        self.home_button1.bind(on_press=self.return_home)
        self.home_button2.bind(on_press=self.return_home)

        self.screen1 = Screen(name="1")

        self.search_screen = Screen(name="search")
        self.list_screen = Screen(name="list")

        # Add widgets----------------------------------------------------------
        with self.screen1.canvas.before:
            Color(0, 0, 0, 1)
            self.screen1.rect = Rectangle(size=self.screen1.size,
                                          pos=self.screen1.pos)

        def update_rect(instance, value):
            instance.rect.pos = instance.pos
            instance.rect.size = instance.size

        # listen to size and position changes
        self.screen1.bind(pos=update_rect, size=update_rect)

        # Add image ----------------------------------------------------
        self.screen1.add_widget(Image(source='Phrijj.png', size_hint=(1, 1),
                                      pos_hint={'center_x': 0.5,
                                                'center_y': 0.6}),
                                index=1)
        # --------------------------------------------------------------

        # Add textinput ------------------------------------------------
        self.textinput = TextInput(hint_text="Search for ingredients",
                                   multiline=False,
                                   size_hint_y=None,
                                   height=144,
                                   pos_hint={'center_x': 0.5,
                                             'center_y': 0.95},
                                   opacity=1)

        # Add dropdown menu --------------------------------------------
        self.dropdown = DropDown()
        self.dropdown.add_widget(self.textinput)

        # Add buttons to dropdown menu
        search_button = Button(color=(0, 0, 0, 1),
                               background_color=(255, 255, 255, 255),
                               text="Search",
                               size_hint_y=None,
                               height=144)

        self.search_response_list = []

        search_button.bind(on_press=lambda widget:
                           self.send_search(self.textinput.text,
                                            self.search_response_list,
                                            self.home_button1))

        self.dropdown.add_widget(search_button)

        show_button = Button(color=(0, 0, 0, 1),
                             background_color=(255, 255, 255, 255),
                             text="Show",
                             size_hint_y=None,
                             height=144)

        show_button.bind(on_press=lambda x:
                         self.switch_screen(self.home_button2))

        self.dropdown.add_widget(show_button)

        # --------------------------------------------------------------

        # Add enter button ---------------------------------------------
        self.enter_button = Button(color=(0, 0, 0, 1),
                                   background_color=(255, 255, 255, 255),
                                   text="Start!",
                                   size_hint=(1, .2),
                                   pos_hint={'center_x': 0.5,
                                             'center_y': 0.07})

        self.enter_button.bind(on_release=self.dropdown.open)
        self.screen1.add_widget(self.enter_button, index=0)

        self.add_widget(self.screen1)
        self.add_widget(self.list_screen)
        self.add_widget(self.search_screen)
        # --------------------------------------------------------------
        # ---------------------------------------------------------------------


class PhrijjApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PhrijjApp().run()
