import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service

# Asegúrate de reemplazar 'tu_ruta_a_msedgedriver' con la ruta correcta al ejecutable de Edge WebDriver
servicio = Service(executable_path=r"C:\dedgedriver\msedgedriver.exe")
driver = webdriver.Edge(service=servicio)
driver.get ("http://localhost/www.sis_biblioteca.com/login/index.php")
driver.save_screenshot('C:/xampp/htdocs/www.sis_biblioteca.com/Screenshotsdepruebas/captura.png')
time.sleep(10) 

