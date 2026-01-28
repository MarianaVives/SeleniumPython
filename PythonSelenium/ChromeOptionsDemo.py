from selenium import webdriver

chrome_options = webdriver.ChromeOptions();
chrome_options.add_argument("--start-maximized"); #Maximize in the backend
#chrome_options.add_argument("window-size:");
chrome_options.add_argument("--ignore-certificate-errors");
chrome_options.add_argument("--disable-popup-blocking");
chrome_options.add_argument("--disable-client-side-phishing-detection");

driver = webdriver.Chrome(options=chrome_options);
driver.get("https://rahulshettyacademy.com/angularpractice/");
print("URL : " + driver.current_url );
print("Title : " + driver.title);