import datetime
from collections import namedtuple

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
    yield fixture
    fixture.destroy()


@pytest.fixture(scope="session")
def db():
    db_fixture = Db("localhost", "opencart", "root", "")
    yield db_fixture
    db_fixture.destroy()


# using of built in cache fixture
Duration = namedtuple('Duration', ['current', 'last'])


@pytest.fixture(scope="session")
def duration_cache(request):
    key = 'duration/testdurations'
    d = Duration({}, request.config.cache.get(key, {}))
    yield d
    request.config.cache.set(key, d.current)


@pytest.fixture(autouse=True)
def check_duration(request, duration_cache):
    d = duration_cache
    nodeid = request.node.nodeid
    start_time = datetime.datetime.now()
    yield
    duration = (datetime.datetime.now() - start_time).total_seconds()
    d.current[nodeid] = duration
    if d.last.get(nodeid, None) is not None:
        error_string = "test duration over 2x last duration"
        assert duration <= (d.last[nodeid] * 2), error_string


# using of built in cache fixture
# Report an error if test lasts longer twice as long as last time
# @pytest.fixture(autouse=True)
# def check_duration(request, cache):
#     key = 'duration/' + request.node.nodeid.replace(':', '_')
#     start_time = datetime.datetime.now()
#     yield
#     stop_time = datetime.datetime.now()
#     this_duration = (stop_time - start_time).total_seconds()
#     last_duration = cache.get(key, None)
#     cache.set(key, this_duration)
#     if last_duration is not None:
#         error_string = "test duration over 2x last duration"
#         assert this_duration <= last_duration * 2, error_string
