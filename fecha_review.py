from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os

# Inicializar Selenium
driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")

# URL base
base_url = 'https://www.tripadvisor.es/Hotel_Review-g662606-d285140-Reviews-or'
base_url2= '-Iberostar_Selection_Anthelia-Costa_Adeje_Adeje_Tenerife_Canary_Islands.html'

# Número de página inicial
pagina = 0
fecha_comentario = []

while True:
    # Crear la URL completa
    url_completa = base_url + str(pagina) + base_url2

    # Navegar a la URL
    driver.get(url_completa)

    # Obtener el contenido de la página
    contenido = driver.page_source

    # Parsear el contenido con BeautifulSoup
    soup = BeautifulSoup(contenido, 'html.parser')

    # Extraer la información que necesites de la página utilizando bs4
    
    comentarios = soup.find_all('div',class_="cRVSd")
    for comentario in comentarios:
        review=comentario.find('span').getText()
        fecha_comentario.append(review)
    
    
    # Verificar si hay una siguiente página
    siguiente_pagina = soup.find('a', text='Siguiente')

    mi_path = r"C:\Users\Usuario\Desktop\Nueva carpeta\fecha_opiniones-Anthelia.txt"
    f = open(mi_path, 'a+', encoding="utf-8")

    if siguiente_pagina:
        # Incrementar el número de página para la siguiente iteración
        for i in fecha_comentario:
            f.write(str(i) + '\n')
            
        pagina += 5
    else:
        # No hay más páginas, salir del bucle
        break
    

driver.quit()




