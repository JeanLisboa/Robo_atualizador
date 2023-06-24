from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Feedback:  #

    def __init__(self, master):
        master.title('Atualizações Diárias Tracking')
        master.resizable(False, False)
        # primeiro frame
        #configura o primeiro frame
        self.Labelframe_seleciona_dist = ttk.LabelFrame(master) # 1a janela filho
        self.Labelframe_seleciona_dist.config(relief=GROOVE, text='distibuidora')

        #border   #padding

        # configura o label
        #configura os botões

        self.opcao_dist = StringVar()
        self.sel_dist_alhandra = ttk.Radiobutton(self.Labelframe_seleciona_dist,text='Alhandra', variable=self.opcao_dist, value=1, command=self.sel_dist).grid(row=1, column=0,sticky='sw'  )
        self.sel_dist_Extrema = ttk.Radiobutton(self.Labelframe_seleciona_dist, text='Extrema', variable=self.opcao_dist, value=2, command=self.sel_dist).grid(row=2, column=0, sticky='sw')
        self.Labelframe_seleciona_dist.pack(fill=BOTH, expand=True)



        #configura o segundo Labelframe
        self.Labelframe_atualiza = ttk.LabelFrame(master) # 2a janela filho
        self.Labelframe_atualiza.config(relief=GROOVE, text='Atualizações')



        #configura os botões
        self.opcao_processo = StringVar()
        self.op1_exped = ttk.Radiobutton(self.Labelframe_atualiza,text='Expedição', variable=self.opcao_processo, value=1, command=self.sel_processo).grid(row=1, column=0 ,sticky='sw')
        self.op2_agend = ttk.Radiobutton(self.Labelframe_atualiza,text='Agendamento', variable=self.opcao_processo, value=2, command=self.sel_processo).grid(row=2, column=0 ,sticky='sw')
        self.op3_entrega = ttk.Radiobutton(self.Labelframe_atualiza,text='entrega', variable=self.opcao_processo, value=3, command=self.sel_processo).grid(row=3, column=0 ,sticky='sw')
        self.op4_todos = ttk.Radiobutton(self.Labelframe_atualiza,text='Todos', variable=self.opcao_processo, value=0, command=self.sel_processo).grid(row=4, column=0,sticky='sw')

        self.opcao_mes = StringVar()
        self.combobox = ttk.Combobox(self.Labelframe_atualiza)
        self.combobox.config(textvariable=self.opcao_mes,values=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'])
        self.combobox.grid(row=2, column=1,sticky='sw')
        self.combobox.bind('<<ComboboxSelected>>',self.selec_mes) # 'self.selec_mes' é a função q está fora da classe
        self.combobox.state(['readonly'])
        self.Labelframe_atualiza.pack(fill=BOTH, expand=True)


        #configura o terceiro Labelframe
        self.Labelframe_report_comercial = ttk.LabelFrame(master) # 3a janela filho
        self.Labelframe_report_comercial.config(relief=GROOVE,text='Report Comercial')


        ttk.Label(self.Labelframe_report_comercial, text='Região').grid(row=1, column=0,sticky='sw')
        ttk.Label(self.Labelframe_report_comercial, text='Vendedor').grid(row=2, column=0,sticky='sw')

        self.op_regiao =StringVar()
        self.regiao =ttk.Combobox(self.Labelframe_report_comercial)
        self.regiao.config(textvariable=self.op_regiao,values=('01 NORTE', '02 NORDESTE', '03 LESTE' , 'FARMA BRASIL', '05 SP/SUL ALIMENTAR DIRETO', '06 SP/SUL ALIMENTAR INDIRETO', '07 CENTRO-OESTE', '08 GNV  EDUARDO AZIZ'))
        self.regiao.grid(row=1, column=1,sticky='sw')
        self.regiao.bind('<<ComboboxSelected>>',self.selec_regiao) # 'self.selec_mes' é a função q está fora da classe
        self.regiao.state(['readonly'])



        self.op_vend = StringVar()
        self.vendedor = ttk.Combobox (self.Labelframe_report_comercial)
        self.vendedor.config(textvariable=self.op_vend,values=('MARLEI','FLAVIO','GUALTER','LUCIA','JEANY','CLEBER','PAULO'))
        self.vendedor.grid(row=2, column=1,sticky='sw')
        self.vendedor.bind('<<ComboboxSelected>>',self.seleciona_vendedor)
        self.Labelframe_report_comercial.pack(fill=BOTH, expand=True)

        # configura o quarto Labelframe

        self.Labelframe_executar = ttk.LabelFrame(master) # 4a janela filho
        self.Labelframe_executar.config(relief=GROOVE)

        ttk.Button(self.Labelframe_executar, text = 'OK',command=self.executar).grid(row=0,column=0,sticky='sw')
        ttk.Button(self.Labelframe_executar, text = 'Limpar',command=self.limpar).grid(row=0,column=1,sticky='sw')
        ttk.Button(self.Labelframe_executar, text = 'Fechar',command=self.fechar).grid(row=0,column=2,sticky='sw')

        self.Labelframe_executar.pack(fill=BOTH, expand=True)


    def sel_processo(self):
        a = self.opcao_processo.get()
        print(a)
        if a == '1':
            print('executar processo atualiza expedição')
        if a == '2':
            print('executar processo atualiza agenda')
        if a == '3':
            print('executar processo atualiza entrega')
        if a == '0':
            print('executar processo atualizar todos')
    def sel_dist(self):
        a = self.opcao_dist.get()
        print(a)
        if a == '1':
            print('Alhandra Selecionada')

        if a == '2':
            print('Extrema Selecionada')

    def selec_mes(self, *args):
        a = self.opcao_mes.get()
        print(a)

    def selec_regiao(self,*args):
        a = self.op_regiao.get()
        print(a)

    def seleciona_vendedor(self,*args):
        a = self.op_vend.get()
        print(a)
    def executar(self):
        print('eXecutar')
    def limpar(self):
        print('limpar')

    def fechar(self):
        print('fechar')
def main():
    root = Tk()
    root.config(border=(20))


    feedback = Feedback(root)
    root.mainloop()


if __name__=='__main__': main()