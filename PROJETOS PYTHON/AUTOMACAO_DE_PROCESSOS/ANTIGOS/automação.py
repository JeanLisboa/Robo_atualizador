#BACKUP
import pandas as pd
from selenium import webdriver  # permite criar a janela
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

from datetime import date, timedelta
from datetime import date
import time

class Tracking:
    print('Class Tracking')
    print('Seleciona Distribuidor')
    dist = int(input('Distribuidora Extrema (1) Alhandra (2): '))
    print('Seleciona Processo')
    processo = int(input("                                 TRACKING\n"
                         "(1) Data de Expedição | (2) Data de Agendamento | (3) Data de Entrega\n"
                         "                                 INTRANET\n"
                         "(4) Lista NFS sem data de entrega | (5) Lista NFS sem data de expedição\n"
                         "(6) Atualiza Entrega | (7) Atualiza Expedição (Alhandra)| (8) Análises\n"
                         "                                     >>>"))
    if dist == 1:  # Extrema
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\TRACKING NE-BS-2023.xlsx',
                           sheet_name='BASE TRACKING 2023')  # tracking EXTREMA

    else:  # Alhandra
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\Tracking BNE - 2023.xlsx',
                           sheet_name='BASE TRACKING 2023')  # tracking ALHANDRA
    def importa_data_expedicao(self):
        print('Classe: Tracking, Método: importa_data_expedicao')
        Intranet.acessa_tela_tracking(self=Intranet) # importa a lista de nfs nao entregues
        a = Intranet.gera_lista_nfs_nao_expedidas()

        relatorio = Tracking.df[["DOC", "EXPED"]]
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

        relatorio = Tracking.df[["PEDIDO","DT.AGEND."]]  # considera todas as datas de agenda, inclusive as de nfs já entregues
        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        print('* * * * * * Importa Data De Agenda * * * * * *')


        data_agenda_ini = pd.to_datetime(relatorio['DT.AGEND.'])  # puxa a data no formato yyyy-mm-dd
        data_agenda = data_agenda_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
        pdd = relatorio['PEDIDO']  # puxa em float
        pedido_int = pdd.astype(int)  # transforma float em int
        pedido = pedido_int

        trk = zip(pedido, data_agenda)
        tracking = dict(trk).items()

        cont = 0
        dicionario = {}
        for p, d in tracking:
            if type(d) != str:
                d = "0"

            else:
                p = str(p)
                p = f'0' + p  # acrescenta o '0' no inicio do pedido

                dicionario_temp = {p: d}  # transforma o set em dict
                dicionario.update(dicionario_temp)  # copia o dicionario_temp dentro do dict definitivo
                dicionario_temp.clear()  # limpa o dicionario temp
                cont += 1
        print(dicionario)  # mostra os pedidos e datas localizados na planilha
        print(f'\n{cont} pedidos localizados')
    def importa_data_entrega(self):
        print('Classe: Tracking, Método: importa_data_entrega')
        Intranet.acessa_tela_tracking(self=Intranet) # importa a lista de nfs nao entregues
        a = Intranet.gera_lista_nfs_nao_entregues(self=Intranet) # trf a lst em var
        relatorio = Tracking.df.loc[Tracking.df['STATUS'] == 'ENTREGUE', [ "STATUS", "DOC", "DTA ENTREGA"]]

        relatorio = relatorio.dropna(axis=0)  # exclui as células  vazias
        data_entrega_ini = pd.to_datetime(relatorio['DTA ENTREGA'])  # puxa a data no formato yyyy-mm-dd
        data_entrega = data_entrega_ini.dt.strftime('%d/%m/%Y')  # formata para dd/mm/yyyy
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

class Intranet:
    print('Classe: Intranet')

    servico = Service(ChromeDriverManager().install())
    navegador = webdriver.Chrome(service=servico)
    navegador.minimize_window()

    def acessa_tela_atualizar_expedicao(self):
        print('Classe: Intranet, Método: acessa_tela_atualizar_expedicao')
        tracking = Tracking.importa_data_expedicao(self=Tracking)
        # # acessar 'Customer Services'

        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/a').click() #clica em customer services
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/ul/a[5]').click() #clica em expedição/entrega
        if Tracking.dist == 3:  #  seleciona a dist bs-alhandra
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
        if Tracking.dist == 1:  # seleciona a dist bs-extrema
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr/td/input').click() #clica em 'processa'
            # ACESSA TELA DE EXPEDIÇÃO

        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[9]/a').click() #clica no botão 'expedição'

        if Tracking.dist == 1:  # número de série da NF
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('3')

        if Tracking.dist == 2:
            Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('4')
        # importa lista com as nfs/dtas entrega que deverão ser lançadas
        c = 1
        cont_nfs_expedidas = 0
        for nf, data in tracking.items():
            # critica = navegador.find_element('xpath', '/html/body/form[2]/div[2]/text()') >  esta linha está com erro. o objetivo é mostrar a critica
            # caso já exista data  lan  çada, ou se a data de entrega é menor do que a data  de expedição.
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

    def acessa_tela_tracking(self):
        print('Classe: Intranet, Método: acessa_tela_tracking')

        Intranet.navegador.get('http://45.236.77.106:51236/intranet/login.php?Width1=1366&Height1=768')

        # fazer  login

        Intranet.navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys(
            'jean.lino')
        Intranet.navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
            'Ma250509')
        Intranet.navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(
            Keys.ENTER)

        # acessar 'Customer Services'
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/a').click()
        # input('>>>')
        # acessar Tracking
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/ul/a[1]').click()
        #1 > Extrema 2 > Alhandra
        if Tracking.dist == 2:
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(
                Keys.ARROW_DOWN)
        if Tracking.dist == 1:
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
        # Intranet.navegador.find_element('xpath','/html/body/form[2]/table[3]/tbody/tr/td[1]/input').click()
    def acessa_tela_atualizar_entrega(self):
        print('Classe: Intranet, Método: acessa_tela_atualizar_entrega')
        tracking = Tracking.importa_data_entrega(self=Tracking)

        # # acessar 'Customer Services'

        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/a').click()
        Intranet.navegador.find_element('xpath', '//*[@id="navigation"]/ul/li[4]/ul/a[5]').click()
        # ACESSAR BS DISTRIBUIDORA (bne: arrow up, bs-alhandra: arrow down  bs: arrow down 2x)
        if Tracking.dist == 3:  # bs-alhandra
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
        if Tracking.dist == 1:  # bs-extrema
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[2]/tbody/tr/td/input').click()
        # ACESSA A TELA 'ENTREGA'
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[10]/a').click()
        # número de série da NF
        if Tracking.dist == 1:
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('3')
        if Tracking.dist == 2:
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/input').send_keys('4')
        #importa lista com as nfs/dtas entrega que deverão ser lançadas
        c = 1
        cont_nfs_entregues = 0
        for nf, data in tracking.items():
            # critica = navegador.find_element('xpath', '/html/body/form[2]/div[2]/text()') >  esta linha está com erro. o objetivo é mostrar a critica
            # caso já exista data  lançada, ou se a data de entrega é menor do que a data  de expedição.
            print(f'{c} - {nf}: {data} ')

            data = data.replace("/", "")
            c += 1

            # INSERIR UMA LINHA PARA CASO JÁ HAJA DATA DE ENTREGA LANÇADA, NÃO SOMAR NO TOTAL
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/input').send_keys(nf)

            # data de entrega
            Intranet.navegador.find_element('xpath', '//*[@id="calendario1"]').send_keys(data)

            #  grava
            Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/input').send_keys(Keys.ENTER)
            cont_nfs_entregues += 1

        print(f'{cont_nfs_entregues} datas lançadas')

    def gera_lista_nfs_nao_entregues(self):
        print('Classe: Intranet, Método: gera_lista_nfs_nao_entregues')
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()
        Intranet.navegador.find_element('xpath',
                                        '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[3]').click()
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

        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[3]/tbody/tr/td[1]/input').send_keys(
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

    def gera_lista_nfs_nao_expedidas():
        print('Classe: Intranet, Método: gera_lista_nfs_nao_expedidas')
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click() # FILTRA NFS NAO expedidas

        Intranet.navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[2]').click() # opção nao expedidos


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
        Intranet.navegador.find_element('xpath', '/html/body/form[2]/table[3]/tbody/tr/td[1]/input').send_keys(Keys.ENTER)
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
                nfs_nao_expedidas.append(nf)# insere na lista
        #
        except:
            print(f"{tr - 2} NF'S nao expedidas")
            print(f'Lista > {nfs_nao_expedidas}')
        return nfs_nao_expedidas

    def atualiza_entrega(self):
        print('Classe: Intranet, Método: atualiza_entrega')

        # listar nfs nao entregues
        print('Intranet.gera_lista_nfs_nao_entregues(self)')
        Intranet.gera_lista_nfs_nao_entregues(self) # FUNCIONANDO

        # buscar datas de entrega na planilha
        # retornar dicionario
        print('Tracking.importa_data_entrega(self)')
        Tracking.importa_data_entrega(self) # funcionando

class Analise:
    pass

if Tracking.processo == 1:
    Tracking.importa_data_expedicao(self=Tracking)

if Tracking.processo == 2:
    Tracking.importa_data_agenda(self=Tracking)

if Tracking.processo == 3:
    Tracking.importa_data_entrega(self=Tracking)


if Tracking.processo == 4:
    Intranet.acessa_tela_tracking(self=Intranet)
    Intranet.gera_lista_nfs_nao_entregues(self=Intranet)

if Tracking.processo == 5:
    Intranet.acessa_tela_tracking(self=Intranet)
    Intranet.gera_lista_nfs_nao_expedidas()

if Tracking.processo == 6:

    Intranet.acessa_tela_atualizar_entrega(self=Intranet)
    
if Tracking.processo == 7:
    Intranet.acessa_tela_atualizar_expedicao(self=Intranet)

if Tracking.processo == 8:
    if Tracking.dist == 1:  # Extrema
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\TRACKING NE-BS-2023.xlsx',
                           sheet_name='BASE TRACKING 2023')  # tracking EXTREMA

    else:  # Alhandra
        df = pd.read_excel('G:\Drives compartilhados\CUSTOMER SERVICE\AREA 02 NE\Tracking BNE - 2023.xlsx',
                           sheet_name='BASE TRACKING 2023')  # tracking ALHANDRA
    pass


    #atualiza dta de expedição (somente Alhandra)

# email alerta de nf em transito
# email sobre entrega em d+1
# email de confirmação se entrega está em trânsito