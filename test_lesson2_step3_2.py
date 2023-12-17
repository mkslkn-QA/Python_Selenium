'''
Задание: переход на новую вкладку
'''

import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_accept_alert():
    chrome_options = Options()
    chrome_options.add_argument('start_maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extentions')
    chrome_options.binary_location = 'D:\\Chrome_test\\chrome-win64\\chrome.exe'
    driver_path = "D:\\Chrome_test\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    url = 'http://suninjuly.github.io/redirect_accept.html'

    driver.get(url)

    button1 = driver.find_element(By.CSS_SELECTOR, '[class="trollface btn btn-primary"]').click()
    
    new_window = driver.window_handles[1]
    driver.switch_to.window(new_window)
    

    x = driver.find_element(By.ID, 'input_value').text
    res = calc(x)

    input1 = driver.find_element(By.ID, 'answer').send_keys(res)

    button2 = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()

    assert True, ''