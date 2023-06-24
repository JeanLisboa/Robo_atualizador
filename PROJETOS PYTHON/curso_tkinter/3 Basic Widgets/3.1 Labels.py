from tkinter import *
from tkinter import ttk

root = Tk()
label = ttk.Label(root,text="Hello Everybody")
label.pack()
label.config(text='Olá Mundo!') # altera o texto do label
label.config(wraplength=150) # altera o tamanho do texto antes que haja a quebra
label.config(justify=RIGHT)# OPCOES = RIGHT, LEFT, CENTER
label.config(foreground='blue', background='yellow')
label.config(font=('tahoma', 18,'bold'))
logo = PhotoImage(file='python_logo.gif')
label.config(compound='right') # propriedade que altera a posição da imagem
#  opções para a propriedade 'compound'  são 'center', 'left'  and 'right'

# ass duas linhas abaixo servem para configurar o label a usar a imagem
label.img = logo
label.config(image=label.img)


label.config(image=logo)
root.mainloop()