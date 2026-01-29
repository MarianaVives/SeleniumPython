import pytest
#Setup is found in conftest file

@pytest.mark.usefixtures("setup") #automatically apply the fixture to all the methods of the class
class TestExample:

    def test_fixtureDemo(self):
        print("Test 1- I will be running after fixture");

    def test_fixtureDemo2(self):
        print("Test 2- I will be running after fixture");

    def test_fixtureDemo3(self):
        print("Test 3- I will be running after fixture");

    def test_fixtureDemo4(self):
        print("Test 4- I will be running after fixture");