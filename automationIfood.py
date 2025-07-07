from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.ifood.com.br/")
time.sleep(5)

browser.find_element(By.XPATH, "//span[normalize-space()='Entrar']").click()
time.sleep(5)

browser.find_element(By.XPATH, "//span[normalize-space()='E-mail']").click()
time.sleep(5)

browser.find_element(By.XPATH, "//input[@name='email']").send_keys("gabrielnunesdelima2003@gmail.com")
time.sleep(5)
#depois apertaria nesse botão de continuar, porém não quero testar agora, 
browser.find_element(By.XPATH, "//span[normalize-space()='Continuar']")