from tkinter import *
from tkinter import ttk
class Feedback:  #

    def __init__(self, master):
        master.title('Atualizações Diárias Tracking')
        master.resizable(False, False)
        # primeiro frame
        #configura o primeiro frame
        self.Labelframe_seleciona_dist = ttk.LabelFrame(master) # 1a janela filho
        self.Labelframe_seleciona_dist.config(relief=GROOVE, text='Distribuidora')
        # configura o label
        #configura os botões
        self.opcao_dist = StringVar()
        self.sel_dist_alhandra = ttk.Radiobutton(self.Labelframe_seleciona_dist,text='Alhandra', variable=self.opcao_dist, value=1, command=self.sel_dist).grid(row=1, column=0,sticky='sw'  )
        self.sel_dist_Extrema = ttk.Radiobutton(self.Labelframe_seleciona_dist, text='Extrema', variable=self.opcao_dist, value=2, command=self.sel_dist).grid(row=2, column=0, sticky='sw')
        self.Labelframe_seleciona_dist.pack(fill=BOTH, expand=True)
        # configura o quarto Labelframe
        self.Labelframe_executar = ttk.LabelFrame(master) # 4a janela filho
        self.Labelframe_executar.config(relief=GROOVE)
        ttk.Button(self.Labelframe_executar, text = 'OK',command=self.executar).grid(row=0,column=0,sticky='sw')
        self.Labelframe_executar.pack(fill=BOTH, expand=True)
    def sel_dist(self):
        a = self.opcao_dist.get()
        if a == '1':
            print(f'{a} - Alhandra Selecionada')
        if a == '2':
            print(f'{a} - Extrema Selecionada')   #


    def executar(self):
        print('---------------------------------')
        print('Executar')
        dist = self.opcao_dist.get()
        print(f'Distribuidora {dist}.')
        Feedback.Action.Intranet(self)
        Feedback.Action.Tracking(self)

    class Action:
        def Intranet(self):
            print('Proc Intranet Executado')

        def Tracking(self):
            print('Proc Tracking Executado')

def main():
    root = Tk()
    root.config(border=(20))
    feedback = Feedback(root)

    root.mainloop()
if __name__=='__main__': main()
