from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.google.com")

time.sleep(1)

buscar = driver.find_element(By.XPATH,'//*[@id="APjFqb"]')
buscar.send_keys("Angular")
buscar.send_keys(Keys.ENTER)

time.sleep(2)

## Deslizar mediante Scroll

mover = 3

for m in range(mover):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
