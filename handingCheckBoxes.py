from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
browser=webdriver.Edge()
browser.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
browser.maximize_window()
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

browser.find_element(By.CSS_SELECTOR," label[for='RESULT_CheckBox-8_0']").click()
time.sleep(3)
browser.find_element(By.CSS_SELECTOR," label[for='RESULT_CheckBox-8_0']").click()
#time.sleep(3)
checkboxes=browser.find_elements(By.XPATH,"//input[@type='checkbox']")

for checkbox in checkboxes:
    if checkbox.is_selected():
        print("Selected")
    else:
        print("Not selected")
time.sleep(3)

for checkbox in checkboxes:
    checkbox.send_keys(Keys.SPACE)
    #ou checkbox.click()

checked_count=0

for checkbox in checkboxes:
    if checkbox.is_selected():
        checked_count += 1        

expected_count=9

if checked_count == expected_count:
    print("All checkboxes are checked")
else:
    print("Not all checkboxes are checked")
time.sleep(3)
browser.quit()