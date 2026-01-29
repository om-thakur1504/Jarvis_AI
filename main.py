import eel
# import os
from engine.features import *
from engine.command import *
def start() :
    eel.init("www")
    playAssistantSound()
    eel.start("index.html", size=(1000, 1000))