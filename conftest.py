from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def browser():
    chromeBrowser = webdriver.Edge()
    yield chromeBrowser
