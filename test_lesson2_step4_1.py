'''
Задание: ждем нужный текст на странице
'''

import pytest
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument('start_maximized')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('--disable-extentions')
chrome_options.binary_location = 'D:\\Chrome_test\\chrome-win64\\chrome.exe'
driver_path = "D:\\Chrome_test\\chromedriver-win64\\chromedriver.exe"

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.implicitly_wait(5)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_explicit_wait():
    url = 'http://suninjuly.github.io/explicit_wait2.html'
    driver.get(url)

    price = WebDriverWait(driver, 12).until(EC.text_to_be_present_in_element([By.ID, 'price'], text_='100'))
    button1 = driver.find_element(By.ID, 'book').click()

    driver.execute_script("window.scrollBy(0, 150);")

    x = driver.find_element(By.ID, 'input_value').text
    res = calc(x)
    input1 = driver.find_element(By.ID, 'answer').send_keys(res)

    button_submit = driver.find_element(By.ID, 'solve').click()

    assert True, ''