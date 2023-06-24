# The place Geometry manager provides exact control of widget location and size
# Describes locatiton in absolute and/or relative terms
# pode ser dificil gerenciar muitos widgets


from tkinter import *
from tkinter import ttk
root=Tk()
root.geometry('600x480+200+200')


ttk.Label(root,text='Yellow', background='yellow').place(relx=0.5, rely=0.5, x=-50, y=100, anchor='center')
root.mainloop()