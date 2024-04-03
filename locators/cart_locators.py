from selenium.webdriver.common.by import By

class CartLocators:
    """A class for cart page locators. All inventory cart locators should come here"""

    def __init__(self):

        self.continue_shopping_button =  (By.ID, "continue-shopping")
        self.checkout_button =  (By.ID, "checkout")
        self.remove_backpack_cart_button = (By.ID, "remove-sauce-labs-backpack")
        self.remove_bike_light_cart_button = (By.ID,"remove-sauce-labs-bike-light")
        self.remove_t_shirt_cart_button = (By.ID,"remove-sauce-labs-bolt-t-shirt")
        self.remove_jacket_cart_button = (By.ID,"remove-sauce-labs-fleece-jacket")
        self.remove_onesie_cart_button = (By.ID,"remove-sauce-labs-onesie")
        self.remove_test_red_cart_button = (By.CSS_SELECTOR,"[name='remove-test.allthethings()-t-shirt-(red)']")

        