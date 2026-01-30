import pytest
from selenium.webdriver.common.by import By

from E2E.PageObjectModel.ShopPage_pom import ShopPage
from E2E.util.BrowserUtils import BrowserUtils
from PythonSelenium.Locators import password

@pytest.mark.usefixtures("loginFixture")
class Loginpage(BrowserUtils):

    def __init__(self, driver):
        super().__init__(driver) #initializes driver in parent class
        self.driver = driver
        self.username_input = (By.CSS_SELECTOR, "#username");
        self.password_input = (By.NAME, "password");
        self.signIn_button = (By.CSS_SELECTOR, "#signInBtn");

    def navigate_to_login_page(self, url):
        self.driver.get(url);
        self.driver.maximize_window();
        print("URL: " + self.driver.current_url);

    def login(self, username, password):
        #star breaks elements into two. the selector and by come in a tuple form, star sparates by and locator into twwo arguments
        self.driver.find_element(*self.username_input).send_keys(username);
        self.driver.find_element(*self.password_input).send_keys(password);
        self.driver.find_element(*self.signIn_button).click();
