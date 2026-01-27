from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get("https://rahulshettyacademy.com/AutomationPractice/");
print("Title: " + driver.title);
print("URL: " + driver.current_url);

name= "Ana";
driver.find_element(By.CSS_SELECTOR, "#name").send_keys(name);
driver.find_element(By.ID, "alertbtn").click();
alert = driver.switch_to.alert;
alert.text #Grabs text inside the alert
print(alert.text);
assert alert.text.__contains__(name);
assert name in alert.text;
alert.accept();
#alert.dismiss(); #cancel
print("Successfully Accepted alert box");