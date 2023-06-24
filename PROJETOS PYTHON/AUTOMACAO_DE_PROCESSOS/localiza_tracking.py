# altera formato de data
def formata_data():
    from datetime import date, datetime

    data = datetime.strptime('26/08/2018', '%d/%m/%Y').date()

    print(data)

    dataFormatada = data.strftime('%d/%m/%Y')

    print(dataFormatada)
    return dataFormatada

# --------------------------------
# renomeia arquivo
import datetime
import time
def renomeia_arquivo():

    from datetime import date
    import time
    data = date.today()
    hora = time.ctime()
    import os
    os.rename('C:/Users/User/Downloads/rel_entregas.xls', f'C:/Users/User/Downloads/Relatorio_TSI_{data.year}_{data.month}_{data.day}.xls') # usar barras normais

# ---------------------------------

# - lista arquivos

def localiza_tracking():

    import os

    pasta = 'G:/Meu Drive/TRACKING-EMAIL/2023'
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            print(os.path.join(diretorio, arquivo))
            # print(os.path.join(arquivo))

    tracking = os.path.join(diretorio,arquivo)

    return tracking

# -------------------------------------
# CONTA MINUTOS E SEGUNDOS

import datetime
from time import sleep


while True:
    now = datetime.datetime.now()
    print(now.minute, now.second)
    if now.second % 10 == 0:
        print('atualizar programa')



    sleep(1)
