from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get("https://rahulshettyacademy.com/AutomationPractice/");
driver.maximize_window();
driver.implicitly_wait(5); #if any element is not shown in the page it will wait a max for that element to show up.
print("Title: " + driver.title);
print("URL: " + driver.current_url);

action = ActionChains(driver);

action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform();
action.click(driver.find_element(By.LINK_TEXT, "Reload")).perform();
action.move_to_element(driver.find_element(By.CSS_SELECTOR, "#mousehover")).perform();
action.context_click(driver.find_element(By.CSS_SELECTOR, ".mouse-hover-content a:nth-child(1)")).perform();
action.move_to_element(driver.find_element(By.CSS_SELECTOR, ".mouse-hover-content a:nth-child(1)")).click().perform();
