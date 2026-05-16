from selenium import webdriver
import pytest
from pytest_metadata.plugin import metadata_key

@pytest.fixture()  # decorator
def setup(browser):
    if browser == "chrome":
        driver=webdriver.Chrome()
        print("launching chrome")
    elif browser == "firefox":
        driver=webdriver.Firefox()
        print("launching firefox")
    else:
        driver=webdriver.Edge()
        print("launching edge")
    return driver

def pytest_addoption(parser): #this will get value from cli/hooks
    parser.addoption("--browsername")         #, default="chrome"

@pytest.fixture()
def browser(request): #this will return browser value to setup method
    return request.config.getoption("--browsername")


###pytest html report###
# it is hook for adding environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]['project Name'] = 'nop commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers'
    config.stash[metadata_key]['Tester'] = 'Jahnavi'

#It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
    metadata.pop("Base URL", None)


