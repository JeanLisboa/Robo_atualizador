
import pandas as pd
import pywhatkit
import keyboard
import time
from datetime import datetime

df = pd.read_excel('G:/Drives compartilhados/CUSTOMER SERVICE/AREA 02 NE/Tracking BNE - 2023.xlsx', sheet_name='BASE TRACKING 2023') # tracking bne

relatorio = df.loc[df['STATUS'] != 'ENTREGUE', ["VEND","DOC","CLIENTE","DESTINATÁRIO","MUNICIPIO","VOLUME","Agend","PREVISÃO ENTREGA","OBS","D+"]]
rel = relatorio.loc[relatorio['Agend'] == 's', ["VEND","DOC","CLIENTE","DESTINATÁRIO","MUNICIPIO","VOLUME","Agend","D+","PREVISÃO ENTREGA","OBS"]]

a = '000671 MARLEI'
b = '000508 JEANY'
c = '000595 GUALTER'
d = '000656 FLAVIO'
e = '000641 LUCIA'
f = '000502 CLEBER'
g = '000654 PAULO BESERRA'
vend = str(input('vendedor: '))
cod_vend = ''
if vend == 'a':
    cod_vend = '000671 MARLEI'
if vend == 'b':
    cod_vend = '000508 JEANY'
if vend == 'c':
    cod_vend = '000595 GUALTER'
if vend == 'd':
    cod_vend = '000656 FLAVIO'
if vend == 'e':
    cod_vend = '000641 LUCIA'
if vend == 'f':
    cod_vend = '000502 CLEBER'
if vend == 'g':
    cod_vend = '000654 PAULO BESERRA'



relatorio2 = rel.loc[rel['VEND'] == cod_vend,["D+","Agend","VEND","DOC","DESTINATÁRIO","MUNICIPIO","VOLUME","PREVISÃO ENTREGA","OBS"]]


# rel2 = relatorio2.loc[relatorio2["D+"] == 3, ["D+","DOC","Agend","DESTINATÁRIO","VOLUME","PREVISÃO ENTREGA"]]
# relatorio3 = rel2[["D+","DOC","Agend","DESTINATÁRIO","VOLUME","PREVISÃO ENTREGA"]]
relatorio3 = relatorio2[["D+","DOC","Agend","DESTINATÁRIO","MUNICIPIO","VOLUME","PREVISÃO ENTREGA","OBS"]]

# msg_ini_manha = ['Bom dia','Tenha um Ótimo Dia!']
# msg_ini_tarde = ['Boa tarde', "Ótima tarde"]
# seq_atendimento = ['Como posso te Ajudar ?']

# relatorio3 = rel[["D+","DOC","Agend","DESTINATÁRIO","VOLUME","PREVISÃO ENTREGA"]]

rel3 = relatorio3[["DOC","DESTINATÁRIO","OBS"]]
rel3.columns = ['DOC','DEST',"OBS"]


rel3 = rel3.dropna(axis=0) # exclui as colunas com valores vazios


# rel3.set_index(['DOC'], inplace=True, drop=True) # usa a coluna doc como indice
# relatorio3.sort_values(by=["DOC"],ascending=False) # classifica pela coluna d+
print(rel3)
msg = "Olá familia!!!"
    #
    # cont = 0
    # dicionario = {}
    # for d, doc in rel3:
    #
    #     dicionario_temp = {d: doc } #transforma o set em dict
    #     dicionario.update(dicionario_temp) #copia o dicionario_temp dentro do dict definitivo
    #     print(dicionario_temp)
    #     dicionario_temp.clear() #limpa o dicionario temp
    #     cont += 1
    # print(f'\n {cont} previsões de entrega localizadas')

    # print(dicionario)

contatos = ['+5583993637279','+5583991852537']
cont_familia = ['+5583993637279','+5583999558920','+5583994441587','+5583991382228']
#
pywhatkit.sendwhatmsg_instantly(phone_no='+5583993637279',wait_time=15,tab_close=False,close_time=3,message=msg)
# while len(cont_familia) >= 0:
#     pywhatkit.sendwhatmsg(cont_familia[0],f'{msg}', datetime.now().hour,datetime.now().minute + 1)
#
#     del cont_familia[0]
#     print(msg)

    # keyboard.press_and_release('enter')
    #
    #
    #
    #
    #
    #
    # del contatos[0]
    # time.sleep(1)
    # keyboard.press_and_release('ctrl + w')

