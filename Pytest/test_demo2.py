#pytest file name should start will test_ or end with _test
#pytest method names should start with test
import pytest
from selenium import webdriver

@pytest.mark.smoke
def test_firstProgram():
    msg = "My second class";
    assert "second class" in msg ;

@pytest.mark.xfail #you want this test case to fail
def test_myMethod2():
    a=4;
    b=6;
    assert a+2==b; #Shoud pass

#define a fixture
@pytest.fixture()
def setup():
    print("I will be running first");

def test_fixtureDemo(setup):
    print("I will be running after the fixture");