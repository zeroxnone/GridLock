#beta test ui
#do note edit without team permission
import PySimpleGUI as sim
sim.theme('LightGrey6')

def LaunchInterface():
    global sitename, username, password, sitemirror, usermirror, passmirror
    sitename = ""
    username = ""
    password = ""
    sitemirror = ""  # mirrors to be turned into truncated strings as apposed to their tuple counterparts
    usermirror = ""
    passmirror = ""

    # default main menu layout goes here:
    Main_Menu_width = X = 600  # change width and height of default window
    Main_Menu_Height = Y = 500

    Main_Menu_Layout = [
        [sim.Text('               '), sim.Image('JustALock3.png')],  # drag image at the top
        [sim.Text('                          Grid Lock         ')],
        [sim.Text(' \n')],  # top margin
        # [sim.Input(key='-IN1-')], #key for mirroring
        [sim.Text('App/Site Name')],
        [sim.InputText()],
        [sim.Text('Username')],
        [sim.InputText()],  # these are all on different lines to keep them apart
        [sim.Text('Password')],
        [sim.InputText()],
        [sim.Text('\n')],  # bottom margin
        [sim.Button('Save'), sim.Button('Load')]
        ]  # end of default window
    # __________________

    # ----launch window
    window = sim.Window('Grid Lock Password Security', Main_Menu_Layout, size=(X, Y), finalize=True)

    # MAIN: Event Loop to process "events"
    while 1 == 1:
        event, values = window.read()
        sitename = (event, values[1])
        username = (event, values[2])
        password = (event, values[3])
        # these commands turn tuplets into single string values.
        usermirror = (str(username)[10:-2])
        sitemirror = (str(sitename)[10:-2])
        passmirror = (str(password)[10:-2])
        # the next following if tree
        if event in (sim.WIN_CLOSED, 'Cancel'):  # if closed this happens
            break
            # basic debug strings for testing purposes, keep these but comment them out
        print(event, values)
        print(str(sitemirror) + ' ' + str(usermirror) + ' ' + str(passmirror))
        if event == 'Save':  # If you press the Save button
            # window['-IN1-'].update(sitemirror + " \n" + usermirror + " \n" + str(passmirror) + " \n")
            for i in range(1, 100):
                sim.one_line_progress_meter('Saving In Progress', i + 1, 100, 'Save_Begin', 'Saving your Login Info')
                # you should put save stuff here.
        if event == 'Load':
            PasswordLoad_layout = [
                [sim.Text('Select Your Login')],
                [sim.Listbox(values=['Netflix', 'Facebook', 'Youtube', 'Google', 'Youtube'], size=(40, 25))],
                #!!!! replace with actual list please
                [sim.Button('Back'), sim.Button('Load Password')]]
            endflag2 = False
            window2 = sim.Window('Grid Lock Loading Password', PasswordLoad_layout)

            while endflag2 == False:
                event2, values2 = window2.read()
                if event2 == 'Back':
                    endflag2 = True
                    window2.close()
                    print("Back")
                if event2 == 'Load Password':
                    # this is where we launch the saving function
                    target = str(window2.read())[24:-4]
                    print("Load Password for: ", target)

