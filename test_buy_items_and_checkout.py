import pytest
# import pytest_html
from selenium import webdriver
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import time
import os
from dotenv import load_dotenv
load_dotenv()
homepage_url = os.getenv("homepage_url")


class TestClass:

    def test_buy_items_and_checkout(self,driver_init,valid_login_credentials,valid_checkout_credentials):

        valid_username,valid_password = self.username, self.password                 #valid_login_credentials["username"], valid_login_credentials["password"]
       
        # go to the home page url and login
        login = LoginPage(homepage_url,driver_init,valid_username,valid_password)
        login.valid_login_steps()

        #add backpack_and_jacket to your cart

        inventory = InventoryPage(driver_init)
        inventory.buy_backpack_and_jacket()

        ## proceed to checkout 

        cart = CartPage(driver_init)
        cart.go_to_checkout()

        ## complete checkout process
        valid_first_name,valid_last_name,valid_zip_code =  valid_checkout_credentials
        checkout = CheckoutPage(driver_init,valid_first_name,valid_last_name,valid_zip_code)
        checkout.complete_checkout()
        

       

        
        
        
