from selenium.webdriver.common.by import By
# from PageObjects.shop import Shop
import time

class Loginpage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.ID,"username")
        self.password_field = (By.ID,"password")
        self.login_button = (By.ID,"signInBtn")
    

    def login(self,username,password):
        self.driver.find_element(*self.username_field).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        time.sleep(3)


