from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome();
driver.get("https://rahulshettyacademy.com/angularpractice/");

name="username";
email="myemail@gmail.com";
password = "password123."

#Locators that Selenium supports ID , Xpath CSSSelector, ClassName, name, linktext
#driver.find_element(By.NAME, "name").send_keys(name);
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys(name);
driver.find_element(By.NAME, "email").send_keys(email);
driver.find_element(By.ID,"exampleInputPassword1").send_keys(password);
driver.find_element(By.ID, "exampleCheck1").click();
select = Select(driver.find_element(By.ID, "exampleFormControlSelect1"));
select.select_by_visible_text("Female");
driver.find_element(By.ID, "inlineRadio1").click();
#xpath selector for submit button
driver.find_element(By.XPATH, '//input[@type="submit"]').click();
message = driver.find_element(By.CLASS_NAME, "alert-success").text;
print(message);
assert "Success!" in message;
driver.find_element(By.XPATH, '//h4/input[@type="text"]').send_keys("Hello Again.");
driver.find_element(By.XPATH, '//h4/input[@type="text"]').clear();