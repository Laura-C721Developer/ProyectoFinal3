# Historia de Usuario: Eliminar un Paciente
"""
Como administrador,
Quiero eliminar un paciente de la base de datos,
Para mantener la información actual y relevante.

Criterios de Aceptación:
Debe haber una opción para eliminar un paciente de la tabla de pacientes.
El sistema debe confirmar antes de eliminar permanentemente la información del paciente.

Criterios de Rechazo:
No hay una confirmación clara antes de eliminar un paciente.
La información del paciente eliminado sigue apareciendo en la base de datos.
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
    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    # Ingresar correo electrónico y contraseña
    email_input = driver.find_element(By.NAME, 'correo')
    password_input = driver.find_element(By.NAME, 'password')
    time.sleep(2)  # Espera 2 segundos

    email_input.send_keys('wveriguete@gmail.com')
    password_input.send_keys('12345678')
    time.sleep(2)  # Espera 2 segundos
    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    # Enviar el formulario
    login_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-warning.btn-block')
    login_button.click()

    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    driver.get('http://localhost/www.sis_biblioteca.com/admin/usuarios/')
    time.sleep(2)  # Espera 2 segundos

 # Esperar a que la tabla de usuarios se cargue
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
    )

    # Encuentra la fila que contiene el nombre del usuario
    user_row = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//td[contains(text(), 'Daniel')]"))
    )

    # Encuentra el botón "Borrar" en la misma fila
    borrar_button = user_row.find_element(By.XPATH, ".//a[contains(@href, 'delete')]")
    borrar_button.click()

    # Aquí debes agregar el código para interactuar con el formulario de eliminación
    # Navegar a la página de confirmación de eliminación de usuario
    driver.get('http://localhost/www.sis_biblioteca.com/admin/usuarios/delete.php?id=30')

    # Esperar a que se cargue el botón de eliminar
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.btn.btn-info.btn-block'))
    )

    # Hacer clic en el botón para eliminar el usuario
    eliminar_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-info.btn-block')
    eliminar_button.click()

    # Esperar y manejar la alerta de confirmación si es necesario
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()  # Aceptar la alerta para confirmar la eliminación

    time.sleep(6)  # Espera 2 segundos
    driver.get('http://localhost/www.sis_biblioteca.com/admin/usuarios/')
    time.sleep(6)  # Espera 2 segundos
    
    # Verificar mensaje de error para credenciales incorrectas
    # Asegúrate de agregar el ID 'error-message' al mensaje de error en tu HTML si quieres usar esta verificación
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'error-message'))
    )
    assert 'Error' in error_message.text
    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    time.sleep(6)  # Espera 2 segundos
finally:
    # Cerrar el navegador después de las pruebas
    driver.quit()