
def localiza_tracking():

    import os

    pasta = 'G:/Meu Drive/TRACKING-EMAIL/2023'
    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            print(os.path.join(diretorio, arquivo))
            # print(os.path.join(arquivo))

    tracking = os.path.join(diretorio,arquivo)

    return tracking

localiza_tracking()