
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
# relatorio3 = rel[["D+","DOC","Agend","DESTINATÁRIO","VOLUME","PREVISÃO ENTREGA"]]

rel3 = relatorio3[["DOC","DESTINATÁRIO","PREVISÃO ENTREGA"]]
rel3.columns = ['DOC','DEST',"PREVISAO"]


# rel3 = rel3.dropna(axis=0) # exclui as colunas com valores vazios



rel3.set_index(['DOC','DEST',], inplace=True, drop=True) # usa a coluna doc como indice
# relatorio3.sort_values(by=["DOC"],ascending=False) # classifica pela coluna d+
print(rel3)

contatos = ['+5583993637279','+5583994441587']

for p in contatos:
    pywhatkit.sendwhatmsg_instantly(phone_no = p,wait_time=13,tab_close=True,close_time=3,message=f'{rel3}')
    print(p)

