import pytest
#conftest file to generalize fixture and make it available to all classes
#the file should always be called conftest
#scope of the fixture is class only. it runs just when the class begins and ends

@pytest.fixture(scope="class") #only run once when the class begins and once when it ends - #before class and after class in junit/testng
def setup():
    print("I will be running first");
    yield #all commands written after yield will be executed at last
    print("I will be executing at the end");