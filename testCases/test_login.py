import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
# from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.logger import LogGen

from time import sleep

class TestLoginPage():
    # baseURL = "http://automationpractice.com/index.php"
    #moved into config
    # baseURL = ReadConfig.get_application_url()
    # baseURL = "http://www.google.com"
    # username = ReadConfig.get_user_email()
    # username = "xyz"
    # pwd = ReadConfig.get_user_pwd()
    # pwd = "admin"

    #get log or script
    # logger = LogGen.loggen()

    def test_to_first(self):
        print("this will skip...all way up........")

    # user fixture to get the driver
    def test_home_title(self, setup):
        # self.logger.info("************ TestLoginPage ****************")
        # self.logger.info("************ Started n verifiying home page ****************")
        # self.driver = webdriver.Chrome(executable_path="/Users/manish/PycharmProjects/pytest_01/drivers/chromedriver")
        # self.driver = webdriver.Firefox(executable_path="/Users/manish/PycharmProjects/pytest_01/drivers/geckodriver")
        # self.driver = setup
        # firefox_driver_path = "/Users/manish/PycharmProjects/pytest_01/drivers/geckodriver"
        firefox_driver_path = "/drivers/geckodriver"
        self.driver = webdriver.Firefox(executable_path=firefox_driver_path)
        self.driver.get("https://www.srilankan.com/en_uk/au")
        # title_text = self.driver.title
        # print("\n"+title_text)
        sleep(2)
        self.driver.find_element_by_id("navLogin").click()
        self.driver.find_element_by_partial_link_text("Join Now!").click()

        sleep(3)
        win_list = self.driver.window_handles
        self.driver.switch_to.window(win_list[1])
        print(len(win_list))

        sleep(5)
        print(self.driver.title)
        self.driver.implicitly_wait(5)

        self.driver.find_element_by_id("defaultUnchecked").click()

        #fill the sign up form
        title_dropdown = Select(self.driver.find_element_by_id("ddltitle"))
        title_dropdown.select_by_visible_text("Mr")

        self.driver.find_element_by_id("txtfirstname").send_keys("Manish")
        self.driver.find_element_by_id("txtfamilyname").send_keys("singh")

        #select Nationality
        title_dropdown = Select(self.driver.find_element_by_id("ddlnationality"))
        title_dropdown.select_by_visible_text("INDIA")

        #select dob
        title_dropdown = Select(self.driver.find_element_by_id("txtDate"))
        title_dropdown.select_by_visible_text("15")
        #select
        title_dropdown = Select(self.driver.find_element_by_id("txtMonth"))
        title_dropdown.select_by_visible_text("May")
        #select
        title_dropdown = Select(self.driver.find_element_by_id("txtYear"))
        title_dropdown.select_by_visible_text("1990")

        self.driver.find_element_by_id("txtpassportno").send_keys("42537NJK8")

        #contact Detail

        #select Nationality
        title_dropdown = Select(self.driver.find_element_by_id("ddlcountryofres"))
        title_dropdown.select_by_visible_text("INDIA")

        title_dropdown = Select(self.driver.find_element_by_id("ddlteltype"))
        title_dropdown.select_by_visible_text("Mobile")
        self.driver.find_element_by_id("txttelnumber").send_keys("9987601245")


        #email
        self.driver.find_element_by_id("txtemail").send_keys("abc@gmail.com")
        self.driver.find_element_by_id("txtemailcon").send_keys("abc123")

        #address
        self.driver.find_element_by_id("txtadd1").send_keys("Pent House, Bangalore")
        title_dropdown = Select(self.driver.find_element_by_id("ddlcountry"))
        title_dropdown.select_by_visible_text("INDIA")

        title_dropdown = Select(self.driver.find_element_by_id("ddlcities"))
        title_dropdown.select_by_visible_text("Bengaluru")

        self.driver.find_element_by_id("txtState").send_keys("Karnataka")
        self.driver.find_element_by_id("txtZip").send_keys("560068")


        self.driver.find_element_by_id("txtpasswordreg").send_keys("Abc123456#")
        self.driver.find_element_by_id("txtpasswordcon").send_keys("Abc123456#")

        self.driver.find_element_by_xpath("//div[@class='subs-gen-com']//input[@type='checkbox']").click()
        self.driver.find_element_by_xpath("//div[@class='subs-promo-com']//input[@type='checkbox']").click()
        self.driver.find_element_by_xpath("//div[@class='subs-lanka-com']//input[@type='checkbox']").click()

        self.driver.find_element_by_xpath("//input[@id='chkAgree']").click()

        #click on join now
        self.driver.find_element_by_id("getButtonValue").click()

        # pytest.fail("bad luck")
        # self.driver.save_screenshot("./Screenshots/test_011.png")
        self.driver.close()
        self.driver.quit()
        # self.logger.info("************ test passed ****************")


    # def test_login(self, setup):
        # self.driver = webdriver.Firefox(executable_path="/Users/manish/PycharmProjects/pytest_01/drivers/geckodriver")
        # self.driver = setup
        # self.driver.get(self.baseURL)
        #
        # self.login_page = LoginPage(self.driver)
        # self.login_page.setUserName(self.username)
        # self.login_page.setPassword(self.pwd)
        #
        # self.driver.close()
