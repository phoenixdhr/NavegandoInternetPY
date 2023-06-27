from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service('/mnt/c/Users/danyr/Downloads/chromedriver_win32')  # Sustituye esto con la ruta donde se encuentra tu chromedriver
driver = webdriver.Chrome(service=service)

driver.get("https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/FrameCriterioBusquedaWeb.jsp")

ruc_input = driver.find_element(By.ID, "txtRuc")
ruc_input.clear()
ruc_input.send_keys("20600056477")  # Sustituye esto con el número de RUC

time.sleep(1)  # Dar tiempo para que se cargue la página

submit_button = driver.find_element(By.ID, "btnAceptar")
submit_button.click()

# Esperar a que se carguen los resultados y luego puedes procesarlos
time.sleep(1)

submit_button = driver.find_element(By.CLASS_NAME, "btnInfRepLeg")
submit_button.click()

# Esperar a que se carguen los resultados y luego puedes procesarlos
time.sleep(1)

# Agrega esta línea al final para que el navegador permanezca abierto hasta que presiones una tecla
input("Presiona una tecla para cerrar el navegador...")
driver.quit()


# # Cerrar el navegador una vez que hayas terminado
# driver.quit()




