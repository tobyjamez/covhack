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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
import numpy as np
kivy.require('1.10.1')

class InitialScreen(GridLayout):

    def __init__(self, **kwargs):
        super(InitialScreen, self).__init__(**kwargs)
        self.rows = 2
        self.add_widget(Image(source='Phrijj.png'))
        self.add_widget(Button(text='Enter'))





class PhrijjApp(App):
    def build(self):
        return InitialScreen()

if __name__ == '__main__':
    PhrijjApp().run()


# Subclass app below
# class MainLoop(a.App):
