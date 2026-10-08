import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.login_helper import realizar_login

def test_catalogo():
    driver = webdriver.Chrome()

    try: 
        realizar_login(driver)

        # Validacion titulo pestaña
       
        assert driver.title == "Swag Labs"

        # Validacion cantidad de productos
        productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Cantidad de productos encontrados: {len(productos)}")
        assert len(productos) > 0, "No se encontraron productos en el catálogo."

        # Lista nombre/precio del primero
        primer_nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        primer_precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
        print(f"Primer producto: {primer_nombre} - Precio: {primer_precio}")
        assert primer_nombre == "Sauce Labs Backpack"
        assert primer_precio == "$29.99"

        # Validación de elementos importantes de la interfaz
        menu_hamburguesa = driver.find_element(By.ID, "react-burger-menu-btn")
        filtro_orden = driver.find_element(By.CLASS_NAME, "product_sort_container")
        assert menu_hamburguesa.is_displayed(), "El menú principal no está visible."
        assert filtro_orden.is_displayed(), "El filtro de productos no está visible."
    finally:
        driver.quit()    