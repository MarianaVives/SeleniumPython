import time

from selenium import webdriver

#Open Chrome using selenium webdriver
driver = webdriver.Chrome();
driver.get("https://rahulshettyacademy.com");
driver.maximize_window();
print("Title: " + driver.title);
print("URL: " + driver.current_url);

#Open Firefox using selenium webdriver
# driver = webdriver.Firefox();
# driver.get("https://rahulshettyacademy.com");
# driver.maximize_window();
# print("Title: " + driver.title);
# print("URL: " + driver.current_url);

#Open Edge using selenium webdriver
# driver = webdriver.Edge();
# driver.get("https://rahulshettyacademy.com");
# driver.maximize_window();
# print("Title: " + driver.title);
# print("URL: " + driver.current_url);

#time.sleep(5);#pause the execution of the code


#If driver not supported for current browser  you can download the driver and use it with the Service class
#Download Edge driver for MSEdge driver and Gecko driver for Firefox
# service_obj = Service("/path/to/the/driver.exe");
# driver=webdriver.Chrome(service=service_obj);
# driver = webdriver.Chrome();

