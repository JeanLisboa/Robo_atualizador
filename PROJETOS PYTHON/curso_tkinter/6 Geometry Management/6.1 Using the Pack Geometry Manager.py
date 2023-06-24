from tkinter import messagebox

messagebox.showinfo(title='A friendly message', message='Hello Tkinter')

#tipos de msgbox
# showinfo()
# showwarning()
# showerror()

#type questions
# askyesno()
# askokcancel()
# askyesnocacancel()
# askquestion()


#para yes, retorno = True, para no, False
a= messagebox.askyesno(title='Hungry',message='Do you want SPAM :')

print(a)

from tkinter import filedialog

#arquivo selecionado
filename = filedialog.askopenfile()

print(filename.name)

# tipos de filedialog
# askdirectory()
# asksaveasfile()
# asksaveasfilename()

# askopenfile(mode)
# askopenfiles(mode)
# askopenfilename(mode)


# seletor de cores

from tkinter import colorchooser
colorchooser = colorchooser.askcolor(initialcolor = '#FFFFFF')

print(colorchooser)