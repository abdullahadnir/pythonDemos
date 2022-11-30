from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver  = webdriver.Chrome()

url ="http://github.com"
driver.get(url)
searchInput = driver.find_element(By.XPATH,'/html/body/div[1]/header/div/div[2]/div/div/div[1]/div/div/form/label/input[1]')
time.sleep(2)

searchInput.send_keys("python")
time.sleep(2)

driver.find_element(By.NAME,'q').send_keys(Keys.ENTER)
time.sleep(2)
# result = driver.page_source
# print(result)
result = driver.find_elements(By.CSS_SELECTOR,'.d-flex div .v-align-middle')
for element in result:
    print(element.text)


driver.close()