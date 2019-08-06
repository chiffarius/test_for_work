import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import time


# Page helpers, a.k.a combination of steps to do something like changing language

@allure.step('Change language from current one to {1}')
def change_language(driver, language):
    driver.get(language)