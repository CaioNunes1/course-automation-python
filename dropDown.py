from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver= webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/dropdown")
driver.maximize_window()
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,"#dropdown").click()
time.sleep(3)