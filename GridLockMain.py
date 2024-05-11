#external Libraries
import platform
from datetime import datetime as dt
import PySimpleGUI as sim

#internal Libraries
import UniqueKeyValidator
import UserInterfaceKernal
from UniqueKeyValidator import *
from UserInterfaceKernal import *

#This is the Main file, it will serve as a bootstrap to load the UserInterface
global tempkey, verified, validated
tempkey = ""
verified = False
Quit = False
validated = 0

#Gridlock Startup Sequence-----------------------
#note, the below py files being called were made by Team Gridlock (Jonthan McGlothin and Co)
valid = UniqueKeyValidator.Run_Validator()#run validator through referential function

if valid == 1:
   print("ready to continue to user interface, ", str(validated))#run user interface main app
   LaunchInterface()

#if so, continue to user interface
#(launch user interface here)
