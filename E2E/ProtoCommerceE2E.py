from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome();
driver.get("https://rahulshettyacademy.com/angularpractice/");
driver.maximize_window();
driver.implicitly_wait(5); #if any element is not shown in the page it will wait a max for that element to show up.
print("Title: " + driver.title);
print("URL: " + driver.current_url);

wait = WebDriverWait(driver, 10);
searched_product= "Blackberry";
country="united";
complete_country="United Kingdom"

driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click();
#wait(expected_conditions.presence_of_element_located((By.XPATH,"//a[text()='Home']")))

products_list = driver.find_elements(By.XPATH, "//div[@class='card h-100']");

for p in products_list:
    driver.execute_script("window.scrollBy(0,document.body.scrollHeight)");
    print("Scroll down");
    product_name= p.find_element(By.XPATH,"div/h4/a").text
    print(product_name);
    if product_name.upper() == searched_product.upper():
        print("Found product " + product_name);
        driver.find_element(By.XPATH, "//div[@class='card h-100']/div/button").click();
        print("Added product to the basket " + product_name);
        break;
driver.find_element(By.CSS_SELECTOR, "a[class*='btn']").click();
print("Navigated to checkout");
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click();
driver.find_element(By.CSS_SELECTOR, "#country").send_keys(country);
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"United Kingdom")));
driver.find_element(By.CSS_SELECTOR, "#country").send_keys(country);
print("Successfully typed : " + country);
driver.find_element(By.XPATH, "//ul/li/a[text()='"+complete_country+"']").click();
print("Clicked on country " +complete_country);
driver.find_element(By.CSS_SELECTOR, "*[type='submit']").click();
print("Click on Purchase button");
successText = driver.find_element(By.CSS_SELECTOR, ".alert.alert-success").text;
print("Text from alert: " + successText);
assert "Success! Thank you" in successText;
print("Alert contains expected text")
