from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def setup_driver():
    """Configura y devuelve una instancia del WebDriver de Chrome lista para usar/reutilizar."""

# 1. Configuramos las opciones de Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized") # Abre el navegador maximizado
    
    # (Opcional) Si tuvieras problemas en la terminal, podés descomentar estas líneas:
    # chrome_options.add_argument("--no-sandbox")
    # chrome_options.add_argument("--disable-dev-shm-usage")

    # 2. Creamos el servicio (Selenium 4 lo maneja automáticamente)
    service = Service()
    
    # 3. Inicializamos el driver con nuestras opciones
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    # 4. Le damos una espera implícita global de 5 segundos como red de seguridad
    driver.implicitly_wait(5)
    
    return driver