#pytest file name should start will test_ or end with _test
#pytest method names should start with test

#-k stands for method names execution, -s logs in output, -v stands for more info metadata
##you can mark tests and then run with -m
import pytest
from selenium import webdriver

def test_firstProgram():
    msg = "Hello";
    assert msg == "Hello";

@pytest.mark.smoke
#@pytest.mark.skip #skip test cases in pytest
def test_secondProgram():
    print("My Second pytest method")
    isTrue = True;
    assert isTrue;