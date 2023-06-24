from tkinter import *
#botoes do mouse:
# esquerdo = 1
# scroll = 2
# direito = 3
#

# mouse EVENTS
# EVENTS FORMAT     |   EVENT DESCRIPTION
#----------------------------------------------------
# <Button> <ButtonPress>      | Any button was pressed
# <Button-1>, <ButtonPress-1> | Button 1 was pressed
# <ButtonRelease-1>           | Button 1 was released
# <Double(or triple)-Button-1>| Button 1 was double or triple clicked
root = Tk()
canvas = Canvas (root,width=640, height=400, background='white')
canvas.pack()
def mouse_press(event):
    global prev
    prev = event # utilizado para saber a posição anterior do mouse na função draw
    print(f'type: {event.type}')
    print(f'widget: {event.widget}')
    print(f'num: {event.num}')
    print(f'x: {event.x}') # posição do clique na area da janela
    print(f'y: {event.y}')
    print(f'x: {event.x_root}') # posição do clique na tela
    print(f'y: {event.y_root}')
canvas.bind('<ButtonPress>', mouse_press)

#criar método de desenho

def draw(event):
    global prev
    canvas.create_line(prev.x, prev.y, event.x, event.y,width = 1)
    prev = event # salva o evento atual na variável anterior

canvas.bind('<B1-Motion>', draw)

root.mainloop()