from locators.inventory_locators import InventoryLocators
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InventoryPage(InventoryLocators):
    """A class for inventory page objects. All inventory page objects should come here"""

    def __init__(self,driver):

        super().__init__() # inherit locators from InventoryPageLocators class
        self.driver = driver
 
    def add_remove_item_to_cart(self,add_element,remove_element):
    
        try:
            self.driver.find_element(*remove_element).click()
        except NoSuchElementException:
            self.driver.find_element(*add_element).click()
    
    def add_remove_backpack(self):
        self.add_remove_item_to_cart(self.add_backpack_cart_button,self.remove_backpack_cart_button)

    def add_remove_bike_light(self):
        self.add_remove_item_to_cart(self.add_bike_light_cart_button,self.remove_bike_light_cart_button)

    def add_remove_t_shirt(self):
        self.add_remove_item_to_cart(self.add_t_shirt_cart_button,self.remove_t_shirt_cart_button)

    def add_remove_jacket(self):
        self.add_remove_item_to_cart(self.add_jacket_cart_button,self.remove_jacket_cart_button)
    
    def add_remove_onsesie(self):
        self.add_remove_item_to_cart(self.add_onesie_cart_button,self.remove_onesie_cart_button)

    def add_remove_test_red(self):
        self.add_remove_item_to_cart(self.add_test_red_cart_button,self.remove_test_red_cart_button)

    def remove_any_existing_carts(self):
        
        try:
            elements = self.driver.find_elements(*self.remove_all_cart_button)
            for element in elements:
                element.click()
        except NoSuchElementException:
            pass

    def go_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()


    def verify_cart_url(self):
        time.sleep(2)
        # Get the current URL of the webpage
        extracted_cart_url = self.driver.current_url
        # Assert that the current URL matches the expected inventory URL
        assert "cart" in extracted_cart_url, f"Website not redirected to cart section"

    
    def verify_number_of_items(self):
        time.sleep(1)
        number_of_items = int(self.driver.find_element(*self.number_of_items).text)
        assert number_of_items==2, f"Number of items in the cart must be 2"


    def buy_backpack_and_jacket(self):
        self.remove_any_existing_carts()
        self.add_remove_backpack()
        self.add_remove_jacket()
        self.verify_number_of_items()
        self.go_to_cart()
        self.verify_cart_url()

