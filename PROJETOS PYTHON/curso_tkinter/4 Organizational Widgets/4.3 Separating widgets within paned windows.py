from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()

#paned window = janela panorâmica
# paned window é um widget de gerenciamento de geometria que pode conter outros widgets,
# empilhando-os vertical ou horizontalmente. A janela panorâmica exibe um divisor entre cada
# um dos widgets, que o usuário pode clicar e arrastar para ajustar o tamanho relativo dos
# widgets dentro da janela. Embora qualquer tipo de widget possa ser adicionado à janela do painel,
# ele é comumente usado para manter vários quadros próximos uns dos outros para permitir que o usuário
# os redimimensione facilmente

#Panedwindow é o métodod construtor de janela panorâmica

panedwindow = ttk.Panedwindow(root, orient=HORIZONTAL) # orient = o parâmetro que indica como os widgets serao mostrados
panedwindow.pack(fill=BOTH, expand=True)
# os frames abaixo serão filhos de panedwindow
frame1 = ttk.Frame(panedwindow, width=100, height=300, relief=SUNKEN)
frame2 = ttk.Frame(panedwindow, width=400, height=400, relief=SUNKEN)
# root.resizable(False,False)
#adicionando os frames 'filhos' ao panedwindow
panedwindow.add(frame1, weight=1) # a propriedade weight especifica o quanto do quadro será dimensionado quando janela for dimensionada
panedwindow.add(frame2, weight=1) # a propriedade weight especifica o quanto do quadro será dimensionado quando janela for dimensionada
# cria um novo frame filho

frame3 = ttk.Frame(panedwindow, width=50, height=400, relief=SUNKEN)
#adiciona o novo frame ao pai
panedwindow.insert(1, frame3) # 1 é o index, a posição dele no frame pai

#excluindo um frame do paned
panedwindow.forget(1) # basta apenas informar a posição index


root.mainloop()
