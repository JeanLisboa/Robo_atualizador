from selenium import webdriver #permite criar a janela
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from AUTOMACAO_DE_PROCESSOS.ANTIGOS import importa_dt_agenda

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
# navegador.minimize_window()

dic_mes_faturamento = {'jan':'01',
                   'fev':'02',
                   'mar':'03',
                   'abr':'04',
                   'mai':'05',
                   'jun':'06',
                   'jul':'07',
                   'ago':'08',
                   'set':'09',
                   'out':'10',
                   'nov':'11',
                   'dez':'12'
                   } # dicionário de meses
print()
print('* ' *30)
print()
print('* * * * * * Atualiza Data De Agenda * * * * * *')

dist = (int(input('Distribuidor: BS(1) /BNE(2): ')))
if dist == 1:
    # este if só se aplica para a opção dist = 'bs'
    reg = str(input('Digite "2" para atualizar somente a  R-02 \n'
                    'ou pressione ENTER para atualizar todos: '))
else:
    pass
#mes = int(input('mês 01 - 12: '))
mes = dic_mes_faturamento[str(importa_dt_agenda.mes)]
ano = int(input('Ano: '))



def acessa_tela_agendamento():

    # abrir intranet
    # navegador.minimize_window()

    navegador.get('http://45.236.77.106:51236/intranet/login.php?Width1=1366&Height1=768')

    # fazer  login

    navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input').send_keys('jean.lino')
    navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys('Ma250509')
    navegador.find_element('xpath','/html/body/form/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input').send_keys(Keys.ENTER)

    # seleciona o módulo logistica
    navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys('L')
    navegador.find_element('xpath', '/html/body/form/table/tbody/tr[2]/td[2]/select').send_keys(Keys.ENTER)

    #acessar 'Logística'
    navegador.find_element('xpath','//*[@id="navigation"]/ul/li[2]/a').click()

    #acessar pedidos otc
    navegador.find_element('xpath','//*[@id="navigation"]/ul/li[2]/ul/a[3]').click()

    #ACESSAR BS DISTRIBUIDORA (bne: arrow up,  bs: arrow down)

    if dist == 1:
        navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_DOWN)
    if dist == 2:
        navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[1]/select').send_keys(Keys.ARROW_UP)

    #ACESSAR FILTRO 'AGENDAMENTO'
    navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select').click()
    #selecionar opção 'agendamento'
    navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[2]/select/option[6]').click()

    #selecionar o mês
    # outubro - >  option[10]
    navegador.find_element('xpath','/html/body/form[2]/table[1]/tbody/tr[2]/td[3]/select').click()

    #seleciona o ano
    navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[4]/select').send_keys(f'{ano}')
    navegador.maximize_window()
    # seleciona o mês
    navegador.find_element('xpath',f'/html/body/form[2]/table[1]/tbody/tr[2]/td[3]/select/option[{mes}]').click()
    # selecion a regiao


    if dist == '1' and reg == '2':
        navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(Keys.ARROW_DOWN)
        navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(Keys.ARROW_DOWN)
        navegador.find_element('xpath', '/html/body/form[2]/table[1]/tbody/tr[2]/td[8]/select').send_keys(Keys.ENTER)

    else:
        pass

    #processa
    navegador.find_element('xpath','/html/body/form[2]/table[2]/tbody/tr/td/input').send_keys(Keys.ENTER)


tracking = importa_dt_agenda.dicionario

acessa_tela_agendamento()  #função
cont_tr = 1
c = 0
cont_agenda_incluida = 0

try:

    while c <2000:
        for i in tracking:
            print(f'Analisando linha {cont_tr} | pedido {i}')
            nome = navegador.find_element('xpath', f'/html/body/form[2]/table[3]/tbody/tr[{cont_tr}]/td[1]/input').get_dom_attribute('name')
            if nome == f'marcacao_agenda[{i}]':
                print(f'> Pedido {i} - agendado para {tracking[i]}')
                navegador.find_element('xpath', f'/html/body/form[2]/table[3]/tbody/tr[{cont_tr}]/td[1]/input').send_keys(tracking[i]) # ok
                cont_agenda_incluida += 1



        c += 1
        cont_tr += 1
except:
    print('Verificação finalizada')
finally:
    print(f'{cont_tr} pedidos verificados.\n'
          f'{cont_agenda_incluida} agendas incluídas. ')
    navegador.find_element('xpath', '/html/body/form[2]/div[2]/input').click()


