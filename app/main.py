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

kivy.require('1.10.1')


class RootWidget(FloatLayout):
    # Class variables
    dropdown = DropDown()
    button = Button(text="Enter",
                    size_hint=(1, .2),
                    pos_hint={'center_x': 0.5, 'center_y': 0.07})

    # Add buttons to dropdown menu
    for index in range(3):
        dropdown_button = Button(text='Button %r' % index,
                                 size_hint_y=None,
                                 height=44)

        dropdown.add_widget(dropdown_button)

    button.bind(on_release=dropdown.open)
    dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))

    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)

        self.add_widget(self.button, index=0)
        self.add_widget(Image(source='Phrijj.png', size_hint=(1, 1),
                        pos_hint={'center_x': 0.5, 'center_y': 0.6}),
                        index=1)


class PhrijjApp(App):
    def build(self):

        return RootWidget()

if __name__ == '__main__':
    PhrijjApp().run()
