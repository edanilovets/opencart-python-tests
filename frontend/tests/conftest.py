import pytest
import json
from frontend.application.app import Application
from frontend.application.db import Db

# Alternative version to add tear down fixture

# @pytest.fixture(scope="module")
# def app(request):
#     fixture = Application()
#
#     def fin():
#         fixture.destroy()
#
#     request.addfinalizer(fin)
#     return fixture


def load_xpath_config(file):
    with open(file, 'r') as f:
        config = json.load(f)
    return config


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome, firefox, ie or edge")


@pytest.fixture(scope="session")
def app(pytestconfig):
    config = load_xpath_config("xpath.json")
    browser = pytestconfig.getoption("browser")
    fixture = Application(config, browser)
    fixture.maximize_window()
    yield fixture
    fixture.destroy()


@pytest.fixture(scope="session")
def db():
    db_fixture = Db("localhost", "opencart", "root", "")
    yield db_fixture
    db_fixture.destroy()
