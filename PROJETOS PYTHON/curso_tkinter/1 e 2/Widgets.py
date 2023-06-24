from tkinter import *
from tkinter import ttk

root = Tk()
button = ttk.Button(root, text="clique em mim!")

button.pack()

print(button['text'])
button['text'] = 'aperte'  #altera o texto, após o botão ter sido crido
button.config(text='Empurre') # mais uma forma de alterar o texto
print(button.config()) # sem nenhum parãmetro, ele retorna um dict com todas as propriedades do 'config'

ttk.Label(root, text = 'Hello Tkinter!!').pack()



root.mainloop()