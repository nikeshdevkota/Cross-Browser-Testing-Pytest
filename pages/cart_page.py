from locators.cart_locators import CartLocators
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

class CartPage(CartLocators):
    """A class for cart page objects. All cart page objects should come here"""

    def __init__(self,driver):

        super().__init__() 
        self.driver = driver

    def go_to_checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()

    def remove_item(self,remove_element):
        try:
            self.driver.find_element(*self.remove_element).click()
        except NoSuchElementException:
            pass

    def remove_backpack(self):
        self.remove_item(self.remove_bike_light_cart_button)

    def remove_bike_light(self):
        self.remove_item(self.remove_bike_light_cart_button)

    def remove_t_shirt(self):
        self.remove_item(self.remove_t_shirt_cart_button)

    def remove_jacket(self):
        self.remove_item(self.remove_jacket_cart_button)
    
    def remove_onsesie(self):
        self.remove_item(self.remove_onesie_cart_button)

    def remove_test_red(self):
        self.remove_item(self.remove_test_red_cart_button)



