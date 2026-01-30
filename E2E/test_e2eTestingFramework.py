import json
import os
import sys

import pytest

#take directory name, then fix the absolute path and then append to the sys path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from E2E.PageObjectModel.ShopPage_pom import ShopPage
from E2E.PageObjectModel.LoginPage_pom import Loginpage
from E2E.PageObjectModel.CheckoutPage_pom import Checkoutpage

test_data_path = "../E2E/data/test_e2eTestingFramework.json";
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item",test_list)
def test_e2e(browserInstance,test_list_item):
    driver=browserInstance;

    login_page = Loginpage(driver);
    shop_page= ShopPage(driver);
    checkout_page = Checkoutpage(driver, test_list_item["country"], test_list_item["country_name"])

    #login
    login_page.navigate_to_login_page(test_list_item["url"])
    login_page.login(test_list_item["username"], test_list_item["password"]);

    #Shop product
    shop_page.add_item_to_cart(test_list_item["product_name"]);
    shop_page.go_to_cart();

    #Checkout
    checkout_page.checkout();
    checkout_page.select_country();
    checkout_page.validate_order();