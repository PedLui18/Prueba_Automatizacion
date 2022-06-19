#Importamos las librerias 
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# Segun un articulo de internet se modificaron funciones a partir de la v4 
# Razon por la cual es necesario importa las siguientes librerias
# Mas Informacion: https://itsmycode.com/executable-path-has-been-deprecated/
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

#Llamamos al directorio donde se encuentra el ejecutable
driver_path = 'C:\\Users\\Pedro\\Downloads\\chromedriver\\chromedriver.exe'

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

#Inicia la pagina
driver.get('https://es.khanacademy.org/')

#Selecciona el boton de inicia sesion
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'a._282h9ya')))\
    .click()

#Rellena los datos de correo
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'input#uid-login-form-0-wb-id-identifier-field')))\
    .send_keys('pedro.tarqui@uab.edu.bo')
    
#Rellena los datos de contraseña
WebDriverWait(driver, 5)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                    'input#uid-labeled-text-field-1-wb-id-field')))\
    .send_keys('soyelrey10')    
    
#Hace click en el boton Inicia Sesion
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        
                                    'button._6n7s3pu')))\
    .click() 
          
#Hace click en el boton Cursos
WebDriverWait(driver, 10)\
    .until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        
                                    'button._tr38f8i')))\
    .click()       
                         
