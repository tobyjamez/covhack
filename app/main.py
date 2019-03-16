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
import kivy.app as a
kivy.require('1.10.1')


# Subclass app below
# class MainLoop(a.App):
