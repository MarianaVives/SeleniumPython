from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get("https://the-internet.herokuapp.com/iframe");
driver.maximize_window();
driver.implicitly_wait(5); #if any element is not shown in the page it will wait a max for that element to show up.
print("Title: " + driver.title);
print("URL: " + driver.current_url);

driver.switch_to.frame("mce_0_ifr");
driver.find_element(By.ID, "tinymce").clear();
driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys("Send some text to the input iframe");
driver.switch_to.default_content();
print(driver.find_element(By.CSS_SELECTOR, "h3").text);