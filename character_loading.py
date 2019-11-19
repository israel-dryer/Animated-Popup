"""
    Simple Character Process/Loading Screen
    Author      :   Israel Dryer
    Modified    :   2019-11-18
"""
from threading import Thread
from time import sleep
import PySimpleGUI as sg 
sg.change_look_and_feel('Dark2')

STATUS = False

def your_process(seconds):
    """ simulated network connection test """
    global STATUS
    sleep(seconds)
    STATUS = True


def animated_popup():
    """ create animated popup window """
    msg = 'doing stuff.'
    ellipsis = '.'
    e_count = 0
    layout = [[sg.Text(msg, size=(16, 1), font=(sg.DEFAULT_FONT, 14), key='LOAD')]]
    window = sg.Window(
        'Loading...', layout=layout, element_justification='center', 
        size=(200, 60), margins=(15, 15), grab_anywhere=True, 
        keep_on_top=True, no_titlebar=True)

    while not STATUS:
        window.read(timeout=500)
        window['LOAD'].update(value = msg + (ellipsis * e_count))
        if e_count == 5:
            e_count = 0
        else:
            e_count += 1
    window.close()
    sg.popup_ok('Complete!', font=(sg.DEFAULT_FONT, 11)) 


def main():
    """ main program execution """
    sg.popup_ok('Begin Test', font=(sg.DEFAULT_FONT, 11))
    t1 = Thread(target=your_process, args=(8, ))
    t1.start()
    animated_popup()
 

if __name__ =="__main__":
    main()
  
