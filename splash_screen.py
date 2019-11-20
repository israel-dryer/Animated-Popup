"""
    Sample Splash Screen with images and loading progress bar
    Author      :   Israel Dryer
    Modified    :   2019-11-19
"""
import PySimpleGUI as sg

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

sg.LOOK_AND_FEEL_TABLE['custom'] = {
        'BACKGROUND': '#E8E8E8',
        'TEXT': '#234988',
        'INPUT': '#000000',
        'TEXT_INPUT': '#000000',
        'SCROLL': '#000000',
        'BUTTON': '#000000',
        'PROGRESS': ('#199FD0', '#FFFFFF'),
        'PROGRESS_DEPTH': 0,
        'BORDER': 1,
        'SLIDER_DEPTH': 0 }

# --- GUI LAYOUT -------------------------------------------------------------
sg.change_look_and_feel('custom')
layout = [
    [sg.Text('Splash Screen', justification='center', font=('Tahoma', 30), pad=((5, 5), (25, 5)))],
    [sg.Text('Splash Screen Demo for Your Program', justification='center', size=(50, 1), 
             font=('Tahoma', 10), pad=((5, 5), (10, 25)), key='MSG')],
    [sg.Text('0%', size=(5, 1), font=('Tahoma', 12), pad=((5, 5), (5, 12)), key='PCT')],
    [sg.Image('', key='BOAT')],
    [sg.ProgressBar(max_value=100, orientation='h', border_width=1, size=(25, 25), key='PRG')],
    [sg.Image(filename='images/water-small.png', key='WATER')]]

window = sg.Window(
    'splash', layout, no_titlebar=True, element_justification='center', size=(500, 300),
    margins=(0, 0), alpha_channel=1, grab_anywhere=True, keep_on_top=True)

# --- MAIN EVENT LOOP --------------------------------------------------------
bar_count = 0
while bar_count <= 100:
    window.read(100)
    window['PRG'].update_bar(current_count=bar_count)
    window['PCT'].update(value="{}%".format(bar_count))
    bar_count +=1
    if bar_count%10 == 0:
        window['MSG'].update(value=next(messages))

# --- CLOSING SEQUENCE -------------------------------------------------------
window['PRG'].update(visible=False)
window['PCT'].update(visible=False)
window['WATER'].update(visible=False)
window['MSG'].update(font=('Tahoma', 12, 'bold'))
window['BOAT'].update(filename='images/sailing.png')
window.read(3000)