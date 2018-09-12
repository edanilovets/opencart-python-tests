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


@pytest.fixture(scope="module")
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()


@pytest.fixture
def db():
    db_fixture = Db("localhost", "opencart", "root", "")
    yield db_fixture
    db_fixture.destroy()
