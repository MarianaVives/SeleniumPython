from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get("https://rahulshettyacademy.com/AutomationPractice/");
print("Title: " + driver.title);
print("URL: " + driver.current_url);

selected_checkbox= "option2"

#Dynamically search for checkbox based on attribute and value
checkbox_list = driver.find_elements(By.XPATH, "//fieldset//input[@type='checkbox']");
for c in checkbox_list:
    if c.get_attribute("value") == selected_checkbox:
        c.click();
        driver.implicitly_wait(5);
        assert c.is_selected();
        print("Successfully checked " + selected_checkbox);
        break;

#Radio button
radioBtn = driver.find_elements(By.CSS_SELECTOR, ".radioButton");
#when you know the exact index you can find it using index [i]
radioBtn[2].click();
assert radioBtn[2].is_selected();
print("Successfully selected radio button");

#Hide text/boxes
assert driver.find_element(By.ID, "displayed-text").is_displayed();
print("Successfully found visible text");
driver.find_element(By.ID, "hide-textbox").click();
print("Successfully clicked hide button");
assert not driver.find_element(By.ID, "displayed-text").is_displayed();
print("Successfully not found visible text");
