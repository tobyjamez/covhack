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

from comm import search, add, show

kivy.require('1.10.1')


class RootWidget(FloatLayout):
    # Class variables

    def send_search(term, response_list, widget) -> type(None):

        response_dict = search(term)

        response_list.append(response_dict)

        self.dropdown.dismiss()
    
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        # Add widgets----------------------------------------------------------

        # Add image ----------------------------------------------------
        self.add_widget(Image(source='Phrijj.png', size_hint=(1, 1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.6}),
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
        search_button = Button(text="Search",
                               size_hint_y=None,
                               height=44)

        self.search_response_list = []

        search_button.bind(on_click=lambda widget:
                           self.send_search(self.textinput.text,
                                            self.search_response_list,
                                            widget))

        self.dropdown.add_widget(search_button)

        show_button = Button(text="Show",
                             size_hint_y=None,
                             height=44)

        self.dropdown.add_widget(show_button)

        # --------------------------------------------------------------

        # Add enter button ---------------------------------------------
        self.enter_button = Button(text="Start!",
                                   size_hint=(1, .2),
                                   pos_hint={'center_x': 0.5,
                                             'center_y': 0.07})

        self.enter_button.bind(on_release=self.dropdown.open)
        self.add_widget(self.enter_button, index=0)
        # --------------------------------------------------------------
        # ---------------------------------------------------------------------


class PhrijjApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PhrijjApp().run()
