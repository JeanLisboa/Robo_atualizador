import os
import time
from datetime import timedelta, date
from time import sleep
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
import pywhatkit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from informacoes import pwd


class Feedback:
    print('Class Feedback')

    def __init__(self, master, opcao_mes, opcao_regional, teste_arquivo):
        self.opcao_mes = opcao_mes
        self.opcao_regional = opcao_regional
        self.teste_arquivo = teste_arquivo
        master.title('Atualizações Diárias Tracking')
        master.resizable(False, False)

        # photo = PhotoImage(file="logol.png")
        # master.iconphoto(False, photo)

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

        # seleciona arquivo
        self.arquivo = StringVar()
        self.sel_arquivo = ttk.Button(self.Labelframe_seleciona_dist, text='Selecionar arquivo', command=self.abrir_arquivo).grid(row=2, column=1, sticky='sw')


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

        self.opcao_regional = StringVar()
        self.opcao_mes = StringVar()
        self.teste_arquivo = StringVar()

        self.combobox = ttk.Combobox(self.Labelframe_atualiza)
        self.combobox.config(textvariable=self.opcao_mes,
                             values=['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov',
                                     'dez'])
        self.combobox.grid(row=2, column=1, sticky='sw')
        self.combobox.bind('<<ComboboxSelected>>', self.selec_mes)  # 'self.selec_mes' é a função q está fora da classe
        # --------------------------
        self.combobox2 = ttk.Combobox(self.Labelframe_atualiza)
        self.combobox2.config(textvariable=self.opcao_regional,
                             values=['TODAS','1 - NORTE', '2 - NORDESTE', '3 - LESTE', '4 - FARMA', '5 - ALIM DIRETO', '6 - ALIM INDIRETO', '7 - CENTRO-OESTE'])
        self.combobox2.grid(row=2, column=2, sticky='sw')
        self.combobox2.bind('<<ComboboxSelected>>', self.selec_regional)  # 'self.selec_mes' é a função q está fora da classe

        # self.combobox.state(['readonly', 'disabled'])
        self.combobox.state(['readonly'])
        self.combobox2.state(['readonly'])
        # ----------------------------------
        self.Labelframe_atualiza.pack(fill=BOTH, expand=True)

        # configura o terceiro Labelframe
        self.Labelframe_report_comercial = ttk.LabelFrame(master)  # 3a janela filho
        self.Labelframe_report_comercial.config(relief=GROOVE, text='Report Comercial')

        ttk.Label(self.Labelframe_report_comercial, text='Região').grid(row=1, column=0, sticky='sw')
        ttk.Label(self.Labelframe_report_comercial, text='Vendedor').grid(row=2, column=0, sticky='sw')

        self.op_regiao = StringVar()
        self.regiao = ttk.Combobox(self.Labelframe_report_comercial)
        self.regiao.config(textvariable=self.op_regiao, values=('02 NORDESTE'))
        self.regiao.grid(row=1, column=1, sticky='sw')
        self.regiao.bind('<<ComboboxSelected>>', self.selec_regional)  # 'self.selec_mes' é a função q está fora da classe
        self.regiao.state(['readonly', 'disabled'])

        self.op_vend = StringVar()
        self.vendedor = ttk.Combobox(self.Labelframe_report_comercial)
        self.vendedor.config(textvariable=self.op_vend, values=(
            'TODOS', '000669 FLAVIO SILVA', '000671 MARLEI', '000508 JEANY', '000595 GUALTER', '000656 FLAVIO',
            '000641 LUCIA', '000502 CLEBER', '000654 PAULO BESERRA','000686 LUANA'))
        self.vendedor.grid(row=2, column=1, sticky='sw')
        self.vendedor.state(['readonly', 'disabled'])

        self.vendedor.bind('<<ComboboxSelected>>', self.seleciona_vendedor)
        self.Labelframe_report_comercial.pack(fill=BOTH, expand=True)

        # configura o quarto Labelframe

        self.Labelframe_executar = ttk.LabelFrame(master)  # 4a janela filho
        self.Labelframe_executar.config(relief=GROOVE)

        ttk.Button(self.Labelframe_executar, text='OK', command=self.executar).grid(row=0, column=1, sticky='sw')
        ttk.Button(self.Labelframe_executar, text='Fechar', command=self.fechar).grid(row=0, column=2, sticky='sw')
        ttk.Button(self.Labelframe_executar, text='TSI', command=self.tsi).grid(row=0, column=0, sticky='sw')

        self.Labelframe_executar.pack(fill=BOTH, expand=True)

    def sel_processo(self):
        print('Class: Feedback, Método: sel_processo.')
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
            self.combobox.state(['disabled'])

    def sel_dist(self):
        print('class: Feedback, método: sel_dist')
        a = self.opcao_dist.get()

        return a

    def selec_mes(self, *args):
        print('class: Feedback, método: sel_mes')
        a = self.opcao_mes.get()
        print(f'def selec_mes retorna: {a}')
        return a

    def selec_regional(self, *args):
        print('class: Feedback, método: selec_regiao')
        a = self.opcao_regional.get()
        print(f'Regional {a} Selecionada')

    def seleciona_vendedor(self, *args):
        print('class: Feedback, método: seleciona_vendedor')
        a = self.op_vend.get()
        print(a)

    def report_comercial(self):
        print('class: Feedback, método: report_comercial')
        """Report_comercial

        Esta função utiliza o PyautuGUI e  envia as informações da
        coluna 'Observação' via WhatsApp
        """
        a = self.op_vend.get()
        print(a)
        cod_vend = ''
        msg_vend = ''
        contato = ''
        if a == 'TODOS':
            pass

        if a == '000671 MARLEI':
            cod_vend = '000671 MARLEI'
            msg_vend = str('Bom dia Marlei, tudo bem ?')
            contato = '+5581994447916'  # marlei 81994447916 >> luana   5571981075723

        if a == '000686 LUANA':
            cod_vend = '000686 LUANA'
            msg_vend = str('Bom dia Luana, tudo bem ?')
            contato = '+5571981075723'

        if a == '000669 FLAVIO SILVA':
            cod_vend = '000669 FLAVIO SILVA'
            msg_vend = str('Bom dia Flávio, tudo bem ?')
            contato = '+5531984034352'

        if a == '000508 JEANY':
            cod_vend = '000508 JEANY'
            msg_vend = str('Bom dia Jeany, tudo bem ?')
            contato = '+5584999811102'  # +5584999811102
        if a == '000595 GUALTER':
            cod_vend = '000595 GUALTER'
            msg_vend = str('Bom dia Gualter, tudo bem ?')
            contato = '+5582988110209'
        if a == '000656 FLAVIO':
            cod_vend = '000656 FLAVIO'
            msg_vend = str('Bom dia Flávio, tudo bem ?')
            contato = '+5585991239734'
        if a == '000641 LUCIA':
            cod_vend = '000641 LUCIA'
            msg_vend = str('Bom dia Vanessa, tudo bem ?')
            contato = '+5583998072021'
        if a == '000502 CLEBER':
            cod_vend = '000502 CLEBER'
            msg_vend = str('Bom dia Cléber, tudo bem ?')
            contato = '+5587996265806'
        if a == '000654 PAULO BESERRA':
            cod_vend = '000654 PAULO BESERRA'
            msg_vend = str('Bom dia Paulo, tudo bem ?')
            contato = '+5586999773176'  #'+5586999773176'

        print(f' Cod vend: {cod_vend}')
        print(f'Contato: {contato}')
        print(f'Msg vend: {msg_vend}')

        df = pd.read_excel('C:/Users/User/OneDrive - Baruel/CUSTOMER SERVICE/CUSTOMER SERVICE/AREA 02 NE/Tracking BNE - 2023.xlsx', sheet_name='BASE TRACKING 2023')
        if self.dist == '2':
            df = pd.read_excel(self.abrir_arquivo, sheet_name='TRACKING 2023')  # luana Norte

        relatorio = df.loc[
            (df['STATUS'] != 'ENTREGUE') & (df['STATUS'] != 'DEVOLUÇÃO'), ["VEND", "DOC", "CLIENTE", "DESTINATÁRIO",
                                                                           "MUNICIPIO", "VOLUME", "Agend",
                                                                           "PREVISÃO ENTREGA", "OBS"]]

        relatorio2 = relatorio.loc[relatorio['VEND'] == cod_vend, ["VEND", "DOC", "DESTINATÁRIO", "OBS"]]

        rel3 = relatorio2[["DOC", "DESTINATÁRIO", "OBS"]]
        rel3 = rel3.dropna(axis=0)  # exclui as colunas com valores vazios
        doc = rel3['DOC'].tolist()

        lst_doc = []
        for a in doc:
            a = int(a)
        lst_doc.append(a)
        doc = lst_doc
        dest = rel3['DESTINATÁRIO'].tolist()
        obs = rel3['OBS'].tolist()
        trk = zip(dest, obs)

        trk2 = zip(doc, trk)
        tracking = dict(trk).values()
        print(len(doc))
        if len(doc) == 0:
            messagebox.showinfo('', 'Não há Entregas pendentes para este vendedor')
        else:
            pywhatkit.sendwhatmsg_instantly(phone_no=contato, wait_time=10, tab_close=True, close_time=3,
                                            message=f'{msg_vend}\n Seguem informações: \n')
            for a in range(len(doc)):
                pywhatkit.sendwhatmsg_instantly(phone_no=contato, wait_time=10, tab_close=True, close_time=3,
                                                message=f"{doc[a]} | {dest[a]} | {obs[a]}")
                print(f"{doc[a]} | {dest[a]} | {obs[a]}")
            messagebox.showinfo('', 'Report Concluído')
    dist = sel_dist
    mes = selec_mes
    df = 0

    @staticmethod
    def navegador(self):
        print('class: Feedback, método: navegador')
        options = Options()
        navegador = webdriver.Chrome(options=options)
        # navegador.minimize_window()
        # options.add_argument("--headless=new")
        return

    def dataframe(self):
        print('class: Feedback, método: dataframe')

        if self.dist == '1':
            print(f'{self.dist} - Alhandra Selecionada')
            print(self.df)
        if self.dist == '2':
            print(f'{self.dist} - Extrema Selecionada')
            # self.df = pd.read_excel(self.abrir_arquivo, sheet_name='BASE TRACKING 2023')
        return self.df

    sel_arquivo = ''

    def abrir_arquivo(self):
        global teste_arquivo
        print('class: Feedback, método: abrir_arquivo')
        filetypes = (('excel files', '*.xlsx'), ('All files', '*.*'))
        sel_arquivo = fd.askopenfile(title='Selecione o Tracking', initialdir='C:/Users/User/Baruel/Baruel - CUSTOMER SERVICE', filetypes=filetypes)
        ttk.Label(self.Labelframe_seleciona_dist, text=sel_arquivo.name).grid(row=3, column=1, sticky='sw')
        print(f'arquivo selecionado: {sel_arquivo.name}')
        # print(f'arquivo tipo {type(sel_arquivo.name)}')
        teste_arquivo = str(sel_arquivo.name)
        teste_arquivo = teste_arquivo.replace('/', '\\')
        teste_arquivo = f'{teste_arquivo}'
        # print(teste_arquivo)

        return teste_arquivo
    print()

    def sel_arquivo(self):
        self.abrir_arquivo = StringVar()
        print('class: Feedback, método: sel_arquivo')
        a = self.arquivo.get()
        return a

    arquivo = sel_arquivo

    def executar(self):
        print('class: Feedback, método: executar')
        processo = self.opcao_processo.get()
        print(f'Processo {processo}')
        mes = self.opcao_mes.get()
        regional = self.opcao_regional.get()
        print(f'Regional {regional}')

        print(f'Função Executar: Mês selecionado: {mes}')
        if processo == '1':
            Intranet.acessa_tela_atualizar_expedicao(self)
            messagebox.showinfo('Processo Concluído', 'Datas de Expediçao Atualizadas')
        if processo == '2':
            Intranet.atualiza_agenda(self)
            messagebox.showinfo('Processo Concluído', f'Datas de Agendamento Atualizadas')
        if processo == '3':
            Intranet.acessa_tela_atualizar_entrega(self)
            messagebox.showinfo('Processo Concluído', f'Datas de Entrega Atualizadas')
        if processo == '0':
            print('Processo 1: Expedição')
            Intranet.acessa_tela_atualizar_expedicao(self)
            print('Processo 2: Agendamento')
            Intranet.atualiza_agenda(self)
            print('processo 3: Entrega')
            Intranet.acessa_tela_atualizar_entrega(self)
            messagebox.showinfo('Processo Concluído', 'Datas de Expedição, Agendamento\n'
                                                      'e Entrega Atualizadas')

        if processo == '4':
            self.report_comercial()

    @staticmethod
    def fechar():
        print('class: Feedback, método: fechar')
        Intranet.navegador.close()
        print('Encerrando Aplicação...')
        exit()


    def tsi(self):
        # navegador = self.navegador()
        print('class: Feedback, método: tsi')
        data = date.today()
        Intranet.navegador.get('https://tsicliint.intecomlogistica.com.br/#/')
        print("Logging")
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[3]/label[1]') \
            .send_keys(pwd.mail_tsi)
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[3]/label[2]') \
            .send_keys(pwd.pwd_tsi)
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[4]/button[2]') \
            .send_keys(Keys.ENTER)
        sleep(2.0)
        print('Opções de Download')
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/header/div/button').click()
        # sleep(2.0)
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div/a[5]/div[2]/div').click()
        sleep(2.0)
        Intranet.navegador.find_element('xpath', '//*[@id="tabelaFornecedores"]/div[1]/div[3]/div/button').send_keys(
            Keys.ENTER)
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
        Intranet.navegador.find_element('xpath',
                                        '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[2]/label/div/div/div[1]/input').send_keys(
            dta_inicial_formatada)
        sleep(3.0)
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div[2]/div[2]/div[3]/label').send_keys(
            dta_final_formatada)
        sleep(3.0)
        print('Seleciona filial')
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div[2]/div[3]/div[2]/label').click()
        sleep(2.0)
        print(" Seleciona 'João Pessoa'")
        Intranet.navegador.find_element('xpath', '//*[@id="qvs_5"]/div[4]').send_keys(Keys.ENTER)
        sleep(3.0)
        print('Clica em filtrar')
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div[2]/div/div[3]/button[2]').send_keys(Keys.ENTER)
        sleep(60.0)
        print('Baixar planilha')
        Intranet.navegador.find_element('xpath',
                                        '/html/body/div[1]/div/div/main/div[2]/div[1]/div[3]/div/div/button').send_keys(
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
            cont_copias += 1

class Tracking:
    ano = 2023

    def importa_data_expedicao(self):
        print('Classe: Tracking, Método: importa_data_expedicao')
        Intranet.acessa_tela_tracking(self)  # importa a lista de nfs nao entregues
        a = Intranet.gera_lista_nfs_nao_expedidas(self)

        if Feedback.dist(self) == '1':
            df = pd.read_excel(teste_arquivo,
                               sheet_name='BASE TRACKING 2023')
            # df = pd.read_excel('C:/Users/User/OneDrive - Baruel/CUSTOMER SERVICE/CUSTOMER SERVICE/AREA 02 NE/Tracking BNE - 2023.xlsx', sheet_name='BASE TRACKING 2023')
        if Feedback.dist(self) =='2':
            df = pd.read_excel(teste_arquivo,
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

        a = Intranet.gera_lista_ped_sem_agenda(self)
        # df = Feedback.df()
        print(Feedback.dist)
        df = pd.read_excel(f'{teste_arquivo}', sheet_name='BASE TRACKING 2023')


        relatorio = df[["PEDIDO", "DT.AGEND."]]  # considera todas as datas de agenda, inclusive as de nfs já entregues
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        # print('-----------------------')
        # print('<<<<<<Relatório>>>>>>>>')
        # print(relatorio)
        # print('-----------------------')
        print('* * * * * * Importa Data De Agenda * * * * * *')

        data_agenda_ini = pd.to_datetime(relatorio['DT.AGEND.'])  # puxa a data no formato yyyy-mm-dd
        data_agenda = data_agenda_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        pdd = relatorio['PEDIDO']  # puxa em float
        # print('VARIAVEL PDD')
        print(pdd, end='')
        pedido_int = pdd

        pedido_int = pedido_int.astype(int)  # transforma float em int
        pedido = pedido_int
        trk = zip(pedido, data_agenda)
        tracking = dict(trk).items()

        cont = 0
        # cont_teste = 0
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

                # # TRECHO DE VERIFICADO DO FORMATO DOS DADOS
                # print('-----------------------')
                # print(p)
                # print('-----------------------')
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

        if Feedback.dist(self) == '1':
            df = pd.read_excel('C:/Users/User/OneDrive - Baruel/CUSTOMER SERVICE/CUSTOMER SERVICE/AREA 02 NE/Tracking BNE - 2023.xlsx', sheet_name='BASE TRACKING 2023')
        if Feedback.dist(self) == '2':
            print(f'Teste arquivo >>>{teste_arquivo}')
            df = pd.read_excel(teste_arquivo,
                               sheet_name='BASE TRACKING 2023')

            # df = pd.read_excel(f'{Feedback.dataframe}', sheet_name='TRACKING 2023')

        relatorio = df.loc[df["STATUS"] == "ENTREGUE", ["STATUS", "DOC", "DTA ENTREGA"]]

        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        data_entrega_ini = pd.to_datetime(relatorio['DTA ENTREGA'])  # puxa a data no formato yyyy-mm-dd
        data_entrega = data_entrega_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        doc = relatorio['DOC']  # puxa em float
        doc_int = doc.astype(int)  # transforma float em int
        doc = doc_int
        trk = zip(doc, data_entrega)
        tracking = dict(trk).items()
        print(tracking)
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

class Intranet(Feedback, object):
    print('Classe: Intranet')
    options = Options()
    # options.add_argument("--headless=new")
    options.page_load_strategy = 'normal'
    navegador = webdriver.Chrome(options=options)
    navegador.minimize_window()

    def acessa_intranet(self):
        print('Classe: Intranet, Método: acessa_Intranet')
        Intranet.navegador.get('http://45.236.77.106:51236/intranet/login.php')

        # fazer  login
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').clear()

        Intranet.navegador.find_element('xpath',
                                        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys(
            pwd.mail)
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
            pwd.pwd)
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
            Keys.ENTER)

    def acessa_tela_pedidos_otc(self):
        print('class: Intranet, método: acessa_tela_pedidos_otc')
        Intranet.navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys('L')
        Intranet.navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys(Keys.ENTER)
        print('acessa logística')
        # acessar 'Logística'
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[2]/a').click()
        print('acessa pedidos otc')
        # acessar pedidos otc
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[2]/ul/a[2]').click()

        if Feedback.dist(self) == '2':  # extrema

            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            if self.opcao_regional == '2 - NORDESTE':
                Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(Keys.ARROW_DOWN)
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(Keys.ARROW_DOWN)
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(Keys.ENTER)


                # ['TODAS','1 - NORTE', '2 - NORDESTE', '3 - LESTE', '4 - FARMA', '5 - ALIM DIRETO', '6 - ALIM INDIRETO', '7 - CENTRO-OESTE']

        if Feedback.dist(self) == '1':  # Alhandra
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            # /html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select

    def acessa_tela_tracking(self):
        print('Classe: Intranet, Método: acessa_tela_tracking')
        Intranet.acessa_intranet(self)

        # acessar 'Customer Services'
        print('Acessa Customer Services')
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/a').click()
        # acessar Tracking
        print('Acessa Distribuidor')
        print(f'Feedback.dist(self) >> {Feedback.dist(self)}')
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/ul/a[1]').click()
        # 1 > Extrema 2 > Alhandra

        if Feedback.dist(self) == '1':
            print('Acessa Alhandra')
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)

        if Feedback.dist(self) == '2':
            print('Acessa Extrema')
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)

    def gera_lista_nfs_nao_expedidas(self):
        print('Classe: Intranet, Método: gera_lista_nfs_nao_expedidas')
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()  # FILTRA NFS NAO expedidas
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[2]').click()  # opção nao expedidos
        data = date.today()
        dta_inicial = data - timedelta(120)

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
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[3]/tbody/tr/td[1]/input').send_keys(Keys.ENTER)

        nfs_nao_expedidas = []
        tr = 2
        try:
            while True:

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
            print('Verificar Erro')
        finally:
            print(f"{tr - 2} NF'S nao expedidas")
            print(f'Lista > {nfs_nao_expedidas}')
        return nfs_nao_expedidas

    def acessa_tela_atualizar_expedicao(self):
        print('Classe: Intranet, Método: acessa_tela_atualizar_expedicao')
        tracking = Tracking.importa_data_expedicao(self)
        # # acessar 'Customer Services'
        Intranet.navegador.find_element('xpath','//*[@id="navigation"]/ul/li[4]/a').click()  # clica em customer services
        if Feedback.dist(self) == '1':  # seleciona a dist bs-alhandra

            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.dist(self) == '2':  # seleciona a dist bs-extrema
            # Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            # Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
        Intranet.navegador.find_element('xpath','//*[@id="navigation"]/ul/li[4]/ul/a[5]').click()  # clica em expedição/entrega

        # ACESSA TELA DE EXPEDIÇÃO

        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[9]/a').click()  # clica no botão 'expedição'

        if Feedback.dist(self) == '2':  # número de série da NF
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('3')

        if Feedback.dist(self) == '1':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('4')
        # importa lista com as nfs/dtas entrega que deverão ser lançadas
        c = 1
        cont_nfs_expedidas = 0
        for nf, data in tracking.items():
            print(f'{c} - {nf}: {data} ')

            data = data.replace("/", "")
            c += 1

            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/input').send_keys(nf)

            # data de expedicao
            Intranet.navegador.find_element('xpath', '//*[@id="calendario1"]').send_keys(data)

            #  grava
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/input').send_keys(Keys.ENTER)
            cont_nfs_expedidas += 1



        print(f'{cont_nfs_expedidas} datas lançadas')

    def gera_lista_ped_sem_agenda(self):
        print('Class: Intranet - Metodo: Gera_lista_ped_sem_agenda')
        """
        
        lst_area = ''
        if Feedback.abrir_arquivo == 'C:/Users/User/Baruel/Baruel - CUSTOMER SERVICE/AREA 01 NORTE/TRACKING R1 - NORTE - VIRGINIO.xlsx':
            lst_area = 'NORTE'
        if Feedback.abrir_arquivo == 'C:/Users/User/Baruel/Baruel - CUSTOMER SERVICE/AREA 02 NE/TRACKING_NE_EXTREMA.xlsx':
            lst_area = 'NORDESTE'

        if Feedback.abrir_arquivo == ' C:/Users/User/Baruel/Baruel - CUSTOMER SERVICE/AREA 03/AREA 03 LESTE - ANA':
            lst_area = 'LESTE'
        if Feedback.abrir_arquivo == 'C:/Users/User/Baruel/Baruel - CUSTOMER SERVICE/AREA 04 - FARMA/TRACKING FARMA - 2023.xlsx':
            lst_area = 'FARMA BRASIL'
        if Feedback.abrir_arquivo =='G:\Drives compartilhados\CUSTOMER SERVICE\AREA 05 - ALIMENTAR DIRETO\BASE TRACKING 2023.xlsx':
            lst_area = 'SP/SUL ALIMENTAR DIRETO'
        if Feedback.abrir_arquivo ==  'G:\Drives compartilhados\CUSTOMER SERVICE\AREA 03 E 06\TRACKING LESTE ALIMENTAR INDIRETO.xlsx':
            lst_area = 'SP/SUL ALIMENTAR INDIRETO'
        if Feedback.abrir_arquivo ==  'G:\Drives compartilhados\CUSTOMER SERVICE\AREA 07 CO-RO-AC-MG\TRACKING R7 - CO-RO-AC-MG - MARAFON - Atual.xlsx':
            lst_area = 'CENTRO OESTE'


        if Feedback.dist(self) == '2':
            print(lst_area)

            # area = input('AREA (Pressione "ENTER" Para Todas): ')
        """
        mes = Feedback.selec_mes(self)

        print(f'Mês selecionado: {mes}')
        # mes = str(input("Mês (mmm): "))
        print('Intranet.acessa_intranet')
        Intranet.acessa_intranet(self)
        print('Intranet.acessa_tela_pedidos_otc')
        Intranet.acessa_tela_pedidos_otc(self)
        print('seleciona mês')
        # seleciona mês
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[3]/select').send_keys(
            f'{mes}')
        print(f'Mês de pesquisa: {mes}')

        # seleciona a tela de agendamento
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').send_keys(
            'agendamento')

        # SELECIONA REGIONAL

        """
        area = '0'
        if Feedback.dist(self) == '1' and area in lst_area:
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                f'{area}')
        """
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
        print('class: Intranet, método: atualiza_agenda')
        tracking = Tracking.importa_data_agenda(self)
        print(tracking)
        print('----------------------------------')
        print(f'Regional {self.opcao_regional}')
        if self.opcao_regional == '1 - NORTE':
            print('teste ok')
        else:
            print('proximo passo')
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

                        # print(f'Analisando linha {cont_tr} | pedido {i}')
                        nome = Intranet.navegador.find_element('xpath',
                                                               f'/html/body/form[2]/table[3]/tbody/tr[{cont_tr}]/td[1]/input').get_dom_attribute(
                            'name')
                        # print(nome)

                        if nome == f'marcacao_agenda[{i}]':
                            print(f'> {cont_agenda_incluida}- Pedido {i} - agendado para {tracking[i]}')
                            Intranet.navegador.find_element('xpath',
                                                            f'/html/body/form[2]/table[3]/tbody/tr[{cont_tr}]/td[1]/input').send_keys(
                                tracking[i])  # ok
                            cont_agenda_incluida += 1
                            # if cont_agenda_incluida == len(Tracking.importa_data_agenda(self)):
                            #     Intranet.navegador.find_element('xpath', '/html/body/form[2]//div[2]/input').click()
                            #     break
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
        if Feedback.dist(self) == '1':  # bs-alhandra
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
        if Feedback.dist(self) == '2':  # bs-extrema
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr/td/input').click()
        # ACESSA A TELA 'ENTREGA'
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[10]/a').click()
        dist = Feedback.dist
        # número de série da NF
        if Feedback.dist(self) == '1':
            # /html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '4')
        if Feedback.dist(self) == '2':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '3')
        # importa lista com as nfs/dtas entrega que deverão ser lançadas
        print(f'distribuidora {Feedback.dist(self)} - {type(Feedback.dist(self))}')
        c = 1
        cont_nfs_entregues = 0
        for nf, data in tracking.items():
            print(f'{c} - {nf}: {data} ')
            data = data.replace("/", "")
            c += 1
            # INSERIR UMA LINHA PARA CASO JÁ HAJA DATA DE ENTREGA LANÇADA, NÃO SOMAR NO TOTAL
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/input').send_keys(
                nf)
            # data de entrega
            Intranet.navegador.find_element('xpath', '//*[@id="calendario1"]').send_keys(data)

            #  grava
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/input').send_keys(
                Keys.ENTER)
            cont_nfs_entregues += 1

        print(f'{cont_nfs_entregues} datas lançadas')

    def gera_lista_nfs_nao_entregues(self):
        print('Classe: Intranet, Método: gera_lista_nfs_nao_entregues')
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[3]').click()
        data = date.today()
        dta_inicial = data - timedelta(120)

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
        print('Feedback.Intranet.gera_lista_nfs_nao_entregues(self)')
        Intranet.gera_lista_nfs_nao_entregues(self)
        print('Tracking.importa_data_entrega(self)')
        Tracking.importa_data_entrega(self)  # funcionando

def main():
    print('def main')
    root = Tk()
    root.config(border=(20))

    feedback = Feedback(root, opcao_mes=StringVar(), opcao_regional=StringVar(), teste_arquivo=StringVar())
    root.mainloop()

if __name__ == '__main__': main()
