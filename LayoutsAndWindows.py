#default main menu layout goes here:
Main_Menu_width = X = 600     #change width and height of default window
Main_Menu_Height = Y = 400

Main_Menu_Layout = [
            [sim.Text('Grid Lock         ')],
            [sim.Text(' \n \n \n \n \n')], #top margin
           #[sim.Input(key='-IN1-')], #key for mirroring
            [sim.Text('App/Site Name')],
            [sim.InputText()],
            [sim.Text('Username')],
            [sim.InputText()],      # these are all on different lines to keep them apart
            [sim.Text('Password')],
            [sim.InputText()],
            [sim.Text('\n')],  # bottom margin
            [sim.Button('Save'), sim.Button('Load')]
                   ] #end of default window
#__________________

#----launch window (For Key Validator)
window = sim.Window('Grid Lock', Main_Menu_Layout, size = (X, Y), finalize = True)
Unique_Menu_width = X = 500    #change width and height of default window
Unique_Menu_Height = Y = 350
sim.theme('LightGrey6')
Unique_Menu_Layout = [
            [sim.Text('  GridLock is working to Validate your Unique User Key   ')],
            [sim.Text(' \n \n\n \n')], #top margin
            #[sim.Input(key='-IN1-')], #key for mirroring
            [sim.Text(' '),sim.Button('Quit')]
                   ] #end of default window
#__________________
#----launch window
