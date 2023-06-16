from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import pytest
import time

LINK = "http://selenium1py.pythonanywhere.com"

def test_language_options(browser):
    browser.get(LINK)

    book_ref = browser.find_element(By.CSS_SELECTOR, "li.dropdown-submenu > a")
    book_ref.click()

    title_book_ref = browser.find_element(By.CSS_SELECTOR, "[title='Coders at Work']")
    title_book_ref.click()

    button_add_to_basket = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    time.sleep(10)
    assert button_add_to_basket
