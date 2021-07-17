from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from locators.signup_page_locators import SignupPageLocators
from pageObjects.base_page import BasePage


class SignupPage(BasePage):


    def __init__(self, driver):
        self.driver = driver
        super().__init__(self.driver)

    # signup_page_locator = SignupPageLocators()


    def click_on_login_link(self):
        BasePage.click(self, By.ID, SignupPageLocators.LOGIN_ID)

    def click_on_join_now_link(self):
        BasePage.click(self, By.PARTIAL_LINK_TEXT, SignupPageLocators.JOIN_ME_NOW_TXT)



    def enter_email(self, email):
        print(SignupPageLocators , email)

    def enter_pwd(self, pwd):
        print("pwd:" + pwd)

    def enter_first_name(self, first_name):
        print("first:" + first_name)

    def select_new_acc_type(self):
        self.driver.find_element_by_id(SignupPageLocators.NEW_ACC_TYPE_ID).click()

    def select_title(self, title):
        title_dropdown = Select(self.driver.find_element_by_id(SignupPageLocators.TITLE_ID))
        title_dropdown.select_by_visible_text(title)



    def fill_create_account_form(self):
        #click on join now to create acc.
        self.click_on_join_now_link()
        # select open new tab
        win_list = self.driver.window_handles
        self.driver.switch_to.window(win_list[1])
        print(len(win_list))

        # sleep(5)
        print(self.driver.title)
        self.driver.implicitly_wait(5)
        # seleect acc type
        self.select_new_acc_type()

        #fill the sign up form
        self.select_title()