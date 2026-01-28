from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get("https://the-internet.herokuapp.com/windows");
driver.maximize_window();
driver.implicitly_wait(5); #if any element is not shown in the page it will wait a max for that element to show up.
print("Title: " + driver.title);
print("URL: " + driver.current_url);

driver.find_element(By.LINK_TEXT, "Click Here").click();
windowsOpenedlist = driver.window_handles;
driver.switch_to.window(windowsOpenedlist[1]);

print(driver.find_element(By.TAG_NAME, "h3").text);
driver.close();

driver.switch_to.window(windowsOpenedlist[0]);
assert (driver.find_element(By.TAG_NAME, "h3")).text == "Opening a new window";