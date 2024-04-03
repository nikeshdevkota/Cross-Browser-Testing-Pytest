from locators.checkout_locators import CheckOutLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class CheckoutPage(CheckOutLocators):
    """A class for cart page objects. All cart page objects should come here"""

    def __init__(self,driver,first_name,last_name,zip_code):

        super().__init__() 
        self.first_name = first_name
        self.last_name = last_name
        self.driver = driver
        self.zip_code = zip_code
    
    def enter_first_name(self):
        try:
            first_name_input =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.first_name_input))
            first_name_input.clear()
            first_name_input.send_keys(self.first_name)
        
        except NoSuchElementException as e:
             print("Username element not found:", e)

    def enter_last_name(self):
        try:
            last_name_input =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.last_name_input))
            last_name_input.clear()
            last_name_input.send_keys(self.last_name)
        
        except NoSuchElementException as e:
             print("Username element not found:", e)

    def enter_zip_code(self):
        try:
            zip_code_input =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.zip_code_input))
            zip_code_input.clear()
            zip_code_input.send_keys(self.zip_code)
        
        except NoSuchElementException as e:
             print("Username element not found:", e)

    def continue_checkout(self):
        self.driver.find_element(*self.continue_button).click()

    def finish_checkout(self):
        time.sleep(2)
        self.driver.find_element(*self.finish_button).click()

    def complete_checkout(self):
        self.enter_first_name()
        self.enter_last_name()
        self.enter_zip_code()
        self.continue_checkout()
        self.finish_checkout()