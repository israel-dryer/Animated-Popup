"""
    Sample Splash Screen with images and loading progress bar
    Author      :   Israel Dryer
    Modified    :   2019-11-20
"""
import PySimpleGUI as sg
from threading import Thread
from time import sleep

images = ['images/water_1.png', 'images/water_2.png', 'images/water_3.png', 'images/water_2.png']
img_iter = iter(images)

messages = iter([
    'checking weather reports for tides and currents...',
    'passing out life-jackets...',
    'designating the skipper...',
    'checking for on-board safety equipment...',
    'turning on the GPS and other equipment...',
    'filling the gas tank...',
    'inspecting the engine...',
    'grabbing the case of beer...',
    'programming destination coordinates...',
    'setting sail for an adventure!!!' ])

def change_message():
    try:
        return next(messages)
    except StopIteration:
        return 'setting sail for an adventure!!!'

def animate_water():
    global img_iter, images
    try:
        return next(img_iter)
    except StopIteration:
        img_iter = iter(images)
        return next(img_iter)

# --- SOME SIMULATED PROCESS -------------------------------------------------
bar_count = 0
active = True

def some_external_process():
    """ put whatever you want here """
    global bar_count, active
    while bar_count < 100:
        bar_count += 1
        sleep(0.1)
    active = False

# --- GUI --------------------------------------------------------------------
def splash_gui():
    layout = [
        [sg.Text('Splash Screen', justification='center', text_color='#234988', font=('Tahoma', 30), pad=((5, 5), (25, 5)))],
        [sg.Text('Splash Screen Demo for Your Program', justification='center', size=(50, 1), 
                text_color='#234988', font=('Tahoma', 10), pad=((5, 5), (10, 25)), key='MSG')],
        [sg.Text('0%', size=(5, 1), text_color='#234988', font=('Tahoma', 12), pad=((5, 5), (5, 12)), key='PCT')],
        [sg.Image('', key='BOAT')],
        [sg.ProgressBar(max_value=100, orientation='h', border_width=1, size=(25, 25), 
                        bar_color=('#199FD0', '#FFFFFF'), key='PRG')],
        [sg.Image(filename='images/water_3.png', key='WATER')]]

    return sg.Window('splash', layout, no_titlebar=True, element_justification='center', 
        size=(500, 300), margins=(0, 0), alpha_channel=1, grab_anywhere=True, keep_on_top=True)

def gui_event_loop(window):
    global bar_count, active
    while active:
        window.read(100)
        window['PRG'].update_bar(current_count=bar_count)
        window['PCT'].update(value="{}%".format(bar_count))
        if bar_count%10 == 0:
            window['MSG'].update(value=change_message())
        if bar_count%4 == 0:
            window['WATER'].update(filename=animate_water())

    window['PRG'].update(visible=False)
    window['PCT'].update(visible=False)
    window['WATER'].update(visible=False)
    window['MSG'].update(font=('Tahoma', 12, 'bold'))
    window['BOAT'].update(filename='images/sailing.png')
    window.read(3000)
    window.close()

def main():
    t1 = Thread(target=some_external_process)
    t1.start()
    window = splash_gui()
    gui_event_loop(window)

if __name__=='__main__':
    main()    