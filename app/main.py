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

from comm import search, add, show
from productview import ProductView

kivy.require('1.10.1')


class RootWidget(ScreenManager):

    def switch_screen(self):
        self.current = "list"
        self.dropdown.dismiss()

    def send_search(self, term, response_list) -> type(None):

        new_screen = "search"

        response_dict = search(term)['data']

        if response_dict is None:
            return None


        else:
            response_list.append(response_dict)
            for item in response_list:
                item_view = ProductView(item)
                self.search_screen.add_widget(item_view)

            self.current = new_screen
            self.dropdown.dismiss()

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super().__init__(**kwargs)

        self.screen1 = Screen(name="1")

        self.search_screen = Screen(name="search")
        self.list_screen = Screen(name="list")

        # Add widgets----------------------------------------------------------

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
                                   height=44,
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
                              height=44)

        self.search_response_list = []

        search_button.bind(on_press=lambda widget:
                           self.send_search(self.textinput.text,
                                            self.search_response_list))

        self.dropdown.add_widget(search_button)

        show_button = Button(color=(0, 0, 0, 1), 
                             background_color=(255, 255, 255, 255),
                             text="Show",
                             size_hint_y=None,
                             height=44)

        show_button.bind(on_press=lambda widget: self.switch_screen())

        self.dropdown.add_widget(show_button)

        # --------------------------------------------------------------

        # Add enter button ---------------------------------------------
        self.enter_button = Button(color=(0, 0, 0, 1), 
                                   background_color=(255, 255, 255, 255),
                                   text="Start!",
                                   size_hint=(1, .2),
                                   pos_hint={'center_x': 0.5,
                                             'center_y': 0.07},
                                   
                                    )

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
