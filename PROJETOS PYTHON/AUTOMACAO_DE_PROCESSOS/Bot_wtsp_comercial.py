import pandas as pd
import pywhatkit
df = pd.read_excel('G:/Drives compartilhados/CUSTOMER SERVICE/AREA 02 NE/Tracking BNE - 2023.xlsx', sheet_name='BASE TRACKING 2023') # tracking bne

relatorio = df.loc[(df['STATUS'] != 'ENTREGUE')& (df['STATUS'] != 'DEVOLUÇÃO'), ["VEND","DOC","CLIENTE","DESTINATÁRIO","MUNICIPIO","VOLUME","Agend","PREVISÃO ENTREGA","OBS","D+"]]
rel = relatorio.loc[relatorio['Agend'] == 's', ["VEND","DOC","CLIENTE","DESTINATÁRIO","MUNICIPIO","VOLUME","Agend","D+","PREVISÃO ENTREGA","OBS"]]

a = 'Bom dia Marlei, tudo bem ?'
contatos_a = ['+5581994447916','+5583993228395']

b = 'Bom dia Jeany, tudo bem ? '
contatos_b = ['','+5583993228395']

c = 'Bom dia Gualter, tudo bem ? '
contatos_c = ['','+5583993228395']

d = 'Bom dia Flávio, tudo bem ? '
contatos_d = ['','+5583993228395']

e = 'Bom dia Lúcia, tudo bem ? '
contatos_e = ['','+5583993228395']

f = 'Bom dia Cléber, tudo bem ? '
contatos_f = ['','+5583993228395']

g = 'Bom dia Paulo, tudo bem ? '
contatos_g = ['','+5583993228395']

print('(a)Marlei | (b)Jeany | (c)Gualter | (d)Flávio | (e)Lúcia | (f)Cléber | (g)Paulo')
vend = str(input('Informe o Vendedor: '))


# vend = 'a'
if vend == 'a':
    cod_vend = '000671 MARLEI'
    msg_vend = a
if vend == 'b':
    cod_vend = '000508 JEANY'
    msg_vend = b
if vend == 'c':
    cod_vend = '000595 GUALTER'
    msg_vend = c
if vend == 'd':
    cod_vend = '000656 FLAVIO'
    msg_vend = d
if vend == 'e':
    cod_vend = '000641 LUCIA'
    msg_vend = e
if vend == 'f':
    cod_vend = '000502 CLEBER'
    msg_vend = f
if vend == 'g':
    cod_vend = '000654 PAULO BESERRA'
    msg_vend = g
relatorio2 = rel.loc[rel['VEND'] == cod_vend,["D+","Agend","VEND","DOC","DESTINATÁRIO","MUNICIPIO","VOLUME","PREVISÃO ENTREGA","OBS"]]
relatorio3 = relatorio2[["D+","DOC","Agend","DESTINATÁRIO","MUNICIPIO","VOLUME","PREVISÃO ENTREGA","OBS"]]
rel3 = relatorio3[["DOC","DESTINATÁRIO","OBS"]]
rel3.columns = ['DOC','DEST',"OBS"]
# rel3['PREVISÃO ENTREGA'] = pd.to_datetime(rel3['PREVISÃO ENTREGA'], format='%d/%m/%Y')
rel3 = rel3.dropna(axis=0) # exclui as colunas com valores vazios
# rel3.set_index(['DOC','DEST'], inplace=True, drop=True) # usa a coluna doc como indice

#marlei +5581994447916

for i in rel3.head(100).iterrows():
    print(f"{i[1]['DOC']:<4} {i[1]['DEST']:.<33} {i[1]['OBS']:.>20}")


#
# for p in contatos:
#     pywhatkit.sendwhatmsg_instantly(phone_no=p, wait_time=13, tab_close=True, close_time=3,message=f'{msg_vend},\n Seguem informações: \n')
#
#     for i in rel3.head(100).iterrows():
#
#         pywhatkit.sendwhatmsg_instantly(phone_no = p,wait_time=13,tab_close=True,close_time=3,message=(f"{i[1]['DOC']:<4} {i[1]['DEST']:.<33} {i[1]['OBS']:.>20}"
#                                                                                                        f""))
#     print(p)

#



# for p in contatos:
#
#     pywhatkit.sendwhatmsg_instantly(phone_no = p,wait_time=13,tab_close=True,close_time=3,message=f'{rel3}')
#
#     print(p)