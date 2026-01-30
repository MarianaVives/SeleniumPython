from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from E2E.PageObjectModel.CheckoutPage_pom import Checkoutpage


class ShopPage:
    def __init__(self, driver):
        self.driver = driver;
        self.shop_link = (By.XPATH, "//a[contains(@href,'shop')]")
        self.product_cards = (By.XPATH, "//div[@class='card h-100']");
        self.add_item_to_cart_btn = (By.XPATH, "//div[@class='card h-100']/div/button")
        self.product_name = (By.XPATH, "div/h4/a")
        self.checkout_btn = (By.CSS_SELECTOR, "a[class*='btn']")
        self.home_text = (By.XPATH,"//a[text()='Home']")

    def add_item_to_cart(self, search_product_name):
        print("Navigating to shop")
        self.driver.find_element(*self.shop_link).click();
        wait = WebDriverWait(self.driver, 10);
        #wait(expected_conditions.presence_of_element_located(self.home_text))
        wait.until(expected_conditions.visibility_of_element_located(self.product_cards));
        products_list = self.driver.find_elements(*self.product_cards);

        for p in products_list:
            self.driver.execute_script("window.scrollBy(0,document.body.scrollHeight)");
            print("Scroll down");
            product_name = p.find_element(*self.product_name).text
            print(product_name);
            if product_name.upper() == search_product_name.upper():
                print("Found product " + product_name);
                self.driver.find_element(*self.add_item_to_cart_btn).click();
                print("Added product to the basket " + product_name);
                break;

    def go_to_cart(self):
        self.driver.find_element(*self.checkout_btn).click();
        print("Navigated to cart");
