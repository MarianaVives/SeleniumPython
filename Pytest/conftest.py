import pytest
#conftest file to generalize fixture and make it available to all classes
#the file should always be called conftest
#scope of the fixture is class only. it runs just when the class begins and ends

@pytest.fixture(scope="class") #only run once when the class begins and once when it ends - #before class and after class in junit/testng
def setup():
    print("I will be running first");
    yield #all commands written after yield will be executed at last
    print("I will be executing at the end");

@pytest.fixture
def dataLoad():
    print("User data profile is being created");
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]

#handle multiple browsers
#@pytest.fixture(params=["chrome","Firefox","IE"])
#def crossBroswer(request):
#    print("Running test in browser : " + request.param);
#    return request.param;

#handle multiple browsers when the test requires test data
@pytest.fixture(params=[("chrome", "Rahul", "Shetty"),("Firefox", "rahul"), ("IE", "ABC")])
def crossBroswer(request):
    return request.param;