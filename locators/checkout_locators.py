from selenium.webdriver.common.by import By


class CheckOutLocators:
    """A class for inventory page locators. All inventory page locators should come here"""

    def __init__(self):

        self.first_name_input =  (By.ID, "first-name")
        self.last_name_input =  (By.ID, "last-name")
        self.zip_code_input = (By.ID,"postal-code")
        self.continue_button = (By.ID,"continue")
        self.cancel_button = (By.ID,"cancel")
        self.finish_button = (By.ID,"finish")
       