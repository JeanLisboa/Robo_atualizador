from tkinter import *
from tkinter import  ttk
root = Tk()

text = Text(root, width=40, height=10, wrap='word')
text.grid(row=0, column=0)
scrollbar = ttk.Scrollbar(root,orient=VERTICAL,command=text.yview) #command indica para onde o scroll vai rolar quando for acionado
#adicionando o scroll à janela
scrollbar.grid(row=0, column=1, sticky='ns')
text.config(yscrollcommand=scrollbar.set) # configura a barra de rolagem de acordo com a posiçao do cursor
root.mainloop()