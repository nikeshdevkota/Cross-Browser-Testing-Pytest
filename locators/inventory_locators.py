from selenium.webdriver.common.by import By

class InventoryLocators:
    """A class for inventory page locators. All inventory page locators should come here"""

    def __init__(self):

        self.add_backpack_cart_button =  (By.ID, "add-to-cart-sauce-labs-backpack")
        self.remove_backpack_cart_button = (By.ID,"remove-sauce-labs-backpack")
        self.add_bike_light_cart_button = (By.ID,"add-to-cart-sauce-labs-bike-light")
        self.remove_bike_light_cart_button = (By.ID,"remove-sauce-labs-bike-light")
        self.add_t_shirt_cart_button = (By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
        self.remove_t_shirt_cart_button = (By.ID,"remove-sauce-labs-bolt-t-shirt")
        self.add_jacket_cart_button = (By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        self.remove_jacket_cart_button = (By.ID,"remove-sauce-labs-fleece-jacket")
        self.add_onesie_cart_button = (By.ID,"add-to-cart-sauce-labs-onesie")
        self.remove_onesie_cart_button = (By.ID,"remove-sauce-labs-onesie")
        self.add_test_red_cart_button =  (By.CSS_SELECTOR,"//button[@name='add-to-cart-test.allthethings()-t-shirt-(red)']")
        self.remove_test_red_cart_button =  (By.CSS_SELECTOR,"//button[@name='remove-test.allthethings()-t-shirt-(red)']")
        self.add_to_cart_button = (By.CLASS_NAME,"shopping_cart_link")
        self.remove_all_cart_button = (By.CSS_SELECTOR,"[class='btn btn_secondary btn_small btn_inventory ']")
        self.number_of_items = (By.CLASS_NAME,"shopping_cart_badge")
        
# price = @//div[@class='inventory_list']//div[n]//div[2]//div[2]//div[1]