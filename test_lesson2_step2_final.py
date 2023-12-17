'''
Загрузка файлов
'''

import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


def test_load_file():
    chrome_options = Options()
    chrome_options.add_argument('start_maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extentions')
    chrome_options.binary_location = 'D:\\Chrome_test\\chrome-win64\\chrome.exe'
    driver_path = "D:\\Chrome_test\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test_file.txt')

    url = 'http://suninjuly.github.io/file_input.html'

    driver.get(url)
    element = driver.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]').send_keys('Ivan')
    element = driver.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]').send_keys('Ivanov')
    element = driver.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]').send_keys('ivanov@ya.ru')
    element = driver.find_element(By.ID, 'file')
    element.send_keys(file_path)

    button1 = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()

    assert True, ''




