# Historia de Usuario: Agendar una Nueva Cita PA-28
"""
Como administrador registrado,
Quiero programar una nueva cita,
Para organizar mi calendario de trabajo.

Criterios de Aceptación:
Debe haber un formulario sencillo para ingresar los detalles de la nueva cita.
La cita debe aparecer en la tabla de citas una vez confirmada.

Criterios de Rechazo:
El formulario de agendamiento es complicado o confuso para el usuario.
La cita agendada no se refleja en la tabla de citas.
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

    driver.get('http://localhost/www.sis_biblioteca.com/admin/libros/create.php')
    time.sleep(2)  # Espera 2 segundos
    
    #Autocompletado 
   # Autocompletar el formulario
    driver.find_element(By.NAME, 'codigo').send_keys('123262')
    driver.find_element(By.NAME, 'titulo').send_keys('Centro Médico Oncologico')
    driver.find_element(By.NAME, 'autor').send_keys('12:00 AM')
    driver.find_element(By.NAME, 'campo').send_keys(' Gabriel Gonzalo')
    driver.find_element(By.NAME, 'editorial').send_keys('Masculino')
    driver.find_element(By.NAME, 'ano_publicacion').send_keys('12312789')
    driver.find_element(By.NAME, 'nro_edicion').send_keys('80 kg')
    driver.find_element(By.NAME, 'paginas').send_keys('30')
    driver.find_element(By.NAME, 'formato').send_keys('Consulta General')
    driver.find_element(By.NAME, 'ejemplares').send_keys('876')
    driver.find_element(By.NAME, 'observaciones').send_keys('SENASA Contributivo')
    driver.find_element(By.NAME, 'codigo_barra').send_keys('40%')
    time.sleep(2)  # Espera 2 segundos
    
    # Encontrar y hacer clic en el botón de guardar
    guardar_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary.btn-block')
    guardar_button.click()

    # Esperar y manejar la alerta de confirmación
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = driver.switch_to.alert
    alert.accept()  # Aceptar la alerta para confirmar el envío

    driver.get('http://localhost/www.sis_biblioteca.com/admin/libros/index.php')
    time.sleep(2)  # Espera 2 segundos
    

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
