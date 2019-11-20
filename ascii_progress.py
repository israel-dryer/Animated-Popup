"""
    ASCII Progress Bar that can run independent of another process
    Author      :   Israel Dryer
    Modified    :   2019-11-18
"""
import PySimpleGUI as sg
from time import sleep
from threading import Thread

# ----- PROGRESS BAR ---------------------------------------------------------
theme = 'BrownBlue'
sg.change_look_and_feel(theme)
bar_colors = sg.LOOK_AND_FEEL_TABLE[theme]['BUTTON']

bar = "█"
bar_pct = 0
loaded = False

def get_bar_size():
    """ calculate progress bar size """
    msg = f"{bar * int(bar_pct//5)}]{bar_pct}%".ljust(35)
    return msg

def loading_popup():
    """ loading popup """
    layout = [
        [sg.Text('Loading...', font=('Tahoma', 12), pad=(5, 15)),
        sg.Text(text=' ]0%', font=('Tahoma', 12), background_color=bar_colors[0], 
                text_color=bar_colors[1], size=(30, 1), pad=(5, 15), key='LOADING'),
        sg.Button('OK', key='OK', size=(4, 1), disabled=True, border_width=0, font=('Tahoma', 12))]]

    window = sg.Window(
        title='Loading', layout=layout, keep_on_top=True, grab_anywhere=True, 
        no_titlebar=True, element_justification='center', finalize=True)

    while not loaded:
        window.read(timeout=50)
        window['LOADING'].update(value=get_bar_size())

    window['OK'].update(disabled=False)

    while True:
        event, values = window.read()
        if event in (None, 'OK'):
            break

# ----- DUMMMY PROCESS -------------------------------------------------------
def your_process():
    """ simulated file loading """
    global bar_pct, loaded
    while bar_pct < 100:
        bar_pct += 1
        sleep(0.1)
    loaded = True



# ----- MAIN ROUTINE ---------------------------------------------------------
def main():
    """ main program routine """
    sg.popup_ok('Load File')
    t1 = Thread(target=your_process)
    t1.start()
    loading_popup()

if __name__=='__main__':
    main()