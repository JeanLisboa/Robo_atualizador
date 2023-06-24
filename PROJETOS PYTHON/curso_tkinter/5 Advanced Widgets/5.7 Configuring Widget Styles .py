from tkinter import *
from tkinter import  ttk
root = Tk()

button1 = ttk.Button(root, text='Button 1', command= lambda: print('botao 1'))
button2 = ttk.Button(root, text='Button 2', command= lambda: print('botao 2'))
button1.pack()
button2.pack()

#configuração de estilos
style = ttk.Style()
a = style.theme_names()
print(f'Estilos disponiveis {a}')

b = style.theme_use()
print(f'Estilo em uso {b}')

style.theme_use('vista') # para utilizar  o tema

# Para se referir ao tema, geralmente se usa a letra  "T" + o widget, ex TCombobox

# Para saber o nome
nome = button1.winfo_class()
print(nome)

#altera o estilo de todos os widgets indicados

style.configure('TButton', foreground='blue')

#criando um estilo personalizado
style.configure('Alarm.TButton', foreground='orange', font=('Arial', 24, 'bold'))
#Após a criação do novo estilo, defina onde ele será usado

button2.config(style='Alarm.TButton')

# ....

style.map('Alarm.TButton',foreground=[('pressed', 'pink'),('alternate','grey')])

"""
STANDARD OPTIONS

            class, compound, cursor, image, state, style, takefocus,
            text, textvariable, underline, width

WIDGET STATES

            active, disabled, focus, pressed, selected, background,
            readonly, alternate, invalid
"""

#para ver quais elementos compõe um estilo, use o metodo layout

estilos = style.layout('TButton')

print(f'estilos>>>> {estilos}')

#existem 4 elementos que existem em uma hierarquia. O elemento de botão de nível superior.
# O elemento de nivel superior representa a borda ao redor do widget.
# O elemento 'Focus' é a parte que muda de cor quando o widget tem foco de entrada
# O elemento 'Padding' contém texto e  imagem, contem os elementos nsew, que é o alinhamento

#verifica as opções disponíveis para o elemento
op_estilo = style.element_options('Button.label')

print(f'Opções do estilo >>> {op_estilo}')




root.mainloop()