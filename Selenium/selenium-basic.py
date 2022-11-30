from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://google.com"
driver.get(url)

time.sleep(2)
driver.maximize_window()
driver.save_screenshot("github.come-homepage.png")


url = "http://github.com/abdullahadnir"
driver.get(url)
print(driver.title)

if "abdullahadnir" in driver.title:
    driver.save_screenshot("github-abdullahadnir.png")

time.sleep(2)

driver.back()
# driver.forward()
time.sleep(2)
driver.close()