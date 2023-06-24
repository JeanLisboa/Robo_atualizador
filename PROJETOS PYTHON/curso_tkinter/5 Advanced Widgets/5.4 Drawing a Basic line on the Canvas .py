from tkinter import *
from tkinter import  ttk
root = Tk()
canvas = Canvas(root)
canvas.pack()

canvas.config(width=600, height=480)
#
line = canvas.create_line(100, 100, 480, 360, fill='blue', width=2)
canvas.itemconfigure(line,fill = 'green')
canvas.coords(line) # informa as coordenadas da linha

#as coordenadas da linha podem ser alteradas
canvas.coords(line, 0, 0, 320, 240, 640, 0)

#suavizando a linha
canvas.itemconfigure(line, smooth = True)
canvas.itemconfigure(line,splinesteps = 100)
# canvas.delete(line) # para deletar a linha


root.mainloop()