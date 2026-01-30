import pytest
from selenium import webdriver

#To send the browser_name using the command line as a param use it like this:
#pytest test_e2eTestFramework.py --browser_name firefox
# py -m pytest --browser_name chrome
#request contains all information and params sent from the command line
# [Important Documentation: https://docs.pytest.org/en/stable/example/simple.html ]

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store_true", default="chrome", help="browser selection"
    )

@pytest.fixture(scope="function")
def browserInstance(request):
    print("Initializing Browser Instance");
    browser_name = request.config.getoption("browser_name")
    print("Browser Name: " + browser_name);
    if browser_name=="chrome":
        driver = webdriver.Chrome();
    elif browser_name=="firefox":
        driver = webdriver.Firefox();
    elif browser_name=="IE":
        driver = webdriver.Ie();
    else:
        print("Unknown browser");
    driver.implicitly_wait(5);
    yield driver;
    #will run after test execution
    driver.close();

@pytest.fixture(params=[("rahulshettyacademy", "Learning@830$3mK2")])
def loginFixture(request):
    print("Initializing Login Page sending username and password in request param in the fixture");
    return request.param;