import pytest


@pytest.fixture()
def setup():
    print("I will be running first");
    yield #all commands written after yield will be executed at last
    print("I will be execution at the end");

def test_fixtureDemo(setup):
    print("I will be running after fixture");