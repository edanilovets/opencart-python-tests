import pytest
import json
from frontend.application.app import Application
from frontend.application.db import Db

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


@pytest.fixture(scope="session")
def app():
    config = load_xpath_config("xpath.json")
    fixture = Application(config)
    fixture.maximize_window()
    yield fixture
    fixture.destroy()


@pytest.fixture(scope="session")
def db():
    db_fixture = Db("localhost", "opencart", "root", "")
    yield db_fixture
    db_fixture.destroy()
