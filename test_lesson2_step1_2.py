'''
Задание на execute_script
'''
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

def test_execute_script():
    chrome_options = Options()
    chrome_options.add_argument('start_maximized')
    chrome_options.add_argument('--disable-infobars')
    chrome_options.add_argument('--disable-extentions')
    chrome_options.binary_location = 'D:\\Chrome_test\\chrome-win64\\chrome.exe'
    driver_path = "D:\\Chrome_test\\chromedriver-win64\\chromedriver.exe"

    service = Service(executable_path=driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.implicitly_wait(5)

    url = 'https://SunInJuly.github.io/execute_script.html'

    driver.get(url)
    x_elem = driver.find_element(By.ID, 'input_value')
    x = x_elem.text
    res = calc(x)

    input1 = driver.find_element(By.ID, 'answer').send_keys(res)

    robot_checkbox = driver.find_element(By.ID, 'robotCheckbox').click()

    driver.execute_script("window.scrollBy(0, 150);")

    robot_radiobutton = driver.find_element(By.ID, 'robotsRule').click()

    button1 = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()

    assert True, ''

    