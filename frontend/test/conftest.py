import pytest
from frontend.application.application import Application
from frontend.application.db import Db


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser: chrome, firefox, ie or edge")


@pytest.fixture(scope="session")
def base_url():
    return "http://localhost:8080/opencart"


@pytest.fixture(scope="session")
def app(pytestconfig):
    browser = pytestconfig.getoption("browser")
    fixture = Application(browser)
    yield fixture
    fixture.destroy()


@pytest.fixture(scope="session")
def db():
    db_fixture = Db("localhost", "opencart", "root", "")
    yield db_fixture
    db_fixture.destroy()
