from tkinter import *
from tkinter import ttk
root = Tk()

entry=ttk.Entry(root)
entry.pack()

#vinculando ao evento virtual

entry.bind('<<Copy>>', lambda e: print('Copy'))
entry.bind('<<Paste>>', lambda e: print('Paste'))

#criando um novo evento

entry.event_add('<<par>>','2','4','6','8')
entry.event_add('<<impar>>','1','3','5','7','9')
entry.bind('<<impar>>', lambda e: print('impar!'))
entry.bind('<<par>>', lambda e: print('par!'))
a = entry.event_info('<<impar>>')
print(a)

#acionando programaticamente dentro do código
entry.event_generate('<<impar>>')
entry.event_generate('<<Paste>>')


#excluíndo um everto virtual
entry.event_delete('<<impar>>')

root.mainloop()