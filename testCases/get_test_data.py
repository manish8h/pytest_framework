import json
from time import sleep
from selenium import webdriver
import allure_pytest
import allure
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from testCases.basetest import BaseTest

from selenium.webdriver.support.select import Select
from pageObjects.signup_page import SignupPage

firefox_driver_path = "/Users/manish/PycharmProjects/pytest_01/drivers/geckodriver"


class TestSignup():

    def test_sigup_with_valid_data(self):
        print("I am in valid data sign -  1")
        self.driver = webdriver.Firefox(executable_path=firefox_driver_path)

        # move it to page object model
        signup_page = SignupPage(self.driver)

        jsonfile = "/Users/manish/PycharmProjects/pytest_01/testCases/testData/data.json"

        data = []
        with open(jsonfile) as file:
            data = json.load(file)
        print(data)
        # assert False == True


    @pytest.mark.skip
    def test_sigup_with_invalid_data(self):
        print("I am in invalid data sign -  2")
        print(self.driver)
        # self.driver.quit()

    @pytest.mark.skip
    def test_to_skip(self):
        print("this will skip...........")
