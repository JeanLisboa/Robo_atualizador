#tipos de gerenciadores de geometria no tkinter
#grid
# Pros
#  Facilita a organização em duas dimensões
# Organização típica das GUI modernas

# Contras
# Exige mais planejamento antes de iniciar o cod


#place

from tkinter import *
from tkinter import ttk

root = Tk()

#planejamento

#         0      |      1
#   --------------------------
#   0    GREEN   |   ORANGE
#   --------------------------
#   1    BLUE    |   YELLOW

# ttk.Label(root, text='Yellow', background='yellow').grid(row=1,column=1)
# ttk.Label(root, text='Blue', background='blue').grid(row=1,column=0)
# ttk.Label(root, text='Green', background='green').grid(row=0,column=0)
# ttk.Label(root, text='Orange', background='orange').grid(row=0,column=1)

#planejamento

#         0      |      1      |
#   --------------------------
#   0    GREEN   |   ORANGE    |
#   ------------------------------ YELLOW
#   1           BLUE           |

# para configurar o yellow e o blue, será utilizada a propriedade rowspan e columnspan
# no caso dos widgets blue e yellow, o padrão é que sejam centralizados.

# Para que isso seja alterado, utilize a propriedade sticky para informar onde o widget será ancorado.
# Para expandir em toda a celula, utilize a propriedade sticky= 'nsew'
#
# para que os widgets sejam dimensionados junto à janela, utilize a propriedade 'rowconfigure' e 'columnconfigure' no WIDGET PAI

# o peso padrão é 0
# também podem ser utilizados os parâmetros pad e ipad
root.rowconfigure(0,weight=3) # 0 é o index da linha, ... expandirá 3 pixels a cada um que a row 1 expandir
root.rowconfigure(1,weight=1) # a linha 1 expandirá 1 pixel

root.columnconfigure(2,weight=3)


ttk.Label(root, text='Yellow', background='yellow').grid(row=0,column=2, rowspan=2, sticky='nsew')
ttk.Label(root, text='Blue', background='blue').grid(row=1,column=0, columnspan=2, sticky='nsew')
ttk.Label(root, text='Green', background='green').grid(row=0,column=0, sticky='nsew')
ttk.Label(root, text='Orange', background='orange').grid(row=0,column=1, sticky='nsew')


root.mainloop()