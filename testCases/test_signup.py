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

firefox_driver_path = "drivers/geckodriver"


class TestSignup():

    def test_signup_one(self):
        # self.driver.get("https://www.srilankan.com/en_uk/au")
        # self.driver = webdriver.Firefox(executable_path=firefox_driver_path)

        # self.driver.get("https://www.flightcentre.com.au/")
        # title_text = self.driver.title
        # self.driver.implicitly_wait(5)
        # self.driver.set_page_load_timeout(30)
        # print("\n"+title_text)
        # signup_page = SignupPage(self.driver)

        # ac = ActionChains(self.driver)
        # m = self.driver.find_element_by_xpath("//*[@id='root']/div/header/div/div[2]/div/div/div[1]/nav/a[5]")
        # ac.move_to_element(m).perform()
        # sleep(2)
        # n = self.driver.find_element_by_partial_link_text("See all Deals")
        # # hover over element and click
        # ac.move_to_element(n).click().perform()

        # sleep(3)
        # self.driver.find_element_by_css_selector(".fc-takeover-buoy").click()
        sleep(2)
        # ac = ActionChains(self.driver)
        # fld = self.driver.find_element_by_xpath("//input[@class='MuiInputBase-input MuiOutlinedInput-input' and @value='Melbourne Airport']")
        # ac.move_by_offset( 293, 59).send_keys("SYD").perform()
        # ac.click(fld).perform()
        # ac.move_to_element(self.driver.find_element_by_xpath("//div[@id='downshift-0-input']")).click()

        # self.driver.find_element_by_xpath("//div[@id='downshift-0-input']").click()
        # self.driver.find_element_by_xpath("//div[@id='downshift-0-input']").send_keys("SYD")
        # self.driver.find_element_by_xpath("//*[@id='mini-panel-fcc_homepage_banner']/div[2]/div/div/div/div/div/div/div/div/form/div/div[2]/div/div[1]/div/div[1]/div/div[2]/div/div/div/div").send_keys("SYD")
        # self.driver.find_element_by_xpath("//div[@class='MuiInputBase-root MuiOutlinedInput-root MuiInputBase-fullWidth MuiInputBase-formControl']").send_keys("SYD")
        # self.driver.find_element_by_xpath("//input[@class='MuiInputBase-input MuiOutlinedInput-input' and @value='Melbourne Airport']").click()
        # sleep(10)
        # self.driver.find_element_by_css_selector("#downshift-0-input").click()
        # sleep(5)
        # self.driver.find_element_by_xpath("//*[@id='downshift-1-item-1']").click()
        # ac = ActionChains(self.driver)
        # ac.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        # sleep(3)

        # click on join now to create acc.
        # signup_page.click_on_login_link()
        # signup_page.click_on_join_now_link()

    @pytest.mark.skip
    def test_sigup_with_valid_data(self):
        print("I am in valid data sign -  1")

        # move it to page object model
        signup_page = SignupPage(self.driver)
        jsonfile = "testCases/testData/data.json"
        data = []
        with open(jsonfile) as file:
            data = json.load(file)
        print(data)
        signup_page.enter_pwd("123")
        signup_page.enter_email(data["user"]["email"])
        signup_page.enter_first_name(data["user"]["first_name"])

    @pytest.mark.skip
    def test_sigup_with_invalid_data(self):
        print("I am in invalid data sign -  2")
        print(self.driver)
        # self.driver.quit()

    # @pytest.mark.skip
    def test_to_skip(self):
        print("this will skip...........")
