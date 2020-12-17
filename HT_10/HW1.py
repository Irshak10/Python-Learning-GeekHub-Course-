# НТ #10
#За допомогою Selenium зайти на сайт ОЛХ, ввести в пошук будь-який запит, дочекатись отримання результатів і зберегти скріншот сторінки.

#Моя відповідь: 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path='chromedriver')
driver.maximize_window()

delay = 5
wait = WebDriverWait(driver, delay)

driver.get('https://www.olx.ua/')


search_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#headerSearch')), 'Error message')
search_field.send_keys('nokia 3310')

search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#submit-searchmain')), 'Error message')
search_button.click()
time.sleep(5)

driver.get_screenshot_as_file("screenshot.png")

driver.quit()