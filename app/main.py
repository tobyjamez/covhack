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


class CustomTextInput(TextInput):
    def toggle_opacity(self) -> type(None):
        self.opacity = 1 - self.opacity


class RootWidget(FloatLayout):
    # Class variables

    @staticmethod
    def button_trip(textinput, dropdown, widget):
        dropdown.open(widget)
        textinput.toggle_opacity()

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
        textinput = CustomTextInput(hint_text="Search for a meal",
                                    multiline=False,
                                    size_hint_y=None,
                                    height=44,
                                    pos_hint={'center_x': 0.5,
                                              'center_y': 0.95},
                                    opacity=0)

        self.add_widget(textinput)

        # Add dropdown menu --------------------------------------------
        dropdown = DropDown()

        # Add buttons to dropdown menu
        search_button = Button(text="Search",
                               size_hint_y=None,
                               height=44)

        dropdown.add_widget(search_button)

        show_button = Button(text="Show",
                             size_hint_y=None,
                             height=44)

        dropdown.add_widget(show_button)

        dropdown.bind(on_release=lambda x: textinput.toggle_opacity())
        # --------------------------------------------------------------

        # Add enter button ---------------------------------------------
        enter_button = Button(text="Enter",
                              size_hint=(1, .2),
                              pos_hint={'center_x': 0.5, 'center_y': 0.07})

        enter_button.bind(on_release=lambda widget: self.button_trip(textinput,
                                                                     dropdown,
                                                                     widget))

        self.add_widget(enter_button, index=0)
        # --------------------------------------------------------------


class PhrijjApp(App):
    def build(self):
        return RootWidget()

if __name__ == '__main__':
    PhrijjApp().run()
