from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#ABRE EL NAVEGADOR
driver = webdriver.Firefox()
#ABRE UNA PÁGINA
driver.get("https://pixabay.com/es/")
time.sleep(1)
buscar = driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/div[3]/div[1]/div/form/input")
buscar.send_keys("paisajes")
time.sleep(2)
buscar.send_keys(Keys.ENTER)
#TIEMPO DE ESPERA
time.sleep(3)
#Mover espacios
#imagenes = driver.find_elements(By.XPATH, '//img')
#urlImagenes= [imagen.get_attribute('src') for imagen in imagenes]
imagenes = driver.find_elements(By.XPATH, '//img')
data=[]
for imagen in imagenes:
    #print(imagen.get_attribute('src'))
    data.append(imagen.get_attribute('src'))

time.sleep(1)

urlImagenes=[]
for pagina in range(4):
    imagenes = driver.find_elements(By.XPATH, '//img')
    urlImagenes= [imagen.get_attribute('src') for imagen in imagenes]
    time.sleep(1)
    if pagina == 0:
        boton = driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div/div[2]/div[4]/div[1]/a/span[2]')
    else:
        boton = driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[2]/div[4]/div[1]/a[2]/span[2]')    
    boton.click()
    time.sleep(5)

for item in urlImagenes:
    print(item)
    
#CERRAR LA PÁGINA
driver.close()