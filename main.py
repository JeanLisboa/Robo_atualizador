import os
import time
from datetime import timedelta, date, datetime
from time import sleep
from tkinter import *
from tkinter import messagebox, ttk, filedialog as fd
import pandas as pd
import pywhatkit
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

class Feedback:
    print('Class Feedback')
    def __init__(self, master, opcao_mes, opcao_ano, opcao_regional, teste_arquivo, info_backlog):
        self.opcao_mes = opcao_mes
        self.opcao_ano = opcao_ano
        self.opcao_regional = opcao_regional
        self.teste_arquivo = teste_arquivo
        self.info_backlog = info_backlog  # Atributo da classe

        master.title('Atualizações Diárias Tracking')
        master.resizable(False, False)

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
        self.sel_arquivo = ttk.Button(self.Labelframe_seleciona_dist, text='Selecionar arquivo',
                                      command=self.abrir_arquivo).grid(row=2, column=1, sticky='sw')

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

        # self.op5_report = ttk.Radiobutton(self.Labelframe_atualiza)
        # self.op5_report.config(text='Report', variable=self.opcao_processo, value=4, command=self.sel_processo)
        # self.op5_report.grid(row=5, column=0, sticky='sw')

        self.opcao_regional = StringVar()
        self.opcao_mes = StringVar()
        self.teste_arquivo = StringVar()
        self.opcao_ano = StringVar()
        self.info_backlog = StringVar()

        self.combobox = ttk.Combobox(self.Labelframe_atualiza)
        self.combobox.config(textvariable=self.opcao_mes,
                             values=['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov',
                                     'dez'], width=4)
        self.combobox.grid(row=2, column=1, sticky='sw')
        self.combobox.bind('<<ComboboxSelected>>', self.selec_mes)  # 'self.selec_mes' é a função q está fora da classe
        # --------------------------
        self.combobox2 = ttk.Combobox(self.Labelframe_atualiza)
        self.combobox2.config(textvariable=self.opcao_regional,
                              values=['TODAS', '1 - NORTE', '2 - NORDESTE', '3 - LESTE', '4 - FARMA', '5 - ALIM DIRETO',
                                      '6 - ALIM INDIRETO', '7 - CENTRO-OESTE'], width=17)
        self.combobox2.grid(row=2, column=2, sticky='sw')
        self.combobox2.bind('<<ComboboxSelected>>',
                            self.selec_regional)  # 'self.selec_mes' é a função q está fora da classe

        self.combobox3 = ttk.Combobox(self.Labelframe_atualiza)
        self.combobox3.config(textvariable=self.opcao_ano,
                              values=['2023', '2024'], width=5)
        self.combobox3.grid(row=2, column=3, sticky='sw')
        self.combobox3.bind('<<ComboboxSelected>>', self.selec_ano)

        # self.combobox.state(['readonly', 'disabled'])
        self.combobox.state(['readonly'])
        self.combobox2.state(['readonly'])
        self.combobox3.state(['readonly'])
        # ----------------------------------
        self.Labelframe_atualiza.pack(fill=BOTH, expand=True)

        # configura o terceiro Labelframe
        # self.Labelframe_report_comercial = ttk.LabelFrame(master)  # 3a janela filho
        # self.Labelframe_report_comercial = ttk.LabelFrame(master)  # 3a janela filho
        # self.Labelframe_report_comercial.config(relief=GROOVE, text='Report Comercial')
        # ttk.Label(self.Labelframe_report_comercial, text='Região').grid(row=1, column=0, sticky='sw')
        # ttk.Label(self.Labelframe_report_comercial, text='Vendedor').grid(row=2, column=0, sticky='sw')
        #
        # self.op_regiao = StringVar()
        # self.regiao = ttk.Combobox(self.Labelframe_report_comercial)
        # self.regiao.config(textvariable=self.op_regiao, values='02 NORDESTE')
        # self.regiao.grid(row=1, column=1, sticky='sw')
        # self.regiao.bind('<<ComboboxSelected>>',
        #                  self.selec_regional)  # 'self.selec_mes' é a função q está fora da classe
        # self.regiao.state(['readonly', 'disabled'])
        #
        # self.op_vend = StringVar()
        # self.vendedor = ttk.Combobox(self.Labelframe_report_comercial)
        # self.vendedor.config(textvariable=self.op_vend, values=(
        #     'TODOS', '000669 FLAVIO SILVA', '000671 MARLEI', '000508 JEANY', '000595 GUALTER', '000656 FLAVIO',
        #     '000641 LUCIA', '000502 CLEBER', '000654 PAULO BESERRA', '000686 LUANA'))
        # self.vendedor.grid(row=2, column=1, sticky='sw')
        # self.vendedor.state(['readonly', 'disabled'])
        #
        # self.vendedor.bind('<<ComboboxSelected>>', self.seleciona_vendedor)
        # self.Labelframe_report_comercial.pack(fill=BOTH, expand=True)

        # configura o quarto Labelframe

        self.Labelframe_executar = ttk.LabelFrame(master)  # 4a janela filho
        self.Labelframe_executar.config(relief=GROOVE)

        ttk.Button(self.Labelframe_executar, text='OK', command=self.executar).grid(row=0, column=1, sticky='sw')
        ttk.Button(self.Labelframe_executar, text='Fechar', command=self.fechar).grid(row=0, column=2, sticky='sw')
        ttk.Button(self.Labelframe_executar, text='TSI', command=self.tsi).grid(row=0, column=0, sticky='sw')
        # ttk.Button(self.Labelframe_executar, text='Carteira', command=self.acessa_carteira).grid(row=0, column=3, sticky='sw')
        self.Labelframe_executar.pack(fill=BOTH, expand=True)
        ttk.Label(self.Labelframe_executar, text='Desenvolvido por Jean Lino', font=('arial', 9, "italic")).grid(row=1, column=0, stick='sw')


    # funçoes do tkinter

    def sel_processo(self):
        print('Class: Feedback, Método: sel_processo. \n')
        a = self.opcao_processo.get()

        if a == '1':
            print(f'{a} - executar processo atualiza expedição')
        if a == '2':
            print(f'{a} - executar processo atualiza agenda')
        if a == '3':
            print(f'{a} - executar processo atualiza entrega')
        if a == '0':
            print(f'{a} - executar processo atualizar todos')
        if a == '4':
            print(f'{a} - executar processo report')
            self.regiao.state(['!disabled'])
            self.vendedor.state(['!disabled'])
            self.combobox.state(['disabled'])

    def sel_dist(self):
        # print('class: Feedback, método: sel_dist \n')
        a = self.opcao_dist.get()
        # print(f'Distribuidora {a} selecionada')
        return a

    def selec_mes(self, *args):
        print('class: Feedback, método: sel_mes \n')
        a = self.opcao_mes.get()
        print(f'mês {a} selecionado')
        return a

    def selec_regional(self, *args):
        # print('class: Feedback, método: selec_regional \n')
        a = self.opcao_regional.get()
        # print(f'Regional {a} Selecionada')
        return a

    def selec_ano(self, *args):
        print('class: Feedback, método: selec_ano \n')
        a = self.opcao_ano.get()
        print(a)
        # print(f'def selec_ano retorna: {a}')
        return a

    # def seleciona_vendedor(self, *args):
    #     print('class: Feedback, método: seleciona_vendedor')
    #     a = self.op_vend.get()
    #     print(a)

    def report_comercial(self):
        print('class: Feedback, método: report_comercial')
        """Report_comercial

        Esta função utiliza o PyautuGUI e  envia as informações da
        coluna 'Observaçõeservação' via WhatsApp
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
            # contato = '+5581994447916'  # marlei 81994447916 >> luana   5571981075723
            contato = '+5583993637279'

        if a == '000686 LUANA':
            cod_vend = '000686 LUANA'
            msg_vend = str('Bom dia Luana, tudo bem ?')
            # contato = '+5571981075723'
            contato = '+5583993637279'

        if a == '000669 FLAVIO SILVA':
            cod_vend = '000669 FLAVIO SILVA'
            msg_vend = str('Bom dia Flávio, tudo bem ?')
            # contato = '+5531984034352'
            contato = '+5583993637279'

        if a == '000508 JEANY':
            cod_vend = '000508 JEANY'
            msg_vend = str('Bom dia Jeany, tudo bem ?')
            # contato = '+5584999811102'  # +5584999811102
            contato = '+5583993637279'

        if a == '000595 GUALTER':
            cod_vend = '000595 GUALTER'
            msg_vend = str('Bom dia Gualter, tudo bem ?')
            # contato = '+5582988110209'
            contato = '+5583993637279'

        if a == '000656 FLAVIO':
            cod_vend = '000656 FLAVIO'
            msg_vend = str('Bom dia Flávio, tudo bem ?')
            # contato = '+5585991239734'
            contato = '+5583993637279'

        if a == '000641 LUCIA':
            cod_vend = '000641 LUCIA'
            msg_vend = str('Bom dia Vanessa, tudo bem ?')
            # contato = '+5583998072021'
            contato = '+5583993637279'

        if a == '000502 CLEBER':
            cod_vend = '000502 CLEBER'
            msg_vend = str('Bom dia Cléber, tudo bem ?')
            # contato = '+5587996265806'
            contato = '+5583993637279'

        if a == '000654 PAULO BESERRA':
            cod_vend = '000654 PAULO BESERRA'
            msg_vend = str('Bom dia Paulo, tudo bem ?')
            # contato = '+5586999773176'  #'+5586999773176'
            contato = '+5583993637279'

        print(f' Cod vend: {cod_vend}')
        print(f'Contato: {contato}')
        print(f'Msg vend: {msg_vend}')
        df = pd.read_excel(self.teste_arquivo, sheet_name=Feedback.aba_excel(self))
        relatorio = df.loc[
            (df['Status Macro'] != 'ENTREGUE') & (df['Status Macro'] != 'DEVOLUÇÃO'), ["VEND", "Doc", "CLIENTE",
                                                                                       "Nome Fantasia",
                                                                                       "Cidade", "VOLUME", "Agend",
                                                                                       "PREVISÃO ENTREGA",
                                                                                       "Observações"]]

        relatorio2 = relatorio.loc[relatorio['VEND'] == cod_vend, ["VEND", "Doc", "Nome Fantasia", "Observações"]]

        rel3 = relatorio2[["Doc", "Nome Fantasia", "Observações"]]
        rel3 = rel3.dropna(axis=0)  # exclui as colunas com valores vazios
        doc = rel3['Doc'].tolist()

        lst_doc = []
        for a in doc:
            a = int(a)
        lst_doc.append(a)
        doc = lst_doc
        dest = rel3['Nome Fantasia'].tolist()
        Observações = rel3['Observações'].tolist()
        trk = zip(dest, Observações)

        # trk2 = zip(doc, trk)
        tracking = dict(trk).values()
        # print(len(doc))
        if len(doc) == 0:
            messagebox.showinfo('', 'Não há Entregas pendentes para este vendedor')
        else:
            pywhatkit.sendwhatmsg_instantly(phone_no=contato, wait_time=10, tab_close=True, close_time=3,
                                            message=f'{msg_vend}\n Seguem informações: \n')
            for a in range(len(doc)):
                pywhatkit.sendwhatmsg_instantly(phone_no=contato, wait_time=10, tab_close=True, close_time=3,
                                                message=f"{doc[a]} | {dest[a]} | {Observações[a]}")
                print(f"{doc[a]} | {dest[a]} | {Observações[a]}")
            messagebox.showinfo('', 'Report Concluído')

    dist = sel_dist
    mes = selec_mes
    df = 0

    def aba_excel(self):
        if self.opcao_ano == 2023:
            aba = 'Base'
        else:
            aba = 'Base'
        return aba

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
            # self.df = pd.read_excel(self.abrir_arquivo, sheet_name='BASE TRACKING 2024')
        return self.df

    sel_arquivo = ''

    def abrir_arquivo(self):
        global teste_arquivo
        print('class: Feedback, método: abrir_arquivo')
        filetypes = (('excel files', '*.xlsx'), ('All files', '*.*'))
        sel_arquivo = fd.askopenfile(title='Selecione o Tracking',
                                     initialdir='C:/Users/User/Baruel/Baruel - CUSTOMER SERVICE/CUSTOMER SERVICE/01. ACOMPANHAMENTO GERAL',
                                     filetypes=filetypes)
        ttk.Label(self.Labelframe_seleciona_dist, text=sel_arquivo.name).grid(row=3, column=1, sticky='sw')
        print(f'arquivo selecionado: {sel_arquivo.name}')
        teste_arquivo = str(sel_arquivo.name)
        teste_arquivo = teste_arquivo.replace('/', '\\')
        teste_arquivo = f'{teste_arquivo}'
        return teste_arquivo

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
            retorno = Intranet.acessa_tela_atualizar_expedicao(self)
            # import tela_backlog
            #
            # global info_backlog  # especifica que se quer alterar a variável global
            # info_backlog = retorno
            #
            # # tela_backlog.BacklogApp.adicionar_backlog(info_backlog)

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

    def acessa_carteira(self):
        print('class: Intranet, método: acessa_carteira')
        Intranet.acessa_intranet(self)
        Intranet.navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys('L')
        Intranet.navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys(Keys.ENTER)
        Intranet.navegador.find_element('xpath', '/html/body/div[2]/ul/li[1]/a').click()
        Intranet.navegador.find_element('xpath', '/html/body/div[2]/ul/li[1]/ul/a[1]').click()
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').click()
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr/td[1]/input').send_keys(Keys.ENTER)

        pedidos = []
        situacao = []
        fase = []
        emissao = []
        nome_fantasia = []
        uf = []
        qtd_saldo = []
        vlr_saldo = []

        tr = 2
        try:
            while True:

                col_vlr_saldo = Intranet.navegador.find_element('xpath',f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[25]') # VLr SALDO
                vlr_sld = col_vlr_saldo.text
                vlr_saldo.append(vlr_sld)

                col_pedido = Intranet.navegador.find_element('xpath',f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[3]') # pedido
                pedido = col_pedido.text
                pedido = int(pedido)
                pedidos.append(pedido)

                col_situacao = Intranet.navegador.find_element('xpath',f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[6]')  # situacao
                sit = col_situacao.text
                situacao.append(sit)

                col_fase = Intranet.navegador.find_element('xpath',f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[7]') # fase
                fse = col_fase.text
                fase.append(fse)

                col_nome_fant = Intranet.navegador.find_element('xpath', f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[12]') # nome_fantasia
                nme_fant = col_nome_fant.text
                nome_fantasia.append(nme_fant)

                col_uf = Intranet.navegador.find_element('xpath', f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[13]') # UF
                uff = col_uf.text
                uf.append(uff)

                col_qtd_saldo = Intranet.navegador.find_element('xpath',
                                                                f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[24]') # QTD SALDO
                qtd_sld = col_qtd_saldo.text
                qtd_sld = qtd_sld.replace('.', '')
                qtd_sld = int(qtd_sld)
                if qtd_sld == "":
                    col_qtd_saldo == 0
                qtd_saldo.append(qtd_sld)
                tr += 2

        except Exception as e:
            print(e)
            print('fim')
            print('--------------------------')

        finally:
            print(f"{tr - 2} pedidos localizados")
            print(f'Lista pedidos > {pedidos} - {len(pedidos)}')
            print(f'Lista situacao > {situacao} - {len(situacao)}')
            print(f'Lista fase > {fase} - {len(fase)}')
            # print(f'Lista dt Emissao > {dt_emissao}')
            print(f'Lista dt nome fantasia > {nome_fantasia} - {len(nome_fantasia)}')
            print(f'Lista vlr saldo > {vlr_saldo} - {len(vlr_saldo)}')
            print(f'Lista qtde saldo > {qtd_saldo} - {len(qtd_saldo)}')
            df = pd.DataFrame({
                'Pedido': pedidos,
                'Situação': situacao,
                'Fase': fase,
                'Destinatário': nome_fantasia,
                'Valor Saldo': vlr_saldo,
                'Quantidade Saldo': qtd_saldo
            })
            caminho_arquivo = r'C:\Users\jean.lino\OneDrive - Baruel\CONTROLES\BASE_AUTOMATICA\CARTEIRA_ALH.xlsx'
            df.to_excel(caminho_arquivo, index=False)
        print(pedidos)
        print()

    @staticmethod
    def tsi():
        # navegador = self.navegador()
        print('class: Feedback, método: tsi')
        data = date.today()
        Intranet.navegador.get('https://tsicliint.intecomlogistica.com.br/#/')
        print("Logging")
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[3]/label[1]') \
            .send_keys('jean.lino@baruel.com.br')
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[3]/label[2]') \
            .send_keys('151082')
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/div/main/div/div[4]/button[2]') \
            .send_keys(Keys.ENTER)
        Intranet.navegador.implicitly_wait(10.0)
        sleep(2.0)
        print('Opções de Download')
        Intranet.navegador.find_element('xpath', '//*[@id="q-app"]/div/header/div/button').click()
        # sleep(2.0)
        Intranet.navegador.find_element('xpath', '/html/body/div[3]/div/a[5]/div[2]/div').click()
        sleep(2.0)
        Intranet.navegador.find_element('xpath', '//*[@id="tabelaFornecedores"]/div[1]/div[3]/div/button').send_keys(
            Keys.ENTER)

        print('Insere data Inicial')
        if data.day < 10 and data.month < 10:
            dta_final_formatada = f'0{data.day}/0{data.month}/{data.year}'  # ano  formato xx/xx/xxxx

        if data.day < 10 and data.month > 9:
            dta_final_formatada = f'0{data.day}/{data.month}/{data.year}'  # ano  formato xx/xx/xxxx

        if data.day > 9 and data.month < 10:
            dta_final_formatada = f'{data.day}/0{data.month}/{data.year}'  # ano  formato xx/xx/xxxx

        print('Insere data final')
        dta_inicial = data - timedelta(30)
        if dta_inicial.day < 10 and dta_inicial.month < 10:
            dta_inicial_formatada = f'0{dta_inicial.day}/0{dta_inicial.month}/{dta_inicial.year}'
        elif dta_inicial.day < 10:
            dta_inicial_formatada = f'0{dta_inicial.day}/{dta_inicial.month}/{dta_inicial.year}'
        elif dta_inicial.month < 10:
            dta_inicial_formatada = f'{dta_inicial.day}/0{dta_inicial.month}/{dta_inicial.year}'

        else:
            dta_inicial_formatada = f'{dta_inicial.day}/{dta_inicial.month}/{dta_inicial.year}'
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
                               sheet_name=Feedback.aba_excel(self))
        if Feedback.dist(self) == '2':
            df = pd.read_excel(teste_arquivo,
                               sheet_name=Feedback.aba_excel(self))
        relatorio = df[["Doc"]]
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias

        # ----- teste, excluindo datas maiores que a data atual ---

        # relatorio['Expedicao'] = pd.to_datetime(relatorio['Expedicao'])
        data_atual = datetime.now().date()
        relatorio = df[pd.to_datetime(df['Expedicao']).dt.date <= data_atual][["Doc", "Expedicao"]]
        # relatorio = df[df['Expedicao'] <= data_atual][['doc', 'Expedicao']]

        # ---- fim do teste

        data_exped_ini = pd.to_datetime(relatorio['Expedicao'])  # puxa a data no formato yyyy-mm-dd
        data_exped = data_exped_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        doc = relatorio['Doc']  # puxa em float
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
        df = pd.read_excel(f'{teste_arquivo}', sheet_name=Feedback.aba_excel(self))
        relatorio = df[["Pedido", "Dt Agenda"]]  # considera todas as datas de agenda, inclusive as de nfs já entregues
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        print('Relatorio')
        print(relatorio)
        print('* * * * * * Importa Data De Agenda * * * * * *')

        data_agenda_ini = pd.to_datetime(relatorio['Dt Agenda'])  # puxa a data no formato yyyy-mm-dd
        data_agenda = data_agenda_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        pdd = relatorio['Pedido']  # puxa em float
        # print('*** PRINTA PEDIDO EM FLOAT ***')
        # print(pdd, end='')
        pedido_int = pdd

        pedido_int = pedido_int.astype(int)  # transforma float em int
        # print('*** PEDIDO CONVERTIDO EM INT *** ')
        pedido = pedido_int
        trk = zip(pedido, data_agenda)
        tracking = dict(trk).items()
        cont = 0
        dicionario = {}

        for p, d in tracking:  # p = numero do pedido / d = data da agenda
            if type(d) != str:
                d = "0"
            if p in a:
                p = str(p)
                if len(p) == 3:
                    p = f'000' + p
                if len(p) == 4:
                    p = f'00' + p
                if len(p) == 5:
                    p = f'0' + p
                dicionario_temp = {p: d}  # transforma o set em dict
                dicionario.update(dicionario_temp)  # copia o dicionario_temp dentro do dict definitivo
                dicionario_temp.clear()  # limpa o dicionario
                # temp
                cont += 1

        # print(dicionario)  # mostra os pedidos e datas localizados na planilha
        if cont == 0:
            print(f'\n{cont} pedidos localizados')

        return dicionario

    def importa_data_entrega(self):
        print('Classe: Tracking, Método: importa_data_entrega')

        Intranet.acessa_tela_tracking(self)  # importa a lista de nfs nao entregues
        a = Intranet.gera_lista_nfs_nao_entregues(self)  # trf a lst em var
        df = pd.read_excel(teste_arquivo,
                           sheet_name=Feedback.aba_excel(self))
        relatorio = df.loc[df["Status Macro"] == "ENTREGUE", ["Status Macro", "Doc", "Dt Entrega"]]
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        data_entrega_ini = pd.to_datetime(relatorio['Dt Entrega'])  # puxa a data no formato yyyy-mm-dd
        data_entrega = data_entrega_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        doc = relatorio['Doc']  # puxa em float
        doc_int = doc.astype(int)  # transforma float em int
        doc = doc_int
        trk = zip(doc, data_entrega)
        tracking = dict(trk).items()
        # print(tracking)
        cont = 0
        dicionario = {}
        for p, d in tracking:
            if d != '':
                if p in a:
                    dicionario_temp = {p: d}  # transforma o set em dict
                    dicionario.update(dicionario_temp)  # copia o dicionario_temp dentro do dict definitivo
                    dicionario_temp.clear()  # limpa o dicionario temp
                    cont += 1

        # print(dicionario)
        print(f'{cont} Datas de entrega localizadas')
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
        Intranet.navegador.get('http://45.236.77.106:51230/intranet/login.php')

        # fazer  login
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').clear()

        Intranet.navegador.find_element('xpath',
                                        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys(
            'jean.lino@baruel.com.br')
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
            'Ma250509')
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

        # define ano da pesquisa
        print(self.opcao_ano.get())
        # seleciona ano 2023
        if self.opcao_ano.get() == '2023':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/select').send_keys(
                Keys.ARROW_UP)

        if Feedback.dist(self) == '2':  # extrema

            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            if self.opcao_regional == '2 - NORDESTE':
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
                Intranet.navegador.find_element('xpath',
                                                '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                    Keys.ARROW_DOWN)
                Intranet.navegador.find_element('xpath',
                                                '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                    Keys.ARROW_DOWN)
                Intranet.navegador.find_element('xpath',
                                                '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                    Keys.ENTER)

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
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()  # FILTRA NFS NAO expedidas
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[2]').click()  # opção nao expedidos
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
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[3]/tbody/tr/td[1]/input').send_keys(
            Keys.ENTER)

        nfs_nao_expedidas = []
        tr = 2
        try:
            while True:
                linha = Intranet.navegador.find_element('xpath',
                                                        f'/html/body/form[2]/table[5]/tbody/tr[{tr}]/td[8]')  # busca o elemento NF a partir da linha 2
                col_nf = linha.text  # recebe a varivel linha como texto
                nf = col_nf
                nf = int(nf)  # transforma em inteiro
                tr += 1
                # print(linha)
                nfs_nao_expedidas.append(nf)  # insere na lista

        except:
            print("Busca Finalizada")
        finally:
            pass
            # print(f"{tr - 2} NF'S nao expedidas")
            # print(f'Lista > {nfs_nao_expedidas}')
        return nfs_nao_expedidas

    def acessa_tela_atualizar_expedicao(self):
        info_backlog = 'info_backlog main.py---- teste >>>'
        hoje = date.today()
        hoje_a = datetime.day
        delta = timedelta(days=2)
        margem_de_erro_anterior = hoje - delta
        margem_de_erro_posterior = hoje + delta
        nf_com_info_errada = ()
        lista_nfs_com_info_errada = []

        print('Classe: Intranet, Método: acessa_tela_atualizar_expedicao')
        tracking = Tracking.importa_data_expedicao(self)


        Intranet.navegador.find_element('xpath','//*[@id="navigation"]/ul/li[4]/a').click()  # clica em customer services
        # Intranet.navegador.find_element('xpath','//*[@id="navigation"]/ul/li[4]/a').send_keys(Keys.ARROW_DOWN)
        # /html/body/div[2]/ul/li[4]/ul/a[3]
        if Feedback.dist(self) == '1':  # seleciona a dist bs-alhandra
            # /html/body/div[2]/ul/li[4]/a
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)

        if Feedback.dist(self) == '2':  # seleciona a dist bs-extrema
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
        Intranet.navegador.find_element('xpath',
                                        '//*[@id="navigation"]/ul/li[4]/ul/a[3]').click()  # clica em expedição/entrega
        # /html/body/div[2]/ul/li[4]/ul/a[3]
        # //*[@id="navigation"]/ul/li[4]/ul/a[3]
        # ACESSA TELA DE EXPEDIÇÃO

        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[9]/a').click()  # clica no botão 'expedição'

        if Feedback.dist(self) == '2':  # número de série da NF
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '3')

        if Feedback.dist(self) == '1':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '4')
        # importa lista com as nfs/dtas entrega que deverão ser lançadas
        c = 1
        cont_erro = 0
        cont_nfs_expedidas = 0
        for nf, data in tracking.items():
            # print(f'{c} - {nf}: {data} ')

            data = data.replace("/", "")
            c += 1

            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/input').send_keys(
                nf)

            # data de expedicao
            Intranet.navegador.find_element('xpath', '//*[@id="calendario1"]').send_keys(data)

            #  grava
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/input').send_keys(
                Keys.ENTER)
            cont_nfs_expedidas += 1
            # RELACIONA NFS COM ERRO NO LANÇAMENTO DA DATA DE EXPEDIÇÃO
            alerta_erro = Intranet.navegador.find_element('xpath','/html/body/form[2]/div[2]').text
            dta_emissao = Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[4]').text

            if alerta_erro != '':
                lista_temp = []
                lista_temp.append(nf)
                lista_temp.append(dta_emissao)
                lista_temp.append(data)
                lista_temp.append(alerta_erro)
                lista_nfs_com_info_errada.append(lista_temp[:])
                lista_temp.clear()
                cont_erro += 1
                cont_nfs_expedidas += 1
            else:
                pass
            teste = lista_nfs_com_info_errada


        print(f"{cont_nfs_expedidas} datas processadas\n"
              f"{cont_erro} NF's com erro ")

        print('------ LOG DE ERRO DE DATAS DE EXPEDIÇÃO-------')
        for i in teste:
            print(i)
        print('------ FIM DO LOG DE ERRO -------')


    def gera_lista_ped_sem_agenda(self):
        print('Class: Intranet - Metodo: Gera_lista_ped_sem_agenda')
        mes = Feedback.selec_mes(self)

        print(f'Mês selecionado: {mes}')
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
        # print(f'Teste de input da regional selecionada {Feedback.selec_regional}')


        # SELECIONA REGIONAL
        regional = Feedback.selec_regional(self)
        if regional == '1 - NORTE':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ENTER)

        if regional == '2 - NORDESTE':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ENTER)

        if regional == '3 - LESTE':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ENTER)



        if regional == '4 - FARMA':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ENTER)

        if regional == '5 - ALIM DIRETO':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ENTER)

        if regional == '6 - ALIM INDIRETO':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ENTER)

        if regional == '7 - CENTRO - OESTE':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').click()
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(
                Keys.ENTER)

        # processa
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr/td/input').click()

        tr = 1

        pedidos_sem_agenda = []

        try:
            while True:
                linha = Intranet.navegador.find_element('xpath',f'/html/body/form[2]/table[3]/tbody/tr[{tr}]/td[2]')  # busca o elemento NF a partir da linha 2
                col_pedido = linha.text  # recebe a varivel linha como texto
                pedido = col_pedido
                pedido = int(pedido)
                tr += 1
                pedidos_sem_agenda.append(pedido)
        except:
            print(f'{tr - 2} Pedidos Sem Data de Agendamento')
            # print(f'Lista: {pedidos_sem_agenda}')

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

                        nome = Intranet.navegador.find_element('xpath',
                                                               f'/html/body/form[2]/table[3]/tbody/tr[{cont_tr}]/td[1]/input').get_dom_attribute(
                            'name')
                        # print(f'variavel nome: {nome} ')

                        if nome == f'marcacao_agenda[{i}]':
                            print(f'> {cont_agenda_incluida}- Pedido {i} - agendado para {tracking[i]}')
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
        nf_com_info_errada = ()
        lista_nfs_com_info_errada = []
        tracking = Tracking.importa_data_entrega(self)
        # acessar 'Customer Services'
        # CLICA EM CUSTOMER SERVICES
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/a').click()

        # CLICA NA TELA Sair do Sistema "Danfes com datas de expedição, entrega de devoluções"
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/ul/a[3]').click()

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

        # clica no botão 'entrega'
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[10]/a').click()

        dist = Feedback.dist
        # número de série da NF
        if Feedback.dist(self) == '1':

            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '4')
        if Feedback.dist(self) == '2':
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys(
                '3')
        # importa lista com as nfs/dtas entrega que deverão ser lançadas
        # print(f'distribuidora {Feedback.dist(self)} - {type(Feedback.dist(self))}')
        c = 1
        cont_erro = 0
        cont_nfs_entregues = 0
        # valida a data de entrega.
        for nf, data in tracking.items():
            # print(f'{c} - {nf}: {data} ')
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
            dta_emissao = Intranet.navegador.find_element('xpath','/html/body/form[2]/table[2]/tbody/tr[2]/td[4]').text
            alerta_erro = Intranet.navegador.find_element('xpath', '/html/body/form[2]/div[2]').text
            # print(f'Alerta erro: {alerta_erro}')
            if alerta_erro != '':
                lista_temp = []
                lista_temp.append(nf)
                lista_temp.append(dta_emissao)
                lista_temp.append(data)
                lista_temp.append(alerta_erro)
                lista_nfs_com_info_errada.append(lista_temp[:])
                lista_temp.clear()
                cont_erro += 1
                cont_nfs_entregues += 1
            else:
                pass
            teste = lista_nfs_com_info_errada

        print(f"{cont_nfs_entregues} datas processadas\n"
              f"{cont_erro} NF's com erro ")

        print('------ LOG DE ERRO DE DATAS DE ENTREGA -------')
        for i in teste:
            print(i)
        print('------  FIM DO LOG DE ERRO -----')


    def gera_lista_nfs_nao_entregues(self):
        print('Classe: Intranet, Método: gera_lista_nfs_nao_entregues')
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()
        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[3]').click()
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


        # posição da regiao na caixa

        pos_todas = 0
        pos_norte = 1
        pos_nordeste = 2
        pos_leste = 3
        pos_farma = 4
        pos_alim_direto = 5
        pos_alim_indireto = 6
        pos_centro_oeste = 7
        # 'TODAS', '1 - NORTE', '2 - NORDESTE', '3 - LESTE', '4 - FARMA', '5 - ALIM DIRETO',
        #                                       '6 - ALIM INDIRETO', '7 - CENTRO-OESTE']
        # clica na inputbox 'regiao'
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').click()
        for i in range (0, 9):
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_UP)

        if Feedback.selec_regional(self) == '1 - NORTE':
            for i in range(0, pos_norte):
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.selec_regional(self) == '2 - NORDESTE':
            for i in range(0, pos_nordeste):
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.selec_regional(self) == '3 - LESTE':
            for i in range(0, pos_leste):
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.selec_regional(self) == '4 - FARMA':
            for i in range(0, pos_farma):
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.selec_regional(self) == '5 - ALIM DIRETO':
            for i in range(0, pos_alim_direto):
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.selec_regional(self) == '6 - ALIM INDIRETO':
            for i in range(0, pos_alim_indireto):
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_DOWN)

        if Feedback.selec_regional(self) == '7 - CENTRO-OESTE':
            for i in range(0, pos_centro_oeste):
                Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr[2]/td[2]/select').send_keys(Keys.ARROW_DOWN)

        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(Keys.CLEAR)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(dia_ini_formatado)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(mes_ini_formatado)
        Intranet.navegador.find_element('xpath', '//*[@id="calendario2"]').send_keys(dta_inicial.year)
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[3]/tbody/tr/td[1]/input').send_keys(Keys.ENTER)

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
                tr += 1
                nfs_nao_entregues.append(nf)  # insere na lista

        except:
            pass
            print(f"{tr - 2} NF'S nao entregues")
            # print(f'Lista > {nfs_nao_entregues}')
        return nfs_nao_entregues

    def atualiza_entrega(self):
        print('Classe: Intranet, Método: atualiza_entrega')
        # print('Feedback.Intranet.gera_lista_nfs_nao_entregues(self)')
        Intranet.gera_lista_nfs_nao_entregues(self)
        # print('Tracking.importa_data_entrega(self)')
        Tracking.importa_data_entrega(self)

def main():
    print('def main')
    root = Tk()
    root.config(border=(20))
    feedback = Feedback(root, opcao_ano=StringVar, opcao_mes=StringVar(), opcao_regional=StringVar(),
                        teste_arquivo=StringVar(), info_backlog=StringVar)
    root.mainloop()

if __name__ == '__main__': main()
