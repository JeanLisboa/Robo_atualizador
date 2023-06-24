from tkinter import *
from tkinter import ttk
root = Tk()

label1 = ttk.Label(root, text='label1')
label2 = ttk.Label(root, text='label2')
label1.pack()
label2.pack()

#associando um evento

label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label')) # qualquer botão do mouse
label1.bind('<1>', lambda e: print('<1> Label')) # apenas o botao 1 do mouse
root.bind('<1>', lambda e: print('<1> Root'))

# para desvincular o evento, use 'unbind'

# Para vincular um evento a todos os widgets dentro da janela, use:
root.bind_all('<Escape>', lambda e: print('<Escape!>'))

root.mainloop()