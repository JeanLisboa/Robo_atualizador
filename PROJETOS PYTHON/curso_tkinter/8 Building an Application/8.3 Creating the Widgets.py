"""
Objetivos do projeto:
Criar um formulário de feedback para os clientes que concluíram o passeio From desert to sea para deixar
suas experiências.

Requisitos para o formulário:

O Formulário exibirá o logotipo circular 'do deserto  ao mar', juntamente com uma mensagem para o usuário,
convidando-o para deixar comentários sobre o passeio.

O usuário pode inserir nome, email adress and multiline comments

o Formulário deverá ter dois botões, submit e clear

Ao pressionar o botão submit, 3 coisas deverão acontecer:
    print do conteúdo dos campos no console
    limpar o conteúdo dos campos
    notificar ao usuário que a mensagem foi enviada com sucesso.

Ao pressionar o botão 'clear'
    limpar os campos


"""

from tkinter import *
from tkinter import ttk



# o formulário é implementado com uma classe:

class Feedback:  #
    def __init__(self, master):
        pass

def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__=='__main__': main()