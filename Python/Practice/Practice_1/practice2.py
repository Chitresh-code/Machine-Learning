# Use external modules in python
# pip install pyttsx3

import pyttsx3
engine = pyttsx3.init()
engine.say("Hello, World!")
engine.runAndWait()