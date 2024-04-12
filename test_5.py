# Historia de Usuario: Visualización de la Tabla de Citas PA-26

"""
Como administrador registrado,
Quiero ver una tabla con todas mis citas programadas,
Para tener una visión general de mis próximas citas.

Criterios de Aceptación:
La tabla debe mostrar la fecha, hora, nombre del paciente y tipo de cita.
Debe ser posible ordenar la tabla por cualquiera de los campos mencionados.

Criterios de Rechazo:
La tabla no muestra todos los campos requeridos (fecha, hora, nombre del paciente, tipo de cita).
La tabla no permite la ordenación por los campos mencionados.

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

    
    # Enviar el formulario
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-warning.btn-block')
    login_button.click()

    driver.get('http://localhost/www.sis_biblioteca.com/admin/libros/index.php')
    time.sleep(5)  # Espera 5 segundos
    
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
