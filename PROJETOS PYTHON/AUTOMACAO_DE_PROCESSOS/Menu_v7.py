from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pandas as pd
from selenium import webdriver  # permite criar a janela
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from datetime import timedelta, date
from time import sleep
import time
import os


class Feedback:

    def __init__(self, master, opcao_mes):
        self.opcao_mes = opcao_mes
        master.title('Atualizações Diárias Tracking')
        master.resizable(False, False)
        self.messagebox = messagebox.showinfo('','Processo concluído')
        # primeiro frame
        self.Labelframe_seleciona_dist = ttk.LabelFrame(master)  # 1a janela filho
        self.Labelframe_seleciona_dist.config(relief=GROOVE, text='Distribuidora')
        self.Labelframe_seleciona_dist.pack(fill=BOTH, expand=True)

        # primeiro frame / configura os botões
        self.opcao_dist = StringVar()
        self.sel_dist_alhandra = ttk.Radiobutton(self.Labelframe_seleciona_dist)
        self.sel_dist_alhandra.config(text='Alhandra', variable=self.opcao_dist, value=1, command=self.sel_dist)
        self.sel_dist_alhandra.grid(row=1, column=0, sticky='sw')

        self.sel_dist_Extrema = ttk.Radiobutton(self.Labelframe_seleciona_dist)
        self.sel_dist_Extrema.config(text='Extrema', variable=self.opcao_dist, value=2, command=self.sel_dist)
        self.sel_dist_Extrema.grid(row=2, column=0, sticky='sw')

        # configura o segundo Labelframe
        self.Labelframe_atualiza = ttk.LabelFrame(master)  # 2a janela filho
        self.Labelframe_atualiza.config(relief=GROOVE, text='Processo')

        # configura os botões
        self.opcao_processo = StringVar()
        self.op1_exped = ttk.Radiobutton(self.Labelframe_atualiza)
        self.op1_exped.config(text='Expedição', variable=self.opcao_processo, value=1, command=self.sel_processo)
        self.op1_exped.grid(row=1, column=0, sticky='sw')

        self.op2_agend = ttk.Radiobutton(self.Labelframe_atualiza)
        self.op2_agend.config(text='Agendamento', variable=self.opcao_processo, value=2, command=self.sel_processo)
        self.op2_agend.grid(row=2, column=0, sticky='sw')

        self.op3_entrega = ttk.Radiobutton(self.Labelframe_atualiza)
        self.op3_entrega.config(text='Entrega', variable=self.opcao_processo, value=3, command=self.sel_processo)
        self.op3_entrega.grid(row=3, column=0, sticky='sw')
        self.op4_todos = ttk.Radiobutton(self.Labelframe_atualiza)
        self.op4_todos.config(text='Todos', variable=self.opcao_processo, value=0, command=self.sel_processo)
        self.op4_todos.grid(row=4, column=0, sticky='sw')
        self.op5_report = ttk.Radiobutton(self.Labelframe_atualiza)
        self.op5_report.config(text='Report', variable=self.opcao_processo, value=4, command=self.sel_processo)
        self.op5_report.grid(row=5, column=0, sticky='sw')

        self.opcao_mes = StringVar()

        self.combobox = ttk.Combobox(self.Labelframe_atualiza)
        self.combobox.config(textvariable=self.opcao_mes, values=['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'])
        self.combobox.grid(row=2, column=1, sticky='sw')
        self.combobox.bind('<<ComboboxSelected>>', self.selec_mes)  # 'self.selec_mes' é a função q está fora da classe
        self.combobox.state(['readonly', 'disabled'])
        self.Labelframe_atualiza.pack(fill=BOTH, expand=True)
        # configura o terceiro Labelframe
        self.Labelframe_report_comercial = ttk.LabelFrame(master)  # 3a janela filho
        self.Labelframe_report_comercial.config(relief=GROOVE, text='Report Comercial')

        ttk.Label(self.Labelframe_report_comercial, text='Região').grid(row=1, column=0, sticky='sw')
        ttk.Label(self.Labelframe_report_comercial, text='Vendedor').grid(row=2, column=0, sticky='sw')

        self.op_regiao = StringVar()
        self.regiao = ttk.Combobox(self.Labelframe_report_comercial)
        self.regiao.config(textvariable=self.op_regiao, values=(
            '01 NORTE', '02 NORDESTE', '03 LESTE', 'FARMA BRASIL', '05 SP/SUL ALIMENTAR DIRETO',
            '06 SP/SUL ALIMENTAR INDIRETO', '07 CENTRO-OESTE', '08 GNV  EDUARDO AZIZ'))
        self.regiao.grid(row=1, column=1, sticky='sw')
        self.regiao.bind('<<ComboboxSelected>>', self.selec_regiao)  # 'self.selec_mes' é a função q está fora da classe
        self.regiao.state(['readonly', 'disabled'])

        self.op_vend = StringVar()
        self.vendedor = ttk.Combobox(self.Labelframe_report_comercial)
        self.vendedor.config(textvariable=self.op_vend, values=('MARLEI', 'FLAVIO', 'GUALTER', 'LUCIA', 'JEANY', 'CLEBER', 'PAULO'))
        self.vendedor.grid(row=2, column=1, sticky='sw')
        self.vendedor.state(['readonly', 'disabled'])

        self.vendedor.bind('<<ComboboxSelected>>', self.seleciona_vendedor)
        self.Labelframe_report_comercial.pack(fill=BOTH, expand=True)

        # configura o quarto Labelframe

        self.Labelframe_executar = ttk.LabelFrame(master)  # 4a janela filho
        self.Labelframe_executar.config(relief=GROOVE)

        ttk.Button(self.Labelframe_executar, text='OK', command=self.executar).grid(row=1, column=0, sticky='sw')
        ttk.Button(self.Labelframe_executar, text='Fechar', command=self.fechar).grid(row=1, column=1, sticky='sw')
        ttk.Button(self.Labelframe_executar, text='TSI', command=self.tsi).grid(row=0, column=0, sticky='sw')

        self.progressbar = ttk.Progressbar(self.Labelframe_executar, orient='horizontal', mode='determinate', length=200)
        self.progressbar.grid(row=0, column=1, sticky='sw')

        self.Labelframe_executar.pack(fill=BOTH, expand=True)



    def sel_processo(self):
        a = self.opcao_processo.get()

        if a == '1':
            print(f'{a} - executar processo atualiza expedição')
            self.combobox.state(['disabled'])
        if a == '2':
            print(f'{a} - executar processo atualiza agenda')
            self.combobox.state(['!disabled'])
            self.regiao.state(['disabled'])
            self.vendedor.state(['disabled'])
        if a == '3':
            print(f'{a} - executar processo atualiza entrega')
            self.combobox.state(['disabled'])
            self.regiao.state(['disabled'])
            self.vendedor.state(['disabled'])
        if a == '0':
            print(f'{a} - executar processo atualizar todos')
            self.combobox.state(['!disabled'])
            self.regiao.state(['disabled'])
            self.vendedor.state(['disabled'])
        if a == '4':
            print(f'{a} - executar processo report')
            self.regiao.state(['!disabled'])
            self.vendedor.state(['!disabled'])

    def sel_dist(self):
        a = self.opcao_dist.get()

        return a

    def selec_mes(self, *args):
        a = self.opcao_mes.get()
        print(f'def selec_mes retorna: {a}')
        return a

    def selec_regiao(self, *args):
        a = self.op_regiao.get()
        print(a)

    def seleciona_vendedor(self, *args):
        a = self.op_vend.get()
        print(a)

    dist = sel_dist
    mes = selec_mes
    df = 0


    if dist == '1':
        print(f'{dist} - Alhandra Selecionada')
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\TRACKING NE-BS-2023.xlsx',
                           sheet_name='BASE TRACKING 2023')
    if dist == '2':
        print(f'{dist} - Extrema Selecionada')
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\Tracking BNE - 2023.xlsx',
                           sheet_name='BASE TRACKING 2023')

    # @staticmethod
    def navegador(self):
        servico = Service(ChromeDriverManager().install())
        navegador = webdriver.Chrome(service=servico)
        navegador.minimize_window()
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")

        return

    def executar(self):
        print('Executar')
        print('Classe: Intranet')

        processo = self.opcao_processo.get()

        print(f'Processo {processo}')

        dist = self.opcao_dist.get()
        mes = self.opcao_mes.get()

        print(f'Distribuidora {dist}.')
        print(f'Função Executar: Mês selecionado: {mes}')
        if processo == '1':
            Intranet.acessa_tela_atualizar_expedicao(self)
            self.messagebox


        if processo == '2':
            Intranet.atualiza_agenda(self)

        if processo == '3':
            Intranet.acessa_tela_atualizar_entrega(self)

        if processo =='0':
            print('Processo 1: Expedição')
            Intranet.acessa_tela_atualizar_expedicao(self)
            print('Processo 2: Agendamento')
            Intranet.atualiza_agenda(self)
            print('processo 3: Entrega')
            Intranet.acessa_tela_atualizar_entrega(self)
    def fechar(self):
        Intranet.navegador.close()
        print('Fechando Aplicação...')
        exit()


    def tsi(self):
        print('inicia progressbar')
        self.progressbar.start()

        if self.progressbar['value'] < 100:
            self.progressbar['value'] += 10
        navegador = self.navegador()
        print('Download TSI')

        data = date.today()

        Intranet.navegador.get('https://tsicliint.intecomlogistica.com.br/#/')

        print("Logging")
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[3]/label[1]')\
            .send_keys('jean.lino@baruel.com.br')
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[3]/label[2]')\
            .send_keys('151082')
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[4]/button[2]')\
            .send_keys(Keys.ENTER)
        sleep(2.0)
        print('Opções de Download')

        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/header/div/button').click()
        # sleep(2.0)
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div/a[5]/div[2]/div').click()
        sleep(2.0)

        Intranet.navegador.find_element('xpath', '//*[@id="tabelaFornecedores"]/div[1]/div[3]/div/button').send_keys(Keys.ENTER)
        #    sleep(2.0)

        print('Insere data Inicial')
        if data.day < 10 and data.month < 10:
            dta_final_formatada = f'0{data.day}/0{data.month}/{data.year}'  # ano  formato xx/xx/xxxx

        if data.day < 10 and data.month > 9:
            dta_final_formatada = f'0{data.day}/{data.month}/{data.year}'  # ano  formato xx/xx/xxxx

        if data.day > 9 and data.month < 10:
            dta_final_formatada = f'{data.day}/0{data.month}/{data.year}'  # ano  formato xx/xx/xxxx

        print('Insere data final')
        dta_inicial = data - timedelta(30)
        # print(f' Data Inicial = {dta_inicial}')
        if dta_inicial.day < 10 and dta_inicial.month < 10:
            dta_inicial_formatada = f'0{dta_inicial.day}/0{dta_inicial.month}/{dta_inicial.year}'
        elif dta_inicial.day < 10:
            dta_inicial_formatada = f'0{dta_inicial.day}/{dta_inicial.month}/{dta_inicial.year}'
        elif dta_inicial.month < 10:
            dta_inicial_formatada = f'{dta_inicial.day}/0{dta_inicial.month}/{dta_inicial.year}'

        else:
            dta_inicial_formatada = f'{dta_inicial.day}/{dta_inicial.month}/{dta_inicial.year}'
        # print(f' DAta Inicial Formatada = {dta_inicial_formatada}')
        sleep(15.0)
        Intranet.navegador.implicitly_wait(15.0)
        Intranet.navegador.find_element('xpath','/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/label/div/div/div[1]/input').send_keys(dta_inicial_formatada)

        sleep(3.0)
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/label').send_keys(dta_final_formatada)
        sleep(3.0)
        print('Seleciona filial')
        #
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/label').click()
        sleep(2.0)

        print(" Seleciona 'João Pessoa'")
        Intranet.navegador.find_element('xpath', '//*[@id="qvs_5"]/div[4]').send_keys(Keys.ENTER)
        sleep(3.0)

        print('Clica em filtrar')
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div[3]/button[2]').send_keys(Keys.ENTER)
        sleep(30.0)

        print('Baixar planilha')
        Intranet.navegador.find_element('xpath', '/html/body/div[1]/div/div/main/div[2]/div[1]/div[3]/div/div/button').send_keys(
            Keys.ENTER)
        sleep(10.0)

        data = date.today()
        hora = time.ctime()
        cont_copias = 1

        try:
            nome_arquivo = f'Relatorio_TSI_{data.year}_{data.month}_{data.day}.xls'

            print('Renomear o arquivo')
            os.rename('C:/Users/User/Downloads/rel_entregas.xls',
                      f'C:/Users/User/Downloads/relatorio/{nome_arquivo}')  # usar barras normais
            print(f'Arquivo renomeado para: {nome_arquivo}')
        except:

            nome_arquivo = f'Relatorio_TSI_{data.year}_{data.month}_{data.day}_{cont_copias}.xls'

            print('Renomear o arquivo')
            os.rename('C:/Users/User/Downloads/rel_entregas.xls',
                      f'C:/Users/User/Downloads/relatorio/{nome_arquivo}')  # usar barras normais
            print(f'Arquivo renomeado para: {nome_arquivo}')
            cont_copias+=1

        self.progressbar.stop()
        Intranet.navegador.close()
class Tracking():
    ano = 2023

    def importa_data_expedicao(self):
        print('Classe: Tracking, Método: importa_data_expedicao')
        Intranet.acessa_tela_tracking(self)  # importa a lista de nfs nao entregues
        a = Intranet.gera_lista_nfs_nao_expedidas(self)

        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\TRACKING NE-BS-2023.xlsx',
                           sheet_name='BASE TRACKING 2023')
        relatorio = df[["DOC", "EXPED"]]
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        data_exped_ini = pd.to_datetime(relatorio['EXPED'])  # puxa a data no formato yyyy-mm-dd
        data_exped = data_exped_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        doc = relatorio['DOC']  # puxa em float
        doc_int = doc.astype(int)  # transforma float em int
        doc = doc_int
        trk = zip(doc, data_exped)
        tracking = dict(trk).items()

        cont = 0
        dicionario = {}
        for p, d in tracking:
            if d != "":
                if p in a:
                    dicionario_temp = {p: d}  # transforma o set em dict
                    dicionario.update(dicionario_temp)  # copia o dicionario_temp dentro do dict definitivo
                    dicionario_temp.clear()  # limpa o dicionario temp
                    cont += 1

        print(dicionario)
        print(f'\n {cont} Datas de expedição  localizadas')

        return dicionario

    def importa_data_agenda(self):
        print('Classe: Tracking, Método: importa_data_agenda')

        a = Intranet.gera_lista_ped_sem_agenda(self)
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\Tracking BNE - 2023.xlsx',
                           sheet_name='BASE TRACKING 2023')
        relatorio = df[["PEDIDO", "DT.AGEND."]]  # considera todas as datas de agenda, inclusive as de nfs já entregues
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        print('-----------------------')
        print('<<<<<<Relatório>>>>>>>>')
        print(relatorio)
        print('-----------------------')
        print('* * * * * * Importa Data De Agenda * * * * * *')

        data_agenda_ini = pd.to_datetime(relatorio['DT.AGEND.'])  # puxa a data no formato yyyy-mm-dd
        data_agenda = data_agenda_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        pdd = relatorio['PEDIDO']  # puxa em float
        pedido_int = pdd.astype(int)  # transforma float em int

        pedido = pedido_int
        print('-----------------------')
        print('<<<<<<<<<trk>>>>>>>>>>>')
        trk = zip(pedido, data_agenda)

        print('-----------------------')
        tracking = dict(trk).items()

        cont = 0
        cont_teste = 0
        dicionario = {}

        for p, d in tracking:  # p = numero do pedido / d = data da agenda
            if type(d) != str:
                d = "0"
            # else:

            if p in a:
                p = str(p)
                if len(p) == 3:
                    p = f'000' + p
                if len(p) == 4:
                    p = f'00' + p
                if len(p) == 5:
                    p = f'0' + p
                print('-----------------------')
                print(p)
                print('-----------------------')
                dicionario_temp = {p: d}  # transforma o set em dict
                dicionario.update(dicionario_temp)  # copia o dicionario_temp dentro do dict definitivo
                dicionario_temp.clear()  # limpa o dicionario
                # temp
                cont += 1

        print(dicionario)  # mostra os pedidos e datas localizados na planilha
        if cont == 0:
            print(f'\n{cont} pedidos localizados')

        return dicionario

    def importa_data_entrega(self):
        print('Classe: Tracking, Método: importa_data_entrega')

        Intranet.acessa_tela_tracking(self)  # importa a lista de nfs nao entregues
        # print('Intranet.acessa_tela_tracking ')
        a = Intranet.gera_lista_nfs_nao_entregues(self)  # trf a lst em var
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\TRACKING NE-BS-2023.xlsx',
                           sheet_name='BASE TRACKING 2023')

        relatorio = df.loc[df["STATUS"] == "ENTREGUE", ["STATUS", "DOC", "DTA ENTREGA"]]
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        data_entrega_ini = pd.to_datetime(relatorio['DTA ENTREGA'])  # puxa a data no formato yyyy-mm-dd
        # print(f' Data_entrega_ini > {data_entrega_ini}')
        data_entrega = data_entrega_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        # print(f'  data_entrega > { data_entrega}')
        doc = relatorio['DOC']  # puxa em float
        doc_int = doc.astype(int)  # transforma float em int
        doc = doc_int
        trk = zip(doc, data_entrega)
        tracking = dict(trk).items()

        cont = 0
        dicionario = {}
        for p, d in tracking:
            if d != '':
                if p in a:
                    dicionario_temp = {p: d}  # transforma o set em dict
                    dicionario.update(dicionario_temp)  # copia o dicionario_temp dentro do dict definitivo
                    dicionario_temp.clear()  # limpa o dicionario temp
                    cont += 1

        print(dicionario)
        print(f'\n {cont} Datas de entrega localizadas')
        return dicionario

class Intranet(Feedback,object):

    # print('Classe: Intranet')

    servico = Service(ChromeDriverManager().install())
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    navegador = webdriver.Chrome(service=servico)
    navegador.minimize_window()


    def acessa_intranet(self):
        print('Classe: Intranet, Método: acessa_Intranet')
        Intranet.navegador.get('http://45.236.77.106:51236/intranet/login.php')

        # fazer  login
        Intranet.navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').clear()

        Intranet.navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys(
            'jean.lino')
        Intranet.navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
            'Ma250509')
        Intranet.navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
            Keys.ENTER)

    def acessa_tela_pedidos_otc(self):
        Intranet.navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys('L')
        Intranet.navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys(Keys.ENTER)
        print('acessa logística')
        # acessar 'Logística'
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[2]/a').click()
        print('acessa pedidos otc')
        # acessar pedidos otc
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[2]/ul/a[2]').click()

        if Feedback.dist == 2:  # extrema
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.dist == 1:  # Alhandra
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)

    def acessa_tela_tracking(self):
        print('Classe: Intranet, Método: acessa_tela_tracking')
        Intranet.acessa_intranet(self)

        # acessar 'Customer Services'
        print('Acessa Customer Services')
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/a').click()
        # acessar Tracking
        print('Acessa Distribuidor')
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/ul/a[1]').click()
        # 1 > Extrema 2 > Alhandra

        if Feedback.dist == '1':
            print('Acessa Alhandra')
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)

        if Feedback.dist == '2':
            print('Acessa Extrema')
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)

    def gera_lista_nfs_nao_expedidas(self):
        print('Classe: Intranet, Método: gera_lista_nfs_nao_expedidas')
        Intranet.navegador.find_element('xpath',
                                                 '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()  # FILTRA NFS NAO expedidas
        Intranet.navegador.find_element('xpath',
                                                 '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[2]').click()  # opção nao expedidos
        data = date.today()
        dta_inicial = data - timedelta(60)

        dia_ini_formatado = ''
        mes_ini_formatado = ''
        if dta_inicial.day < 10:
            dia_ini_formatado = f'0{dta_inicial.day}'
        else:
            dia_ini_formatado = dta_inicial.day

        if dta_inicial.month < 10:
            mes_ini_formatado = f'0{dta_inicial.month}'
        else:
            mes_ini_formatado = dta_inicial.month

        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(Keys.CLEAR)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(dia_ini_formatado)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(mes_ini_formatado)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(dta_inicial.year)
        Intranet.navegador.find_element('xpath',
                                                 '/html/body/form[2]/table[3]/tbody/tr/td[1]/input').send_keys(
            Keys.ENTER)
        # procurar linha a linha os numeros das NFS entregue no tracking e preencher, caso seja localizada
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[5]/tbody/tr[2]/td[8]')
        nfs_nao_expedidas = []
        tr = 2
        try:
            while True:
                # campo NF da linha   >>> td[8]
                linha = Intranet.navegador.find_element('xpath',
                                                                 f'/html/body/form[2]/table[5]/tbody/tr[{tr}]/td[8]')  # busca o elemento NF a partir da linha 2
                col_nf = linha.text  # recebe a varivel linha como texto
                nf = col_nf
                nf = int(nf)  # transforma em inteiro
                # print(nf)
                tr += 1
                nfs_nao_expedidas.append(nf)  # insere na lista
        #
        except:
            print(f"{tr - 2} NF'S nao expedidas")
            print(f'Lista > {nfs_nao_expedidas}')
        return nfs_nao_expedidas

    def acessa_tela_atualizar_expedicao(self):
        print('Classe: Intranet, Método: acessa_tela_atualizar_expedicao')
        tracking = Tracking.importa_data_expedicao(self)
        # # acessar 'Customer Services'
        Intranet.navegador.find_element('xpath',
                                                 '//*[@id="navigation"]/ul/li[4]/a').click()  # clica em customer services
        Intranet.navegador.find_element('xpath',
                                                 '//*[@id="navigation"]/ul/li[4]/ul/a[5]').click()  # clica em expedição/entrega
        if Feedback.dist == '1':  # seleciona a dist bs-alhandra
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
        if Feedback.dist == '2':  # seleciona a dist bs-extrema
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[2]/tbody/tr/td/input').click()  # clica em 'processa'
            # ACESSA TELA DE EXPEDIÇÃO

        Intranet.navegador.find_element('xpath',
                                                 '/html/body/form[2]/table[1]/tbody/tr[2]/td[9]/a').click()  # clica no botão 'expedição'

        if Feedback.dist == '2':  # número de série da NF
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '3')

        if Feedback.dist == '1':
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '4')
        # importa lista com as nfs/dtas entrega que deverão ser lançadas
        c = 1
        cont_nfs_expedidas = 0
        for nf, data in tracking.items():
            # critica = navegador.find_element('xpath', '/html/body/form[2]/div[2]/text()') >  esta linha está com erro. o objetivo é mostrar a critica
            # caso já exista data  lan  çada, ou se a data de entrega é menor do que a data  de expedição.
            print(f'{c} - {nf}: {data} ')

            data = data.replace("/", "")
            c += 1

            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/input').send_keys(
                nf)

            # data de expedicao
            Intranet.navegador.find_element('xpath', '//*[@id="calendario1"]').send_keys(data)

            #  grava
            Intranet.navegador.find_element('xpath',
                                                     '/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/input').send_keys(
                Keys.ENTER)
            cont_nfs_expedidas += 1

        print(f'{cont_nfs_expedidas} datas lançadas')

    def gera_lista_ped_sem_agenda(self):
        print('Classe: Intranet - Metodo: Gera_lista_ped_sem_agenda')
        lista_area = ['01_NORTE', '02_NORDESTE', '03_LESTE', '04_FARMA', '05_ALIM_DIRETO', '06_ALIM_INDIRETO',
                      '07_CENTRO-OESTE', '08_GNV-EDUARDO_AZIZ']
        lst_area = ['1', '01', '2', '02', '3', '03', '4', '04', '5', '05', '6', '06', '7', '07', '8', '08', '9',
                    '09']
        if Feedback.dist == 2:
            print(lista_area)

            area = input('AREA (Pressione "ENTER" Para Todas): ')
        #opcao_mes
        # mes = F   eedback.selec_mes
        mes = Feedback.selec_mes(self)

        print(f'Mês selecionado: {mes}')
        # mes = str(input("Mês (mmm): "))
        print('Intranet.acessa_intranet')
        Intranet.acessa_intranet(self)
        print('Intranet.acessa_tela_pedidos_otc')
        Intranet.acessa_tela_pedidos_otc(self)
        print('seleciona mês')
        # seleciona mês
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[3]/select').send_keys(f'{mes}')
        print(f'Mês de pesquisa: {mes}')

        # seleciona a tela de agendamento
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').send_keys('agendamento')
        # SELECIONA REGIONAL
        area = 0
        if Feedback.dist == 1 and area in lst_area:
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(f'{area}')
        # processa
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr/td/input').click()
        tr = 1
        pedidos_sem_agenda = []

        try:
            while True:
                linha = Intranet.navegador.find_element('xpath',
                                                                 f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[2]')  # busca o elemento NF a partir da linha 2
                col_pedido = linha.text  # recebe a varivel linha como texto
                pedido = col_pedido
                pedido = int(pedido)
                tr += 1
                pedidos_sem_agenda.append(pedido)
        except:
            print(f'{tr - 2} Pedidos Sem Data de Agendamento')
            print(f'Lista: {pedidos_sem_agenda}')

        return pedidos_sem_agenda

    def atualiza_agenda(self):
        print('Feedback.Tracking.atualiza_data_agenda')
        tracking = Tracking.importa_data_agenda(self)
        print(tracking)
        print('----------------------------------')
        ano = 2023
        cont_tr = 1
        c = 0
        cont_agenda_incluida = 0
        if len(tracking) == 0:
            pass
        else:
            try:
                while True:
                    for i in tracking:
                        # i = str(i)

                        print(f'Analisando linha {cont_tr} | pedido {i}')
                        nome = Intranet.navegador.find_element('xpath',
                                                                        f'/html/body/form[2]/table[3]/tbody/tr[{cont_tr}]/td[1]/input').get_dom_attribute(
                            'name')
                        print(nome)
                        if nome == f'marcacao_agenda[{i}]':
                            print(f'> Pedido {i} - agendado para {tracking[i]}')
                            Intranet.navegador.find_element('xpath',
                                                                     f'/html/body/form[2]/table[3]/tbody/tr[{cont_tr}]/td[1]/input').send_keys(
                                tracking[i])  # ok
                            cont_agenda_incluida += 1
                    c += 1
                    cont_tr += 1
            except:
                print('Verificar erro')

            finally:
                print(f'{cont_tr} pedidos verificados.\n'
                      f'{cont_agenda_incluida} agendas incluídas. ')
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/div[2]/input').click()

    def acessa_tela_atualizar_entrega(self):
        print('Classe: Intranet, Método: acessa_tela_atualizar_entrega')
        tracking = Tracking.importa_data_entrega(self)

        # # acessar 'Customer Services'

        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/a').click()
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/ul/a[5]').click()
        # ACESSAR BS DISTRIBUIDORA (bne: arrow up, bs-alhandra: arrow down  bs: arrow down 2x)
        if Feedback.dist == 1:  # bs-alhandra
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
        if Feedback.dist == 2:  # bs-extrema
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[2]/tbody/tr/td/input').click()
        # ACESSA A TELA 'ENTREGA'
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[10]/a').click()
        # número de série da NF
        if Feedback.dist == 1:
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('3')
        if Feedback.dist == 2:
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('4')
        # importa lista com as nfs/dtas entrega que deverão ser lançadas
        c = 1
        cont_nfs_entregues = 0
        for nf, data in tracking.items():
            print(f'{c} - {nf}: {data} ')
            data = data.replace("/", "")
            c += 1
            # INSERIR UMA LINHA PARA CASO JÁ HAJA DATA DE ENTREGA LANÇADA, NÃO SOMAR NO TOTAL
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/input').send_keys(nf)
            # data de entrega
            Intranet.navegador.find_element('xpath', '//*[@id="calendario1"]').send_keys(data)

            #  grava
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/input').send_keys(Keys.ENTER)
            cont_nfs_entregues += 1

        print(f'{cont_nfs_entregues} datas lançadas')

    def gera_lista_nfs_nao_entregues(self):
        print('Classe: Intranet, Método: gera_lista_nfs_nao_entregues')
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[3]').click()
        # verificar como as opções otc/filtro /agendamento

        data = date.today()
        dta_inicial = data - timedelta(60)

        dia_ini_formatado = ''
        mes_ini_formatado = ''
        if dta_inicial.day < 10:
            dia_ini_formatado = f'0{dta_inicial.day}'
        else:
            dia_ini_formatado = dta_inicial.day

        if dta_inicial.month < 10:
            mes_ini_formatado = f'0{dta_inicial.month}'
        else:
            mes_ini_formatado = dta_inicial.month


        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(Keys.CLEAR)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(dia_ini_formatado)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(mes_ini_formatado)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(dta_inicial.year)

        Intranet.navegador.find_element('xpath',
                                                 '/html/body/form[2]/table[3]/tbody/tr/td[1]/input').send_keys(
            Keys.ENTER)

        # procurar linha a linha os numeros das NFS entregue no tracking e preencher, caso seja localizada
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[5]/tbody/tr[2]/td[8]')
        nfs_nao_entregues = []
        tr = 2
        try:
            while True:
                # campo NF da linha   >>> td[8]
                linha = Intranet.navegador.find_element('xpath',
                                                                 f'/html/body/form[2]/table[5]/tbody/tr[{tr}]/td[8]')  # busca o elemento NF a partir da linha 2
                col_nf = linha.text  # recebe a varivel linha como texto
                nf = col_nf
                nf = int(nf)  # transforma em inteiro
                # print(nf)
                tr += 1
                nfs_nao_entregues.append(nf)  # insere na lista
        #
        except:
            print(f"{tr - 2} NF'S nao entregues")
            print(f'Lista > {nfs_nao_entregues}')
        return nfs_nao_entregues
    
    
    def atualiza_entrega(self):
        print('Classe: Intranet, Método: atualiza_entrega')
    
        # listar nfs nao entregues
        print('Feedback.Intranet.gera_lista_nfs_nao_entregues(self)')
        Intranet.gera_lista_nfs_nao_entregues(self)  # FUNCIONANDO
    
        # buscar datas de entrega na planilha
        # retornar dicionario
        print('Tracking.importa_data_entrega(self)')
        Tracking.importa_data_entrega(self)  # funcionando


def main():
    root = Tk()
    root.config(border=(20))

    feedback = Feedback(root, opcao_mes=StringVar())
    root.mainloop()


if __name__ == '__main__': main()
