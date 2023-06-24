from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()

entry = ttk.Entry(root,width=30) #Entry é um método construtor de entrada
# entry.insert(0, 'Digite a senha: ')
entry.config(show='*')
entry.state(['readonly']) # somente leitura / disabled / !disabled
entry.pack()

root.mainloop()


