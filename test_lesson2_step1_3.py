'''
Задание: кликаем по checkboxes и radiobuttons (капча для роботов)
'''

import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_check_radio():
    chrome_options = Options()
    chrome_options.add_argument('start_maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extentions')
    chrome_options.binary_location = 'D:\\Chrome_test\\chrome-win64\\chrome.exe'
    driver_path = "D:\\Chrome_test\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    url = 'https://suninjuly.github.io/math.html'

    driver.get(url)

    x_elem = driver.find_element(By.ID, 'input_value') 
    x = x_elem.text
    res = calc(x)

    element = driver.find_element(By.ID, 'answer')
    element.send_keys(res)

    element = driver.find_element(By.ID, 'robotCheckbox')
    element.click()

    element = driver.find_element(By.ID, 'robotsRule')
    element.click()

    element = driver.find_element(by=By.CSS_SELECTOR, value='[class="btn btn-default"]')
    element.click()


    assert True, ''


