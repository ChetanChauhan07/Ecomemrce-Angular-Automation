import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.loginPage import Loginpage
from PageObjects.shop import Shop
from PageObjects.checkout import checkout
import time
import json

test_data_path='../Data/test_e2e.json'
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data['data']

@pytest.mark.parametrize("test_list_items",test_list)
def test_form_submission(browserInstance, test_list_items):
    driver = browserInstance
    driver.get( "https://rahulshettyacademy.com/loginpagePractise/" )
    loginpage=Loginpage(driver)

    loginpage.login(test_list_items["userEmail"], test_list_items["userPassword"])
    shop = Shop(driver)
    shop.add_product_to_cart(test_list_items["productName"])
    shop.go_to_checkout()
    checkout_page = checkout(driver)
    checkout_page.proceed_to_checkout()
    checkout_page.select_country("India")
    checkout_page.confirm_order()

