'''
Задание: работа с выпадающим списком
'''

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select


def test_Drop_down_list():
    chrome_options = Options()
    chrome_options.add_argument('start_maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extentions')
    chrome_options.binary_location = 'D:\\Chrome_test\\chrome-win64\\chrome.exe'
    driver_path = "D:\\Chrome_test\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    url = 'https://suninjuly.github.io/selects1.html'

    driver.get(url)

    x_elem = driver.find_element(By.ID, 'num1')
    x = x_elem.text
    y_elem = driver.find_element(By.ID, 'num2')
    y = y_elem.text
    res = int(x) + int(y)

    select = Select(driver.find_element(By.TAG_NAME, 'select'))
    select.select_by_visible_text(str(res))

    button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-default"]').click()


    assert True, ''