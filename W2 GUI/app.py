import PySimpleGUI as sg

layout = [
    [sg.Text("Enter filename:"),sg.Input(key='FILE')],
    [sg.Text("Enter text:"),sg.Input(key='INPUT')],
    [sg.Button('Create'),sg.Button('Exit')]    
    ]

window = sg.Window('Text file creator', layout)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    # TO DO LIST
    # Write inputted text to file name using given file name
    elif event is 'Create':
        newFile = open(values['FILE'],"w")
        newFile.write(values['INPUT'])
        newFile.close()

window.close()