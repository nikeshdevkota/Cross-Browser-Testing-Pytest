from locators.login_locators import LoginPageLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class LoginPage(LoginPageLocators):
    """A class for login page objects. All login page objects should come here"""

    def __init__(self,url,driver,username,password):

        super().__init__() # inherit locators from LoginPageLocators class
        self.url = url
        self.driver = driver
        self.username = username
        self.password = password
 
    def navigate_to_login_page(self):
        self.driver.get(self.url)

    def enter_username(self):
        try:
            username_input =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.username_input))
            username_input.clear()
            print(self.username)
            username_input.send_keys(self.username)
        
        except NoSuchElementException as e:
             print("Username element not found:", e)

    def enter_password(self):
        try:
            password_input =  WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.password_input))
            password_input.clear()
            print(self.password)
            password_input.send_keys(self.password)
        
        except NoSuchElementException as e:
             print("Password element not found:", e)
        # self.driver.find_element(*self.password_input).send_keys(self.password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def verify_inventory_url(self):
        time.sleep(2)
        expected_inventory_url = "{}/inventory.html".format(self.url)
        # Get the current URL of the webpage
        extracted_inventory_url = self.driver.current_url
        # Assert that the current URL matches the expected inventory URL
        assert extracted_inventory_url == expected_inventory_url, f"Expected inventory URL: {expected_inventory_url}, Actual URL: {extracted_inventory_url}"

    def valid_login_steps(self):
        self.navigate_to_login_page()
        self.enter_username()
        self.enter_password()
        self.click_login_button()
        self.verify_inventory_url()