import pytest


@pytest.mark.usefixtures("dataLoad")
class TestExampleDataLoad: #class name should start with Test

    def test_editProfile(self, dataLoad):
        print(dataLoad)
        print(dataLoad[0])
