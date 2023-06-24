#tipos de gerenciadores de geometria no tkinter
#pack -
 # pros:
 # é o mais simples de usar
 # use quando o widget será expaandido para preencher todo o pai
 # use quando for pilhar os widgets, vertical ou horizontalmente
 # Contras
 #inadequado para layouts complexos

#grid
#place

from tkinter import *
from tkinter import ttk

root = Tk()

#fazendo desta forma, por padrão, o widget será empilhado no topo da janela.
# ao redimensionar a  janela, o label permanecerá centralizado

# ttk.Label(root, text='Hello Tkinter!', background='yellow').pack()

#3 ao redimensionar a janela, o label permanecerá inalterado. PAra que ele seja também redimensionado, é preciso utilizar,
# dentro do pack() os parâmetros  >>> .pack(fill e expand
#fill = X, ou Y ou BOTH (preenche apenas na horizontal
#expand = True ou False  (preenche na vertical)

#ao utilizar vários labels, veja o efeito:

# ttk.Label(root, text='Hello Tkinter!', background='yellow').pack(fill=BOTH)
# ttk.Label(root, text='Hello Tkinter!', background='blue').pack(fill=BOTH)
# ttk.Label(root, text='Hello Tkinter!', background='green').pack(fill=BOTH)

# no caso acima, percebe-se que os widgets serão empilhados conforme o gerenciador é chamado.
# é simples, mas tornará a manutenção do código complicada, quando for necessário adicionar novos widgets.

# para empilhar horizontalmente, veja abaixo:  >> side  LEFT
ttk.Label(root, text='Hello Tkinter!', background='yellow').pack(side=LEFT, anchor='n')
ttk.Label(root, text='Hello Tkinter!', background='blue').pack(side=LEFT, padx=20, pady=20)
ttk.Label(root, text='Hello Tkinter!', background='green').pack(side=LEFT, anchor='sw', ipadx= 20, ipady=20)

# side = LEFT faz com que os widgets sejam organizados contra o lado esquerdo
# sempre na ordem em que foram chamados
# Por padrão, quando a janela é redimensionada, os widgets filhos são centralizados.
# caso seja necessário alterar, utilize a propriedade 'anchor' .... os parametros são os pontos cardinais
# os parâmetros padx e pady acrescentam preenchimento externo ao widget
# os parâmetros ipadx e ipady acrescentam preenchimento interno ao widget


# caso queira uma alteração que abarque todos os widgets contidos na janela pai, é possível fazer da seguinte forma:

for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand=True)
    print(widget.pack_info()) # exibe todas as propriedades do widget




root.mainloop()
