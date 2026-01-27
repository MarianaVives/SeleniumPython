from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
url="https://rahulshettyacademy.com/client";
driver.get(url);
print("Successfully visited the URL: " + url);
email="demo@gmail.com";
password = "Hello@1234"
driver.find_element(By.CSS_SELECTOR, "a[class='forgot-password-link']").click();
print("Successfully clicked on forgot password link");

driver.find_element(By.XPATH,"//form/div[1]/input").send_keys(email);
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys(password);
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys(password);
driver.find_element(By.XPATH,"//button").click();
#To find locator by text //button[text()="Submit"]
print("Successfully clicked on Submit button.");