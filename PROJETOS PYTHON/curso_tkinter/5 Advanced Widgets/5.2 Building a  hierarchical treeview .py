from tkinter import *
from tkinter import  ttk
root = Tk()
treeview = ttk.Treeview(root)
treeview.pack()
#parâmetros:
#nó raiz / posiçao na lista / items id / caption
#
treeview.insert('','0','item1', text='first item' )
treeview.insert('','1','item2', text='second item')
treeview.insert('','end','item3', text='third item' )
logo = PhotoImage(file='python_logo.gif').subsample(10,10)

#insere um sub item no item2
treeview.insert('item2','end','python', text='python',image=logo)
treeview.insert('item3','end','submenu',text='submenu')
treeview.config(height=5)

#move o item de > para
treeview.move('item2', 'item1','end') #move o item2 para dentro do item1, e o aloca no final
treeview.item('item1',open=True)#altera para 'expandida'

# treeview.detach('item3') #remove o item da árvore, mas ele ainda existe.... para  excluir, use o .delete

#insere uma coluna
treeview.config(columns=('version'))
treeview.column('version', width=50, anchor='center') # anchor é o alinhamento

treeview.column('#0',width=150) #define a largura da coluna

treeview.heading('version',text='Version')#define o  título
treeview.heading('#0',text='Menu', anchor='w')#define o  título

#insere informações correspondentes na coluna version
treeview.set('python','version','3.4.1' )
treeview.set('submenu','version','extemp')


#cria tags, marcações

treeview.item('python', tags=('software')) # define o python com a tag software
treeview.tag_configure('software',background='yellow') #marca o tag

#limita a seleção a apenas 1  por vez
treeview.config(selectmode='browse') # none
#criação de eventos virtuais

# def callback (event):
#     print(treeview.selection())
#     treeview.bind('<<<TreeviewSelect>>',callback)



root.mainloop()
def callback (event):
    print(treeview.selection())
    treeview.bind('<<<TreeviewSelect>>',callback)
