import pytest
from selenium import webdriver
import os 
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import os
load_dotenv()

username = os.getenv("valid_username")
password = os.getenv("valid_password")

@pytest.fixture(params=["chrome","firefox","edge"],scope="class")
def driver_init(request):
     
    if request.param == "chrome":
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless")
        web_driver = webdriver.Chrome(options=chrome_options)
    if request.param == "firefox":
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--headless")
        web_driver = webdriver.Firefox(options=firefox_options)
    if request.param == "edge":
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless")
        web_driver = webdriver.Edge(options=edge_options)
    
    # Set username and password attributes 
    request.cls.username = username
    request.cls.password = password

    yield web_driver
    
    web_driver.close()

@pytest.fixture
def valid_login_credentials():
    return {
        "username": os.getenv("valid_username"),
        "password": os.getenv("valid_password")
    }

@pytest.fixture
def valid_checkout_credentials():
    return {
        "first_name": os.getenv("valid_first_name"),
        "last_name": os.getenv("valid_last_name"),
        "zip_code": os.getenv("valid_zip_code")
    }

@pytest.fixture
def empty_login_credentials():
    return {
        "username": os.getenv("empty_username"),
        "password": os.getenv("empty_password")
    }