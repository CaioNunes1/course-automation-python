from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://app.foodrec.com.br/")
browser.set_window_size(342,642)
time.sleep(2)

browser.find_element(By.XPATH, "//button[@id='cookie-deny-button']").click()
time.sleep(2)

#encontrando o input de email
browser.find_element(By.ID, "email-input").send_keys("caio@gmail.com")
#encontrando o input de senha
browser.find_element(By.ID, "password-input").send_keys("1234")
#encontrando o botão de entrar
time.sleep(3)
browser.find_element(By.XPATH, "//button[normalize-space()='Entrar']").click()
time.sleep(8)

browser.find_element(By.XPATH, "//input[@placeholder='Buscar pratos']").click()
time.sleep(5)

#time.sleep(3)
browser.find_element(By.XPATH, "//input[@placeholder='Digite aqui o termo (e clique na lupa)...']").click()
time.sleep(2)
browser.find_element(By.XPATH, "//input[@placeholder='Digite aqui o termo (e clique na lupa)...']").send_keys("pizza")
time.sleep(2)
browser.find_element(By.XPATH, "//img[@alt='Search Icon']").click()
time.sleep(15)
#escrolar a tela para baixo
for i in range(0, 1000, 10):  # Scroll in increments of 10 pixels
    browser.execute_script(f"window.scrollTo(0, {i});")
    time.sleep(0.05)  # Pause briefly to make the scrolling visible


