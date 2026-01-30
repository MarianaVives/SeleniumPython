from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Checkoutpage:
    def __init__(self, driver,country_initials, country_name):
        self.driver = driver;
        self.country_initials = country_initials;
        self.country_name = country_name;
        self.checkout_btn = (By.CSS_SELECTOR, "button[class='btn btn-success']")
        self.country_input = (By.CSS_SELECTOR, "#country")
        self.country_textdropdown = (By.LINK_TEXT, self.country_name);
        self.dynamic_countrydropdown = (By.XPATH, "//ul/li/a[text()='" + self.country_name + "']")
        self.submit_btn = (By.CSS_SELECTOR, "*[type='submit']")
        self.message_textbox = (By.CSS_SELECTOR, ".alert.alert-success")

    def checkout(self):
        print("Click on checkout");
        self.driver.find_element(*self.checkout_btn).click();

    def select_country(self):
        print("Sending country initials ")
        self.driver.find_element(*self.country_input).send_keys(self.country_initials);
        print("Successfully typed : " + self.country_initials);
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_textdropdown));
        self.driver.find_element(*self.dynamic_countrydropdown).click();
        print("Clicked on country " + self.country_name);
        self.driver.find_element(*self.submit_btn).click();
        print("Click on Purchase button");

    def validate_order(self):
        print("Validating order")
        success_text = self.driver.find_element(*self.message_textbox).text;
        print("Text from alert: " + success_text);
        assert "Success! Thank you" in success_text;
        print("Alert contains expected text")





