from selenium.webdriver.common.by import By
import time


class Shop:
    def __init__(self, driver):
        self.driver = driver
        self.shop_link= (By.XPATH,"//a[normalize-space()='Shop']")
        self.product_name = (By.XPATH,"//div[@class='card h-100']")
        self.checkout_button = (By.CSS_SELECTOR,".nav-link.btn.btn-primary")

    def add_product_to_cart(self,product_name):
        self.driver.find_element(*self.shop_link).click()
        products = self.driver.find_elements(*self.product_name)

        for product in products:
            productName = product.find_element(By.XPATH, ".//h4/a").text 
            if productName == product_name:
                product.find_element(By.XPATH, "div/button").click()

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(5)
        
                


    