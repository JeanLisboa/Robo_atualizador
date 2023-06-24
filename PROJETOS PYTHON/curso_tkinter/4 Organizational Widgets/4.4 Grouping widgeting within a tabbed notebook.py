from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()
root.title('Sistema de Integração')
root.state('zoomed')
notebook = ttk.Notebook(root)
notebook.pack()
#criando os frames
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
frame3 = ttk.Frame(notebook)
#adicionando e renomeando os frames no notebook
notebook.add(frame1, text='Expedição')
notebook.add(frame2, text='Agendamento')
notebook.add(frame3, text='Entrega')


#criando um botão o frame 1

ttk.Button(frame1, text='Ok').pack()
ttk.Button(frame1, text='Cancelar').pack()
#identificando qual guia foi selecionada

a = notebook.index(notebook.select())
print(a)
#como desabilitar uma guia
# utilizar o '.tab' é semelhante a usar o .config

# notebook.tab(1, state='disabled')

#oculta a guia

# notebook.tab(1, state='hidden') 'normal' para reexibir a guia
# exibe o texto da guia ativa
b = notebook.tab(1, 'text')
print(b)
#exibir todas as propriedades da guia ativa

c = notebook.tab(1)
print(c)
root.mainloop()
