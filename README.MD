# 🚀 Pre-Entrega QA Automation - Talento Tech

**Alumno:** Leandro Torres
**Sitio de Pruebas:** [Sauce Demo](https://www.saucedemo.com/)

Este repositorio contiene la pre-entrega obligatoria del curso de Automation Testing. El proyecto consiste en un framework de pruebas automatizadas UI utilizando **Python, Selenium WebDriver y Pytest**, aplicando buenas prácticas de modularización y manejo de esperas (implícitas y explícitas).

## 📁 Arquitectura del Proyecto

El código está estructurado de forma modular para separar la configuración, las funciones de apoyo y los casos de prueba:

- **`tests/`**: Contiene los casos de prueba ejecutables e independientes.
  - `test_login.py`: Validación de inicio de sesión y redirección.
  - `test_catalogo.py`: Verificación de interfaz y presencia de productos.
  - `test_carrito.py`: Flujo de agregado de productos y validación del carrito.
- **`utils/`**: Contiene módulos reutilizables (Principio DRY).
  - `login_helper.py`: Función de apoyo con esperas explícitas para automatizar el login en pruebas secundarias.

- **`reports/`**: Directorio donde se generan los reportes de ejecución en formato HTML.
- **`pytest.ini`**: Archivo de configuración básica de Pytest.

## ⚙️ Requisitos Previos

Para ejecutar este proyecto, necesitas tener instalado Python 3 y las siguientes librerías:

```bash
pip install selenium pytest pytest-html
```

## ▶️ Cómo ejecutar las pruebas

El proyecto está configurado mediante `pytest.ini` para organizar la ejecución y generar los reportes automáticamente. Para correr todos los casos de prueba (Login, Catálogo y Carrito) y compilar la evidencia de los resultados, ejecuta el siguiente comando estando posicionado en la raíz del proyecto:

```bash
python3 -m pytest
```

Al finalizar la ejecución en la consola, el framework generará automáticamente un archivo llamado `reporte.html` dentro de la carpeta reports/. Puedes abrir este archivo con cualquier navegador web para visualizar el estado detallado (PASSED/FAILED) de cada una de las pruebas.
