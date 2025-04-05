from selenium import webdriver
import time
driver=webdriver.Edge()
driver.get("https://google.com")
viewports=[(1024,768),(786,1024),(375,667)]


try :
    for width,height in viewports:
        driver.set_window_size(width,height)
        time.sleep(5)
finally:
    driver.close()