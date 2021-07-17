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

@pytest.fixture(scope="session")
def driver_get(request):
    driver = webdriver.Firefox(executable_path=firefox_driver_path)
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    yield
    driver.close()
    driver.quit()


@pytest.fixture
def test_data():
    print("data=========")