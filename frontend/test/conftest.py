import pytest
from frontend.application.application import Application


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
