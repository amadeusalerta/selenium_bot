from selenium import webdriver
import time

driver=webdriver.Chrome()

url_00="https://sicanzi.com/"

driver.get(url_00)

time.sleep(2)
print(driver.title)
driver.maximize_window()
driver.save_screenshot("github.com-nahcek.png")

url_01="https://github.com/amadeusalerta"
driver.get(url_01)

if "amadeusalerta" in driver.title:
    driver.save_screenshot("github_amadeus.png")

time.sleep(4)
driver.back
time.sleep(4)
driver.close()