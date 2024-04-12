# Guía de Pruebas Automatizadas

Este documento proporciona una guía paso a paso sobre cómo realizar pruebas automatizadas para la funcionalidad de eliminación de usuarios en una aplicación web.

## Requisitos Previos

- Python 3.x instalado en tu sistema.
- Selenium WebDriver instalado y configurado.
- Navegador compatible con Selenium (por ejemplo, Chrome, Firefox).
- Acceso a la aplicación web y conocimiento de la URL de la página de eliminación de usuarios.

## Configuración del Entorno de Pruebas

Antes de comenzar, asegúrate de que todos los requisitos previos estén instalados y configurados correctamente. Esto incluye tener el WebDriver correspondiente al navegador que deseas utilizar.

## Estructura del Proyecto

Tu proyecto de pruebas automatizadas puede tener la siguiente estructura de carpetas:

-----------------------------------------
proyecto_pruebas_automatizadas/ │ ├── drivers/ # Carpeta donde se almacenan los WebDriver. ├── tests/ # Carpeta donde se almacenan los scripts de pruebas. │ └── test_eliminar_usuario.py └── README.md # Este archivo.
----------------------------------------

## Script de Prueba

El script `test_eliminar_usuario.py` contiene el código necesario para ejecutar la prueba automatizada. A continuación se muestra un ejemplo de cómo podría ser el script:

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializa el WebDriver para Chrome
driver = webdriver.Chrome('./drivers/chromedriver')

try:
    # Navega a la página de inicio de sesión
    driver.get('http://localhost/login')

    # Inicia sesión en la aplicación (reemplaza con tus propios métodos de inicio de sesión)
    # ...

    # Navega a la página de lista de usuarios
    driver.get('http://localhost/admin/usuarios')

    # Encuentra y hace clic en el botón de eliminar para el usuario específico
    # ...

    # Confirma la eliminación del usuario
    # ...

finally:
    # Cierra el navegador después de la prueba
    driver.quit()


Ejecución de la Prueba
Para ejecutar la prueba, navega a la carpeta del proyecto y ejecuta el script con Python:

python tests/test_eliminar_usuario.py


Resultados de la Prueba
Después de ejecutar el script, observa la ejecución automatizada en el navegador y verifica que los resultados sean los esperados. Si el usuario se elimina correctamente, la prueba ha pasado. De lo contrario, revisa los pasos y asegúrate de que todos los elementos de la interfaz de usuario se estén identificando correctamente.

Notas Adicionales
Asegúrate de que las pruebas se ejecuten en un entorno de prueba y no en producción.
Realiza copias de seguridad de la base de datos antes de ejecutar pruebas que modifiquen datos.
Mantén tus credenciales y datos sensibles seguros y fuera del control de versiones.