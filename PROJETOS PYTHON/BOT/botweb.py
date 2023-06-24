from selenium import webdriver  # permite criar a janela
# import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager

from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
cont_tec = 0
cont_arc = 0
# navegador.get('http://www.tecsigma.com.br')
while True:
    navegador = webdriver.Chrome(service=servico, options=options)
    # navegador = webdriver.Chrome(service=servico)
    # navegador.set_window_size(1,1)
    # navegador.minimize_window()
    # navegador.maximize_window()
    navegador.get('http://www.tecsigma.com.br')
    navegador.find_element('xpath','//*[@id="page"]/div[1]').click() #anuncio 1
    # navegador.find_element('xpath', '//*[@id="page"]/div[2]').click() #  anuncio2
    cont_tec +=1
    print(f'cont_tec{cont_tec}')
    # sleep(10.0)
    # navegador.refresh()
    # sleep(3.0)
    # navegador.get('http://www.arcaboucoliterario.com.br')
    # cont_arc +=1
    # print(f'cont_arc{cont_arc}')
    # # sleep(2.0)
    # navegador.refresh()
    navegador.close()

