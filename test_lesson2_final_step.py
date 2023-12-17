'''
Задание: поиск сокровища с помощью get_attribute
'''

import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_search_valuex():
    chrome_options = Options()
    chrome_options.add_argument('start_maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extentions')
    chrome_options.binary_location = 'D:\\Chrome_test\\chrome-win64\\chrome.exe'
    driver_path = "D:\\Chrome_test\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    url = 'http://suninjuly.github.io/get_attribute.html'
    driver.get(url)

    
    x_elem = driver.find_element(By.ID, 'treasure')
    text = x_elem.get_attribute('valuex')
    x = calc(int(text))

    input1 = driver.find_element(By.ID, 'answer')
    input1.send_keys(x)

    robot_checkbox = driver.find_element(By.ID, 'robotCheckbox')
    robot_checkbox.click()

    robot_radiobutton = driver.find_element(By.ID, 'robotsRule')
    robot_radiobutton.click()

    button = driver.find_element(by=By.CSS_SELECTOR, value='[class="btn btn-default"]')
    button.click()


    assert True, ''