from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()

checkbutton = ttk.Checkbutton(root, text='Spam ?')
checkbutton.pack()

""" 
tkinter variable classes:
Boolean Var
Double Var
Int Var
String Var

"""
spam = StringVar() #cria uma variável texto
spam.set('SPAM!') # envia texto da variável

print(spam.get()) #informa o valor da variável

#associando o checkbutton à variável spam
a = checkbutton.config(variable=spam, onvalue='Selecionado', offvalue='não selecionado')

#rdiobutton

breakfast = StringVar()
ttk.Radiobutton(root, text="SPAM", variable=breakfast, value='SPAM').pack()
ttk.Radiobutton(root, text="Eggs", variable=breakfast, value='Eggs').pack()
ttk.Radiobutton(root, text="Sausage", variable=breakfast, value='Sausages').pack()
ttk.Radiobutton(root, text="SPAM", variable=breakfast, value='SPAM').pack()
checkbutton.config(textvariable=breakfast) #este código altera o label do checkbutton de acordo com o que for selecionado no radiobutton
# ainda nao descobri a utilidade disto... mas

root.mainloop()


