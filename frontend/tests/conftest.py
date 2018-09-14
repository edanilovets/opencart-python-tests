import pytest
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


@pytest.fixture(scope="session")
def app():
    fixture = Application()
    fixture.maximize_window()
    yield fixture
    fixture.destroy()


@pytest.fixture(scope="session")
def db():
    db_fixture = Db("localhost", "opencart", "root", "")
    yield db_fixture
    db_fixture.destroy()
