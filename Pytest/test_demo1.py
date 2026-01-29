#pytest file name should start will test_ or end with _test
#pytest method names should start with test

#-k stands for method names execution, -s logs in output, -v stands for more info metadata
##you can mark tests and then run with -m
#Datadriven and parametrization can be done with return statements in tuple format
#Fixtures are used as setup and teardown methods for test cases - conftest file to generalize
#Fixture and make it available to all test cases (fixture name into parameters of method)
# data driven and parametrization cna be done with return statements in tuple format
#When you define fixture scope to class only, it will run once before class initiated and after it has finished
import pytest
from selenium import webdriver

def test_firstProgram():
    msg = "Hello";
    assert msg == "Hello";

#@pytest.mark.smoke
#@pytest.mark.skip #skip test cases in pytest
def test_secondProgram():
    print("My Second pytest method")
    isTrue = True;
    assert isTrue;

def test_crossBrowser(crossBroswer):
    print("Running test " + crossBroswer[0])