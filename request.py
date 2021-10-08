from selenium import webdriver
import selenium
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome()
driver.get ("https://www.anr.org.py/consulta-padron-nacional/")

#Tiempo de espera para dejar que cargue la página
time.sleep(3)

#Cambio al segundo frame
frame = driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(frame)


def consulta (driver,cedula):
    """Función que retorna una lista con datos del numero de cedula ingresado como parametro"""
    cedula = cedula
    cedula_in = driver.find_element_by_xpath("//input[@name='cedula']")
    cedula_in.clear()
    cedula_in.send_keys(cedula)
    cedula_in.send_keys(Keys.RETURN)
    time.sleep(1.5)
    datos =driver.find_elements_by_xpath("//li[@class='consulta-item list-group-item']")
    data_list = []
    for x in datos:
        data_list.append(x.text)
    return data_list




#Numero de cedula SEBAS 5898204
print (consulta(driver,'5898204'))

#Numero de cedula ESTEBAN 5425495
print (consulta(driver,'5425495'))





