from selenium.webdriver.common.by import By

class LoginPageLocators:
    """A class for login page locators. All login page locators should come here"""

    def __init__(self):

        self.username_input =  (By.ID, "user-name")
        self.password_input = (By.ID,"password")
        self.login_button = (By.ID,"login-button")


        