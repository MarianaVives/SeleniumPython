import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome();
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/");
driver.maximize_window();
driver.implicitly_wait(5); #if any element is not shown in the page it will wait a max for that element to show up.
print("Title: " + driver.title);
print("URL: " + driver.current_url);


items="ber";

product_title = "//div[@class='products']/div/h4";
product_elements = "//div[@class='products']/div";
added_products = [];
matching_products=[];

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber");
print("Successfully sent keys to input bar.");
time.sleep(2);
results = driver.find_elements(By.XPATH, product_elements);
count = len(results);
assert count > 0;
print("Successfully retrieved " + str(count) + " items.");
titles = driver.find_elements(By.XPATH, product_title);
for t in titles:
    added_products.append(t.text);
    print("Added product : " + t.text + " to the cart.");

for r in results:
    r.find_element(By.XPATH, "div/button").click();
    print("Successfully clicked on add to trolley button.");

driver.find_element(By.CSS_SELECTOR, "a[class='cart-icon']").click();
print("Successfully clicked on shopping bag icon")
driver.find_element(By.XPATH, "//*[text()='PROCEED TO CHECKOUT']").click();
print("Successfully clicked 'Proceed to checkout' button");
driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy");
print("Successfully typed promo code into input box");
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click();
print("Successfully clicked to send promo code.");
wait = WebDriverWait(driver, 10);
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")));
print(driver.find_element(By.CSS_SELECTOR, ".promoInfo").text);
assert (driver.find_element(By.CSS_SELECTOR, ".promoInfo")).text == "Code applied ..!";
print("Successfully validated that the code is applied.")

cart_elements= (driver.find_elements(By.CSS_SELECTOR, ".product-name"));
for ce in cart_elements:
    product_name = ce.text.split("-")[0];
    print(product_name);
    for ap in added_products:
        product_title = ap.split("-")[0];
        if product_name == product_title:
            assert product_name == product_title;
            matching_products.append(product_title);
            break
assert len(added_products) == len(matching_products);
print("Successfully validated that selected products are added to the shopping cart the cart.");


prices = driver.find_elements(By.CSS_SELECTOR, "tbody td:nth-child(5) p");
print("Successfully validated that totals of the products are present in the cart.");

sum=0;
for p in prices:
    sum = sum + int(p.text);

total_amt = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text);
total_disc = float(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text);
assert sum == total_amt;
print("Successfully validated that sum of product totals matches total amount.");
assert total_amt > total_disc;
print("Successfully validated that discount is applied to the total amount.");
