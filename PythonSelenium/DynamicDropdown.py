import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
url="https://rahulshettyacademy.com/dropdownsPractise/";
driver.get(url);
print("Successfully visited the URL: " + url);

driver.find_element(By.CSS_SELECTOR, "#autosuggest").send_keys("Ind");
driver.find_element(By.CSS_SELECTOR, "#autosuggest");
driver.implicitly_wait(5);
dd_list =driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a");
print("Successfully found the dropdown list");
print(len(dd_list));
search_country = "india";
for d in dd_list:
    if d.text.upper() == search_country.upper():
        print("Successfully found item : " + d.text);
        d.click();
        print("Successfully clicked on country");
        break; #exit the loop after finding the item we want
#Validate that clicked element is written in the search box
dyn_text = driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value"); #Get the value of the attribute of the locator - listens actively even those dynamically generated through the script
assert dyn_text.upper() == search_country.upper();
print("Successfully found attribute on dynamic dropdown after click");
