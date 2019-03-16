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
from kivy.uix.label import Label
from kivy.uix.image import Image
import numpy as np
kivy.require('1.10.1')
class RootWidget(FloatLayout):
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        super(RootWidget, self).__init__(**kwargs)
        self.add_widget(Image(source='Phrijj.png', size_hint=(1, 1),
                pos_hint={'center_x': 0.5, 'center_y': 0.6}),index=0)
        # let's add a Widget to this layout
        self.add_widget(
            Button(
                text="Enter",
                size_hint=(1, .2),
                pos_hint={'center_x': 0.5, 'center_y': 0.07}),index = 1)
        


class PhrijjApp(App):
    def build(self):

        return RootWidget()

if __name__ == '__main__':
    PhrijjApp().run()


# Subclass app below
# class MainLoop(a.App):
