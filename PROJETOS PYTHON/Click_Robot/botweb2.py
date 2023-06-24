#rola a pagina até o final e clica no anuncio
import datetime

from selenium import webdriver  # permite criar a janela
# import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import webdriver_manager

from selenium.webdriver.chrome.service import Service
from time import sleep

#codigo para testar o scrool
servico = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
cont_tec = 0
cont_arc = 0
while True:
    navegador = webdriver.Chrome(service=servico, options=options)
    navegador.get('http://www.tecsigma.com.br')

    # sleep(2.0)
    navegador.refresh()
    cont_a = 1
    cont_b =0
    for contador in range(0,100):
        last_height = navegador.execute_script("return document.body.scroll.Height")
        navegador.execute_script(f"window.scrollTo({cont_b},{cont_a});")
        cont_b = cont_a
        cont_a += 50
        # sleep(0.2)

        new_height = navegador.execute_script("return document.body.scrollHeight")
        sleep(0.3)
        if new_height == last_height:
            navegador.find_element('xpath', '//*[@id="page"]/div[1]').click()
            # //*[@id="page"]/div[1]
            #//*[@id="page"]/div[1]/ins
            #//*[@id="banner"]/div[1]
            #//*[@id="banner"]/div[1]/a
            #//*[@id="banner"]/div[1]/a/canvas
            #//*[@id="bannerB"]
            #//*[@id="mys-wrapper"]
            #//*[@id="mys-content"]
            #//*[@id="mys-content"]/div[2]
            #
            #
            #



            break
        last_height = new_height
    cont_tec +=1

    print(f'cont_tec{cont_tec}')
    navegador.close()

    navegador = webdriver.Chrome(service=servico, options=options)
    navegador.get('http://www.tecsigma.com.br')

    # sleep(2.0)
    navegador.refresh()
    cont_a = 1
    cont_b = 0
    for contador in range(0, 100):
        last_height = navegador.execute_script("return document.body.scroll.Height")
        navegador.execute_script(f"window.scrollTo({cont_b},{cont_a});")
        cont_b = cont_a
        cont_a += 50
        # sleep(0.2)

        new_height = navegador.execute_script("return document.body.scrollHeight")
        sleep(0.3)
        if new_height == last_height:
            navegador.find_element('xpath', '//*[@id="page"]/div[1]').click()
            # //*[@id="page"]/div[1]
            # //*[@id="page"]/div[1]/ins
            # //*[@id="banner"]/div[1]
            # //*[@id="banner"]/div[1]/a
            # //*[@id="banner"]/div[1]/a/canvas
            # //*[@id="bannerB"]
            # //*[@id="mys-wrapper"]
            # //*[@id="mys-content"]
            # //*[@id="mys-content"]/div[2]
            #
            #
            #

            break
        last_height = new_height
    cont_tec += 1

    print(f'cont_tec{cont_tec}')
    navegador.close()


