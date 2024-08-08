from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("http://localhost:4200/formulario")
time.sleep(5)
data = [
    {
        "id":"1",
        "nombre": "Denis",
        "apellido": "Chasipanta",
        "email": "dchasipanta@gmail.com"
    },
    {
        "id":"2",
        "nombre": "Jonathan",
        "apellido": "Chasipanta",
        "email": "jchasipanta09@gmail.com"
    },
    {
        "id":"1",
        "nombre": "Segundo",
        "apellido": "Chasipanta",
        "email": "sechasi@gmail.com"
    }
]

for item in data:
    campoID= driver.find_element(By.XPATH,"/html/body/app-root/app-form/div/form/input[1]")
    campoID.send_keys(item["id"])
    campoNombre= driver.find_element(By.XPATH,"/html/body/app-root/app-form/div/form/input[2]")
    campoNombre.send_keys(item["nombre"])
    campoApellido= driver.find_element(By.XPATH,"/html/body/app-root/app-form/div/form/input[3]")
    campoApellido.send_keys(item["apellido"])
    campoEmail= driver.find_element(By.XPATH,"/html/body/app-root/app-form/div/form/input[4]")
    campoEmail.send_keys(item["email"])
    time.sleep(1)
    boton = driver.find_element(By.XPATH,'/html/body/app-root/app-form/div/form/button')
    boton.click()
    time.sleep(5)

while True:
    try:
        botonEliminar = driver.find_element(By.XPATH, "/html/body/app-root/app-form/app-tabla/table/tbody/tr[1]/td[5]/button")
        botonEliminar.click()
        time.sleep(1)
    except:
        print("Todos los elementos han sido eliminados.")
        break