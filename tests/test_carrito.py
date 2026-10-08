import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.login_helper import realizar_login

def test_carrito():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    try:
        realizar_login(driver)
        
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        nombre_producto_esperado = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        
        # Agregar el primer producto
        btn_agregar = productos[0].find_element(By.TAG_NAME, "button")
        btn_agregar.click()
        
        # Verificar incremento del contador
        badge_carrito = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge_carrito == "1", "El contador del carrito no se incrementó a 1."
        
        # Navegar al carrito y validar
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        wait.until(EC.url_contains("/cart.html"))
        nombre_producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        assert nombre_producto_carrito == nombre_producto_esperado
    finally:
        driver.quit()