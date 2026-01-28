from selenium import webdriver
from selenium.webdriver.common.by import By

#Execute in headless mode
chrome_opt = webdriver.ChromeOptions();
chrome_opt.add_argument("headless");

#When you get certificate opening on the browser
#chrome_opt.add_argument("--ignore-certificate-errors");

driver = webdriver.Chrome(options=chrome_opt);
driver.get("https://rahulshettyacademy.com/AutomationPractice/");
driver.maximize_window();
driver.implicitly_wait(5); #if any element is not shown in the page it will wait a max for that element to show up.
print("Title: " + driver.title);
print("URL: " + driver.current_url);

#Scroll is supported with JS language
#Scroll to the bottom of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)");
#Take SS after scroll
driver.get_screenshot_as_file("screen.png");
