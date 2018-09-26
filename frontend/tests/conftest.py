import os
import pytest
import json
from frontend.application.app import Application
from frontend.application.db import Db


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome, firefox, ie or edge")


@pytest.fixture(scope="session")
def app(pytestconfig):
    file = os.path.join(os.path.dirname(os.path.abspath("..\\..\\__file__")), "frontend\\application\\app_xpath.json")
    with open(file, 'r') as f:
        selectors = json.load(f)
    browser = pytestconfig.getoption("browser")
    fixture = Application(selectors, browser)
    fixture.home_page.open()
    yield fixture
    fixture.destroy()


@pytest.fixture(scope="session")
def db():
    db_fixture = Db("localhost", "opencart", "root", "")
    yield db_fixture
    db_fixture.destroy()
