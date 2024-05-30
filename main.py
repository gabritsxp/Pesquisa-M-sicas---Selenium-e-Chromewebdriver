from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def get_lyrics(song_name):
    # Inicializa o driver do Chrome
    driver = webdriver.Chrome()
    # Acesse o site de letras de músicas
    driver.get("https://www.letras.com.br/")

        # Clique no ícone da lupa para ativar o campo de busca
    search_icon = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "search-component-button"))
        )
    search_icon.click()
    
    # Aguarde até que a barra de pesquisa esteja presente e seja interagível
    search_box = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='search-input']"))
    )
        
        # Pesquise pela música desejada
    search_box.send_keys(song_name)
    search_box.send_keys(Keys.RETURN)

    # Aguarde os resultados da busca serem carregados
    time.sleep(5)

    # Aguarde até que o primeiro resultado da pesquisa esteja presente e seja interagível
    first_result = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'item-box item-list')]"))
    )

    # Clique no primeiro resultado
    first_result.click()

    # Aguarda a página da letra ser carregada
    time.sleep(5)

    # Encontra e imprime a letra da música
    letra = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, "//section[contains(@class, 'lyrics-section')]"))
    )
    print(letra.text)


    # Fecha o driver
    driver.quit()

# Busca pela letra da música "Imagine" de John Lennon
get_lyrics('Hotel California')

#necessário instalar o chromewebdriver, python e selenium