import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService



@pytest.fixture()
def setup():
    service = FirefoxService(executable_path=GeckoDriverManager().install())
    return webdriver.Firefox(service=service)