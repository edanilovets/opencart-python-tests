import pytest
from frontend.application.app import Application


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

