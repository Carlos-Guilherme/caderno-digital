import PySimpleGUI as sg
import os

def save_file():
    text = window['-text-'].get()
    file_path = sg.popup_get_file('Salvar Nota', save_as=True)
    if file_path:
        if not file_path.endswith('.txt'):
            file_path += '.txt'
        with open(file_path, 'w') as f:
            f.write(text)
        sg.popup("Nota salva!")

# Define a janela
def diario():
    sg.theme('DarkGreen3')
    layout = [[sg.Multiline(size=(80,20), key='-text-', background_color='DimGray')],
            [sg.Button('Salvar'), sg.Button('Exit'), sg.Button('Resetar')]]

    return sg.Window('Diário', layout, finalize=True)

window = diario()

# Loop de eventos
while True:
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    elif event == 'Salvar':
        save_file()
    elif event == "Resetar":
        window.close()
        window = diario()

