# callback é o que acontece quando um widget é acionado

from tkinter import *
from tkinter import ttk
root = Tk()


def callback(number):
    print(number)


# atenção... a função deve ser inserida sem o parênteses, pois se tiver será chamada automaticamente
#  e não com a ação do usuário em apertar o botão.

# usando o lambda, ao rodar o cod, a função não será chamada automaticamente.
# ao invés disso, ela estará passando um numero para a função 'callback', que será passada para o print
ttk.Button(root, text='1', command=lambda: callback(1)).pack()
ttk.Button(root, text='2', command=lambda: callback(2)).pack()
ttk.Button(root, text='3', command=lambda: callback(3)).pack()







root.mainloop()