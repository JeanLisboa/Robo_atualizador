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

#cada par de coordenadas se refere a um canto do retangulo
rect = canvas.create_rectangle(160, 120, 480, 360)

#altera o preenchimento
canvas.itemconfigure(rect, fill = "yellow")
#outros
oval = canvas.create_oval(160, 120, 480, 360)

arc = canvas.create_arc(160, 1, 480, 240)

#configura inicio e fim do arco
canvas.itemconfigure(arc, start=0, extent=180, fill = 'green')


poly = canvas.create_polygon(160,360, 320, 480, 480, 360, fill='blue')

#adicionando texto
text = canvas.create_text(320, 240, text='Python', font=('Tahoma', 32, 'bold'))

#adiciona  imagem
logo = PhotoImage(file='python_logo.gif')#.subsample(10,10)
image = canvas.create_image(320, 480, image=logo)
canvas.lift(text) #move a imagem para trás do texto
canvas.lower(image) #move para baixo de todos

button = Button(canvas,text='Click me')
canvas.create_window(320, 60, window=button)

#cria tags para as formas
canvas.itemconfigure(rect, tag = 'shape')
canvas.itemconfigure(oval, tag = 'shape')
canvas.itemconfigure('shape', fill='grey') #a configuração se aplicará apenas aos itens com id 'shape'
root.mainloop()