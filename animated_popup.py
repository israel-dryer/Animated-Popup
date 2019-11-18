from threading import Thread
from time import sleep
import PySimpleGUI as sg 

STATUS = False
IMAGES = ['spin1.png', 'spin2.png', 'spin3.png', 'spin4.png', 'spin5.png', 'spin6.png', 'spin7.png', 'spin8.png']

def test_connection(seconds):
    """ simulated network connection test """
    global STATUS
    sleep(seconds)
    STATUS = True

def animated_popup():
    """ create animated popup window """
    
    def image_iter() -> iter:
        """ create generator for animated popup images """
        return ('Images/' + image for image in IMAGES)
    
    img = image_iter()
    
    layout = [[sg.Text('Testing network connection...')],[sg.Image(filename=next(img), key='LOAD')]]
    window = sg.Window('Loading...', layout=layout, element_justification='center', 
                        keep_on_top=True, grab_anywhere=True, no_titlebar=True)

    while not STATUS:
        window.read(timeout=150)
        try:
            window['LOAD'].update(filename=next(img))
        except StopIteration:
            img = image_iter()
            window['LOAD'].update(filename=next(img))
    window.close()
    sg.popup_ok('Ready to go') 


def main():
    """ main program execution """
    t1 = Thread(target=test_connection, args=(10, ))
    t1.start()
    animated_popup()
   

main()
