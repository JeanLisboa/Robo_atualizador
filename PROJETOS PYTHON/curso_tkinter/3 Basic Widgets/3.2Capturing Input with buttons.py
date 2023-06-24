from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()

button = ttk.Button(root,text='Executar') # button é um objeto
#root é o primeiro parâmetro 'pai'
button.pack() # gerenciador de geometria para adicionar a janela

def callback(): # função para o botão
    print('Executado')

button.config(command=callback) # esta propriedade atribui o acionamento do botão à função... obs:  sem parênteses
button.invoke() # o método invoke simula o acionamento do botão
button.state(['disabled']) # este método desabilita o funcionamento do botão
button.state(['!disabled']) # altera o status para 'não' desabilitado
a = button.instate(['disabled']) # retorna se o botão está desabilitado true/false

# para verificar todos os métodos, acessar www.tcltk/man/tcl/tkcmd/ttk_widget.htm#m22

# alterar a imagem do botão

logo = PhotoImage(file='python_logo.gif')
button.config(image=logo, compound=LEFT)

#método para redimensionar as imagens
small_logo=logo.subsample(20,20) # pixels x,y  / quanto maior o número, menor será a imagem
button.config(image=small_logo)

print(a)

root.mainloop()