# callback é o que acontece quando um widget é acionado

from tkinter import *
root = Tk()


# KEYBOARD EVENTS
# EVENTS FORMAT     |   EVENT DESCRIPTION
#----------------------------------------------------
# <Key> <keyPress>     | User pressed any key
# <Keypress-Delete>    | User pressed delete key
# <KeyRelease-Right    | User released Right Arrow key
# a,b,c etc <space>,   | User pressed a 'printable key
# <less>               |
#<SHIFT_L>, <Control_R>| User pressed a 'special' key
# <F5>, <UP>           |
# <Return>             | User pressed the enter key
# <CONTROL-ALT-NEXT    |
def key_press(event):
    print(f'Type: {event.type}')
    print(f'Widget: {event.widget}')
    print(f'Char: {event.char}')
    print(f'Keysym: {event.keysym}')
    print(f'Keycode: {event.keycode}')

def shortcut(action):
    print(action)

root.bind('<Control-c>', lambda u: shortcut('Copy')) # nao colocar o argumento no lambda resulta em erro >>> lambda u:
root.bind('<Control-v>', lambda u: shortcut('Paste'))

root.mainloop()