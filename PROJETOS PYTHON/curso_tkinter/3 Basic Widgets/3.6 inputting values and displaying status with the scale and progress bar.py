from tkinter import *
from tkinter import ttk
#ttk é um método construtor
root = Tk()
progressbar = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar.pack()
progressbar.config(mode='indeterminate')
# este tipo pode ser usado quando nao se sabe quando finalizará o processo
progressbar.start()
# progressbar.stop() #ao final do processo
progressbar2 = ttk.Progressbar(root, orient=HORIZONTAL, length=200)
progressbar2.pack()
progressbar2.config(mode='determinate', maximum=11.0, value=2)
# progressbar2.config(value=8) #altera o value inicial
progressbar2.step(4)
value = DoubleVar()
progressbar2.config(variable=value)
scale = ttk.Scale (root, orient=HORIZONTAL, length=400, variable=value, from_=0.0, to=11.0)
scale.pack()
root.mainloop()


