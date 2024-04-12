#Epica 5, HU: Inicio de Sesión Seguro
# Como usuario del sistema de agendamiento de citas, quiero iniciar sesión de manera segura y rápida, para acceder a mis funciones de agendamiento y gestión de citas.
"""
Criterios de Aceptación:

Facilidad de Acceso:
El usuario debe poder acceder al formulario de inicio de sesión desde la página principal.
El formulario debe ser claro y solicitar solo el correo electrónico y la contraseña.
Seguridad:
El sistema debe encriptar la contraseña antes de enviarla para su verificación.
Debe existir una opción para mostrar/ocultar la contraseña mientras se escribe.
Validación:
El sistema debe validar las credenciales y permitir el acceso solo si son correctas.
Si las credenciales son incorrectas, el sistema debe mostrar un mensaje de error claro.


Acceso Difícil:
El formulario de inicio de sesión es difícil de encontrar o no carga correctamente.
El formulario solicita más información de la necesaria, complicando el proceso.
Falta de Seguridad:
La contraseña se envía o almacena sin encriptación adecuada.
No hay opción para mostrar/ocultar la contraseña, lo que puede comprometer la seguridad.
Validación Incorrecta:
El sistema permite el acceso con credenciales incorrectas.
Los mensajes de error son genéricos y no ayudan al usuario a entender el problema.
"""

import time  # Importa el módulo time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configuración del WebDriver para Edge
s = Service(executable_path=r"C:\dedgedriver\msedgedriver.exe")
driver = webdriver.Edge(service=s)
driver.maximize_window()  # Maximiza la ventana del navegador
try:
    # Navegar a la página principal
    driver.get('http://localhost/www.sis_biblioteca.com/login/index.php')
    time.sleep(2)  # Espera 2 segundos

    # Acceder al formulario de inicio de sesión
    login_form = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'form'))
    )
    time.sleep(2)  # Espera 2 segundos

    # Ingresar correo electrónico y contraseña
    email_input = driver.find_element(By.NAME, 'correo')
    password_input = driver.find_element(By.NAME, 'password')
    time.sleep(2)  # Espera 2 segundos

    email_input.send_keys('wveriguete@gmail.com')
    password_input.send_keys('12345678')
    time.sleep(2)  # Espera 2 segundos

    # Localizar el botón para mostrar/ocultar la contraseña
    # Asegúrate de que este botón tenga un ID único en tu HTML para poder localizarlo aquí
    toggle_password_button = driver.find_element(By.ID, 'toggle-password')
    time.sleep(2)  # Espera 2 segundos

    # Hacer clic en el botón para mostrar la contraseña
    toggle_password_button.click()
    time.sleep(2)  # Espera 2 segundos

    # Hacer clic nuevamente para ocultar la contraseña
    toggle_password_button.click()
    time.sleep(2)  # Espera 2 segundos

    # Enviar el formulario
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-warning.btn-block')
    login_button.click()

    # Verificar mensaje de error para credenciales incorrectas
    # Asegúrate de agregar el ID 'error-message' al mensaje de error en tu HTML si quieres usar esta verificación
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'error-message'))
    )
    assert 'Error' in error_message.text
    time.sleep(2)  # Espera 2 segundos
finally:
    # Cerrar el navegador después de las pruebas
    driver.quit()
