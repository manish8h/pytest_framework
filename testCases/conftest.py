from selenium import webdriver
import pytest

chrome_driver_path = "/Users/manish/PycharmProjects/pytest_01/drivers/chromedriver"
firefox_driver_path = "/Users/manish/PycharmProjects/pytest_01/drivers/geckodriver"

@pytest.fixture(scope= "session")
def setup(request):
    pass
    # print("\n to get requester details====")
    # print(request.node)
    # print(request)
    # driver = webdriver.Chrome(executable_path=chrome_driver_path)
    # driver = webdriver.Firefox(executable_path=firefox_driver_path)
    # driver.maximize_window()
    # driver.implicitly_wait(5)
    # request.cls.driver = driver
    # yield
    # driver.close()
    # driver.quit()

@pytest.fixture(scope="class")
def driver_get(request):
    driver = webdriver.Firefox(executable_path=firefox_driver_path)
    request.cls.driver = driver
    # session = request.node
    # for item in session.items:
    #     cls = item.getparent(pytest.Class)
    #     setattr(cls.obj, "driver", driver)
    yield
    request.cls.driver.close()
    request.cls.driver.quit()


@pytest.fixture
def test_data():
    print("==data==")
    return ("user_name", "password", "type_admin")


@pytest.fixture(scope = 'class')
def class_fixture():
    print("before class")
    yield
    print("After class")


@pytest.fixture(params=[
    {'user': "Ptest", "pwd": 123},
    {'user': "Python", "pwd": 12321},
])
def data_provider(request):
    return request.param


def pytest_cmdline_main(config):
    print("\n==I am from cmd line hook ===============\n")
    print(config.option)
    print(config.getoption("debug"))
    print(config.getoption("showcapture"))
    print(config.getoption("browser"))

def pytest_configure(config):
    print("\n=======pytest config hooks=======\n")
    print(config)
    print(config.getoption("browser"))
    print("\n=======pytest config hooks=======\n")

def pytest_sessionstart(session):
    print("\n=======pytest session hooks=======\n")
    print(session)
    print("\n=======pytest session hooks=======\n")

#item = Testcase
def pytest_collection_modifyitems(session, config, items):
    print("\n=======pytest modifyitems hooks=======\n")
    print(session)
    print(config)
    print(items)
    print("\n=======pytest modifyitems hooks=======\n")

def pytest_collection_finish(session):
    print("\n=======pytest collection_finish hooks=======\n")
    print(session)
    print("\n=======pytest collection_finish hooks=======\n")

def pytest_runtest_setup(item):
    print("\n=======pytest runtest_setup level hooks=======\n")
    print(item.name)
    # refer: https://github.com/pytest-dev/pytest/issues/3261
    #refer: https://docs.pytest.org/en/stable/reference.html#config
    print("\n=======pytest test case level hooks=======\n")

def pytest_runtest_teardown(item):
    print("\n=======pytest runtest_teardown level hooks=======\n")
    print(item.name)
    print("\n=======pytest runtest_teardown level hooks=======\n")

def pytest_report_teststatus(report):
    print("\n=======pytest pytest_report_teststatus level hooks=======\n")
    print(report)
    print(report.outcome)
    # refer: https://github.com/pytest-dev/pytest/issues/3261
    #refer: https://docs.pytest.org/en/stable/reference.html#config
    print("\n=======pytest pytest_report_teststatus level hooks=======\n")

#custom option --browser FF
#custom option --browser="chrome"
def pytest_addoption(parser):
    parser.addoption('--browser', action='store',
                     default='chrome', help='Mention browser to run Test Case - chrome, firefox')

