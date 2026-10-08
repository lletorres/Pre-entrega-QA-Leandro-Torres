from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def realizar_login(driver):
    """Función de apoyo para loguearse rápidamente."""
    # Declaramos el wait DENTRO de la función usando el driver que pasamos por parámetro
    wait = WebDriverWait(driver, 10)
    
    driver.get("https://www.saucedemo.com/")
    wait.until(EC.visibility_of_element_located((By.ID, "user-name"))).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()