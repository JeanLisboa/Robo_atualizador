from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()

root.title('janela principal')
root.state('zoomed')

window = Toplevel(root) # cria uma nova janela
window.title('janela secundária')
window.config(width=500, height=100)
# window.lower()
window.lift(root)#  cria uma janela abaixo da principal
window.state('withdrawn') # oculta a janela, inclusive da barra de tarefas
window.state('iconic') #minimiza a janela, mas a deixa disponível na barra de tarefas
window.state('normal') # volta a janela ao tamanho anterior
window.state() # chamando sem parâmetros, vai mostrar o estado atual da  janela
window.iconify() # minimiza a janela para que ela fique visivel na barra de tarefas
window.deiconify() # retorna a janela ao estado normal (diferente do >> window.state('normal') << que volta ao estado anterior)
window.geometry('640x400+50+100') #widthxheightxXxY    >>> x e y referem á posição na tela
window.resizable(True, True) # define se a janela poderá ser redimensionada
window.maxsize(640,640) # define o tamanho máximo de redimensionamento de X e Y
window.minsize(200,200)
# root.destroy() # fecha a janela ( e todas as filhas tambem)

root.mainloop()
