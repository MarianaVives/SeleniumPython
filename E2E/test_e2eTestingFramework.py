import os
import sys

#take directory name, then fix the absolute path and then append to the sys path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from E2E.PageObjectModel.ShopPage_pom import ShopPage
from E2E.PageObjectModel.LoginPage_pom import Loginpage
from E2E.PageObjectModel.CheckoutPage_pom import Checkoutpage


def test_e2e(browserInstance, loginFixture):
    driver=browserInstance;
    url="https://rahulshettyacademy.com/loginpagePractise/"
    searched_product = "Blackberry";
    country = "united";
    complete_country = "United Kingdom"

    login_page = Loginpage(driver);
    shop_page= ShopPage(driver);
    checkout_page = Checkoutpage(driver, country, complete_country)

    #login
    login_page.navigate_to_login_page(url)
    login_page.login(loginFixture);

    #Shop product
    shop_page.add_item_to_cart(searched_product);
    shop_page.go_to_cart();

    #Checkout
    checkout_page.checkout();
    checkout_page.select_country();
    checkout_page.validate_order();