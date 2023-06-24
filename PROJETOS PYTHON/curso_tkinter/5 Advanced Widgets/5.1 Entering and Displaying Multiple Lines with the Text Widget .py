from tkinter import *
#o widget  de texto não é um widget temático, por isso ottk não será usado.

root = Tk()
text = Text(root, width=40, height=10)
text.pack()

#configura a quebra de linha
# char é o padrão... quebra a linha no ponto exato
# none - não quebra a linha
text.config(wrap='word')

#marcar o texto
text.tag_add('my tag','1.0', '1.0 wordend')
text.tag_configure('my tag', background='yellow')

#text.insert insere o texto na caixa
text.insert('1.0 + 2 lines', 'imagine um textão digitado aqui')
text.insert('1.0 + 2 lines lineend', 'imagine um textão digi\ntado aqui......e outro\naqui') # insere no final da linha >>> \n para quebrar o texto

#
#metodo get retorna o índice de um lugar no texto ou uma cadeia  de caracteres

#1.0 significa 'linha 1, posição 0 ( antes do primeiro caractere)
a = text.get('1.0', 'end')
#1.end significa 'até o final da primeira linha

text.get('1.0','1.end')
print(a)

#deletar  a msg
# text.delete('1.0')
# text.delete('1.0', '1.0 lineend')

# substituir um texto
text.replace('1.0','1.0 lineend','this is the first line')
# desabilita
text.config(state='disabled') # use state=normal para habilitar

root.mainloop()
