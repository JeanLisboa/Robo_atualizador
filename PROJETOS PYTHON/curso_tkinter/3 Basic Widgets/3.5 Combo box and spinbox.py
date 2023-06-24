from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()

month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()
combobox.config(values=('jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'))
5
year = StringVar()
Spinbox(root, from_=1990, to=2014, textvariable=year).pack()




root.mainloop()


