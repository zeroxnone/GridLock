#beta test ui
#do note edit without team permission
import PySimpleGui as sim
sim.theme('DarkTeal6')

sitename = ""
username = ""
password = ""
sitemirror = "" #mirrors to be turned into truncated strings as apposed to their tuple counterparts
usermirror = ""
passmirror = ""
#default main menu layout goes here:
Main_Menu_Layout = [
            [sim.Text('                              Grid Lock         ')],
            [sim.Text(' \n \n \n \n \n \n \n')],
           #[sim.Input(key='-IN1-')], #key for mirroring
            [sim.Text('App/Site Name')],
            [sim.InputText()],
            [sim.Text('Username')],
            [sim.InputText()],      # these are all on different lines to keep them apart
            [sim.Text('Password')],
            [sim.InputText()],
            [sim.Button('Save'), sim.Button('Load')]
                   ] #end of default window
#__________________

#----launch window
window = sim.Window('Grid Lock', Main_Menu_Layout)

# MAIN: Event Loop to process "events"
while 1 == 1:
    event, values = window.read()
    sitename = (event, values[0])
    username = (event, values[1])
    password = (event, values[2])
    #these commands turn tuplets into single string values.
    usermirror = (str(username)[10:-2])
    sitemirror = (str(sitename)[10:-2])
    passmirror = (str(password)[10:-2])
    #the next following if tree
    if event in (sim.WIN_CLOSED, 'Cancel'): #if closed this happens
        break
        # basic debug strings for testing purposes, keep these but comment them out
    print(event, values)
    print(str(sitemirror) + ' '  + str(usermirror) + ' ' + str(passmirror))
    if event == 'Save': #If you press the Save button
        #window['-IN1-'].update(sitemirror + " \n" + usermirror + " \n" + str(passmirror) + " \n")
        for i in range(1, 1000):
            sim.one_line_progress_meter('Saving In Progress', i + 1, 1000, 'Save_Begin', 'Saving your Login Info')
            # you should put save stuff here.
    if event == 'Load':
        PasswordLoad_layout = [
            [sim.Text('Select Your Login')],
            [sim.Listbox(values=['Netflix', 'Facebook', 'Youtube', 'Google', 'Youtube'], size=(40, 25))],
            [sim.Button('Back')]]
        endflag = False
        window2 = sim.Window('Grid Lock', PasswordLoad_layout)
        while endflag == False:
            event2, values2 = window2.read()
            if event2 == 'Back':
                endflag = True
                window2.close()
                print("Back")


