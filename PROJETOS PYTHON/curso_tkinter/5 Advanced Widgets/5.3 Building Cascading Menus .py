from tkinter import *
from tkinter import  ttk
root = Tk()
root.option_add('*tearOff',False) # mantém a compatibilidade com versões anteriores


#cria  a barra de menu, filha da janela root
menubar = Menu(root)
#adiciona a barra de menu à janela root
root.config(menu=menubar) # informa que o menu do root será o menubar

# cada item da barra de menu será filho da 'menubar'
file = Menu(menubar)
edit = Menu(menubar)
help_= Menu(menubar)
#adiciona o item do memu à barra
menubar.add_cascade(menu= file, label= 'File')
menubar.add_cascade(menu= edit, label= 'Edit')
menubar.add_cascade(menu= help_, label= 'Help')

#adiciona itens ao menu
file.add_command(label='New', command = lambda: print('new file'))
file.add_separator() # insere uma linha entre os menus
file.add_command(label='Open', command = lambda: print('Open File...'))
file.add_command(label='Save', command = lambda: print('Save'))

#define um atalho
file.entryconfig('New',accelerator = 'Ctrl + N') #apenas informa no menu...aqui ainda falta a configuração do atalho
logo = PhotoImage(file='python_logo.gif').subsample(10,10)
file.entryconfig('Open', image=logo, compound='left') # carrega a imagem à esquerda do Open
# file.entryconfig('Open',state='disabled') # desabilita o item do menu

#adiciona um submenu
save = Menu(file) #perceba que aqui ele será filho de um item do menu..
file.add_cascade(menu = save, label='Salvar')
save.add_command(label='Save As', command= lambda: print('Saving as...'))
save.add_command(label='Save All', command= lambda: print('Saving All...'))

#cria um radiobutton no menu 'edit'
#IntVar é um método construtor
choice  = IntVar
# variable=choice atribui o botão à variável e value é o valor que retornará, se o botao for selecionado
edit.add_radiobutton(label='One', variable=choice,value=1)
edit.add_radiobutton(label='Two', variable=choice,value=2)
edit.add_radiobutton(label='Three', variable=choice,value=3)

#cria um menu estilo pop-up na tela

# file.post(400,300) # 400,300 define a posição na tela



root.mainloop()