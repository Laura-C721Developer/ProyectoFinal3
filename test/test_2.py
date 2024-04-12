#Historia de Usuario: Añadir un Nuevo Paciente PA - 29 
"""
Como administrador,
Quiero añadir un nuevo paciente al sistema,
Para mantener actualizada la base de datos de pacientes.

Criterios de Aceptación:
Debe haber un formulario para ingresar la información del nuevo paciente.
El nuevo paciente debe aparecer en la tabla de pacientes tras ser añadido.

Criterios de Rechazo:
El formulario para añadir pacientes no valida correctamente la información ingresada.
El nuevo paciente no aparece en la tabla de pacientes después de ser añadido.
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

    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    driver.get('http://localhost/www.sis_biblioteca.com/admin/usuarios/create.php')
    time.sleep(2)  # Espera 2 segundos
    
    #Autocompletado 
   # Autocompletar el formulario
    # Autocompletar los campos del formulario
    driver.find_element(By.NAME, 'nombres').send_keys('Martina')
    driver.find_element(By.NAME, 'apellidos').send_keys('D Oleo')
    driver.find_element(By.NAME, 'ci').send_keys('46464646')
    driver.find_element(By.NAME, 'celular').send_keys('8295678376')
    driver.find_element(By.NAME, 'cargo').send_keys('Tumor')
    driver.find_element(By.NAME, 'email').send_keys('martinadoleo@hotmail.com')
    time.sleep(3)  # Espera 2 segundos
    
    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    # Encontrar y hacer clic en el botón para registrar el usuario
    registrar_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-info.btn-block')
    registrar_button.click()

    # Esperar y manejar la alerta de confirmación
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()  # Aceptar la alerta para confirmar el envío

    time.sleep(4)  # Espera 2 segundos
    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    driver.get('http://localhost/www.sis_biblioteca.com/admin/usuarios/')
    time.sleep(6)  # Espera 2 segundos
    
    # Verificar mensaje de error para credenciales incorrectas
    # Asegúrate de agregar el ID 'error-message' al mensaje de error en tu HTML si quieres usar esta verificación
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, 'error-message'))
    )
    assert 'Error' in error_message.text
    driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')

    time.sleep(2)  # Espera 2 segundos
finally:
    # Cerrar el navegador después de las pruebas
    driver.quit()