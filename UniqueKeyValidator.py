import platform
from datetime import datetime as dt
import PySimpleGUI as sim
import os
global verified
verified = False
global tempkey
tempkey = ""
global opt_out
opt_out = 0   #checks to see if menu is closed early



def GL_Authenticate_UniqueKey():
    authentic = False
    stable = True
    ThisPC = True
    global Reason

    global tempkey
    file = open("UniqueKeyStorage.txt", "r")   #first we check the instant value
    value1 = file.readline()
    file.close()
    # check 100 total times to make sure this is not an ever-changing key.
    for i in range(99):
        file = open("UniqueKeyStorage.txt", "r")
        value2 = file.readline()
        file.close()
        if value2 != value1:
            stable = False
            Reason = "This Key Is not Static, it Continues to Change"
    #If the key is stable, meaning it does not change, we can now check to see if your computer name matches the name
    #stub within the key. (if not, this key belongs to someone else)
    if stable == True:  #If
        PCName = platform.node()
        if PCName[0:4] != value1[0:4]:
            ThisPC = False
            Reason = "This Key Belongs to someone else"
    if stable and ThisPC:
        authentic = True      #If the key is stable (unchanging) and this pc's name is appropriate, the key is valid
    return authentic

def GL_Check_for_Key(): #check to see if there is a key
    key_detected = False
    file = open("UniqueKeyStorage.txt", "r")
    value = file.readline()
    file.close()
    if value != "" and value != " " and value != EOFError:
        key_detected = True
        global tempkey
        tempkey = str(value)
    return key_detected

def GL_Save_Key(): #how to save a key
    file = open("UniqueKeyStorage.txt", "w")
    file.write(tempkey)
    file.close()
#define Unique User Key function
def GL_Gen_UniqueKey():
    unique_key = ""
    tempPCName = platform.node()    #gather the user's device name
    temptime = dt.now()
    print("creating key:\n", "Device name: ", tempPCName, "TimeStamp: ", temptime)
    if len(tempPCName) >= 4:
        unique_key += tempPCName[0:4]   #if possible, add the 1st 4 letters of the machine name to the unique key
    elif len(tempPCName) < 4:
        unique_key += tempPCName[0:(len(tempPCName)-1)]
    unique_key += str(temptime)[1:4] #add the last 3 digits of the year
    unique_key += "-"
    # add all 4 digits of the date as one block without the hyphen
    unique_key += str(temptime)[5:7]
    unique_key += str(temptime)[8:10]
    # add all 4 digits of the time in minutes without the colon
    unique_key += str(temptime)[14:16]
    unique_key += "-"
    #add the time in seconds
    unique_key += str(temptime)[17:19]
    print("\nKey Successfully Created: ", unique_key)
    return unique_key

def Run_Validator():
    Reason = ""
    global verified
    verified = False
    global tempkey
    tempkey = ""
    global opt_out
    opt_out = 0
    global validated
    validated = 0
    #Create userinterface
    Unique_Menu_width = X = 400    #change width and height of default window
    Unique_Menu_Height = Y = 350
    sim.theme('LightGrey6')
    Unique_Menu_Layout = [
            [sim.Text('  GridLock is working to Validate your Unique User Key   ')],
            [sim.Text(' \n \n\n\n')], #top margin
            #[sim.Input(key='-IN1-')], #key for mirroring
            [sim.Text(' '),sim.Button('Quit')]
                   ] #end of default window
    #__________________
    #----launch window
    Unique_Binary_Layout = [
            [sim.Text('No Unique User Key Was found,\nwould you like to create one?')],
            [sim.Text(' \n \n')],  # top margin
            # [sim.Input(key='-IN1-')], #key for mirroring
            [sim.Button('Yes'), sim.Button('No')]]



    prewindow = sim.Window('Gridlock Validing Key...', Unique_Menu_Layout, size = (X, Y), finalize = True)
    opt_out = False
    while verified == False and opt_out == False:
        if opt_out == True:
            break
    #check for key
        KeyHave = GL_Check_for_Key()
        if KeyHave == True: #if there is a key,
            if GL_Authenticate_UniqueKey() == False:     #attempt to authenticate it
                sim.popup_ok("This Unique Key is Not Authentic,\n Belongs to someone else")
                opt_out = True
            elif GL_Authenticate_UniqueKey() == True:
             #only when we authenticate the key, and it exists, are we sure that it is valid
                print("verified successfully")
                verified = True
                validated = 1 #update main to allow passage to next python page
                sim.popup_ok("Unique Key Successfully Verified!")

        elif KeyHave == False:                  #if check_for_key = false, there is no key and we need one
            print("There is no key detected")  #you need to generate a key if there isn't one.
            prewindow2 = sim.Window('Create Key?',Unique_Binary_Layout, size = (350, 180), finalize = True )
            minimenu = True
            while minimenu == True:
                eventpre2, values = prewindow2.read()
                if eventpre2 == "Yes":    #if they click yes
                    tempkey = GL_Gen_UniqueKey()   #we use the functions defined above
                    GL_Save_Key()
                    sim.popup_ok("Key Successfully Created!")
                    prewindow2.close()
                    verified = True
                if eventpre2 == "No":     #if they click No
                    prewindow2.close()
                if eventpre2 in (sim.WIN_CLOSED, 'Cancel'):  # if closed this happens
                    break


    #button events handled last
        if verified == True:

            validated = 1  # update main to allow passage to next python page
            break
        eventpre, values = prewindow.read()
        if verified == True:
            validated = 1  # update main to allow passage to next python page
            prewindow.close()
            break
        if eventpre == 'Quit':
            opt_out = True
            prewindow.close()
            break
        if eventpre in (sim.WIN_CLOSED, 'Cancel'): #if closed this happens
            break

    return validated
#Run_Validator() #<<<
