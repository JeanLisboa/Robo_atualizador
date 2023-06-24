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
from tkinter import messagebox



# o formulário é implementado com uma classe:

#master é a janela principal
class Feedback:  #
    def __init__(self, master): #aqui devem ser criados todos os widgets
        # quadro superior da janela master
        self.frame_header = ttk.Frame(master) # este Frame é filho de 'master'
        self.frame_header.pack()

        self.logo = PhotoImage(file='tour_logo.gif')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text= 'Thanks for Exploring').grid(row=0, column=1)
        ttk.Label(self.frame_header, text=" We're glad you chose Explore Califórnia for you recent adventure.\n"
                                          "Please, tell us what you thought about the 'Desert to Sea' Tour ").grid(row=1, column=1)
        # quadro inferior da janela master

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()
        ttk.Label(self.frame_content, text='Name').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='E-Mail').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Comments').grid(row=2, column=0, columnspan=2, padx=5, sticky='sw')

        # para criar os campos de entrada e texto, já que será necessário acessá-los
        # posteriormente, utilizando o GIT será necessário armazenar referências a esses
        # objetos em variáveis de classe variável de classe para o nome da entrada,

        self.entry_name = ttk.Entry(self.frame_content, width= 24)
        self.entry_email = ttk.Entry(self.frame_content, width= 24)
        self.text_comments = Text(self.frame_content,width=50, height=10) # não está na bibl 'TK"

        self.entry_name.grid(row=1, column=0, padx=5, sticky='sw')
        self.entry_email.grid(row=1, column=1, padx=5, sticky='sw')
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5, sticky='sw')
        ttk.Button(self.frame_content, text='Submit', command=self.submit).grid(row=4, column=0, padx=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear', command=self.clear).grid(row=4, column=1, padx=5, sticky='w')

    def submit(self):
        print(f'Name: {self.entry_name.get()}')
        print(f'Email: {self.entry_email.get()}')
        print(f'Comments: {self.text_comments.get(1.0, "end")}')
        messagebox.showinfo(title="Explore California Feedback", message="Comments Submited")
        self.clear()

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')


def main():
    root = Tk()

    feedback = Feedback(root)
    root.mainloop()


if __name__=='__main__': main()