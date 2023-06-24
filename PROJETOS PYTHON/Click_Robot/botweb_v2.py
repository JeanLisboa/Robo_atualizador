from selenium import webdriver  # permite criar a janela
# import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager

from selenium.webdriver.chrome.service import Service
from time import sleep

servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
# options.add_argument("--headless=new")
cont_tec = 0
cont_arc = 0
# navegador.get('http://www.tecsigma.com.br')
while True:
    navegador = webdriver.Chrome(service=servico, options=options)
    navegador.get('http://www.tecsigma.com.br')
    for click in range(0,10):
        navegador.find_element('xpath','//*[@id="page"]/div[1]').click() #anuncio 1
        sleep(0.2)
        navegador.find_element('xpath','//*[@id="banner"]/div[1]/a/canvas').click() #anuncio 2
        navegador.find_element('xpath','//*[@id="page"]/div[1]').click()  #anuncio 3
    cont_tec +=1
    print(f'cont_tec{cont_tec}')
    navegador.close()

