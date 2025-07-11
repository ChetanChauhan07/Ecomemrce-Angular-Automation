import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC


class checkout:
    def __init__(self,driver):
        self.driver = driver
        self.checkout_button = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.country_dropdown = (By.CSS_SELECTOR,"#country")
        self.country_option = (By.LINK_TEXT,"India")
        self.checkbox_agree = (By.CSS_SELECTOR,"label[for='checkbox2']")
        self.purchase_button = (By.CSS_SELECTOR,"input[value='Purchase']")
        self.order_confirmation_message = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")


    def proceed_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(3)
        # Assuming there is a confirmation page or next step after clicking checkout
        # You can add more actions here if needed
    def select_country(self, country_name):
        self.driver.find_element(*self.country_dropdown).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.presence_of_element_located(self.country_option))
        self.driver.find_element( *self.country_option ).click()
        # Wait for the dropdown to populate with suggestions    
        # Assuming the country dropdown is a typeahead input, you might need to select the country from suggestions
        self.driver.find_element(*self.checkbox_agree).click()
        self.driver.find_element(*self.purchase_button).click()


    def confirm_order(self):
        success_message = self.driver.find_element(*self.order_confirmation_message).text
        assert "Success! Thank you!" in success_message, "Order confirmation failed"
        
