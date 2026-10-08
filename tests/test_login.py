import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login_helper import realizar_login

def test_login():
   driver = webdriver.Chrome()
   wait = WebDriverWait(driver, 10)
   try:
     #Navegacion y login
     realizar_login(driver)
  
     #Validaciones
     wait.until(EC.url_contains("/inventory.html"))
     # Esperamos explícitamente a que el logo sea visible en pantalla y extraemos su texto
     titulo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "app_logo"))).text
     assert titulo == "Swag Labs"

     Subtitulo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test='title']"))).text
     assert Subtitulo == "Products"
   finally:
     driver.quit()   
