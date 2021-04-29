import PySimpleGUI as sg
sg.theme('DarkAmber')

layout = [
    [sg.Text("Enter filename:"),sg.Input(key='FILE')],
    [sg.Text("Enter text:"),sg.Input(key='INPUT')],
    [sg.Button('Create'),sg.Button('Exit')],
    [sg.Text("Waiting", key='STATUS')]    
    ]

window = sg.Window('File creator', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    # TO DO LIST
    # Write inputted text to file name using given file name
    elif event is 'Create':
        window['STATUS'].update('Writing')
        newFile = open(values['FILE'],"w")
        newFile.write(values['INPUT'])
        newFile.close()

window.close()