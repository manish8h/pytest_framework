from webdriver.WebdriverBasePage import WebdriverBasePage


class BasePage(WebdriverBasePage):

    def __init__(self, driver , file_path = "Reports/test.log"):
        self.driver = driver
        super().__init__(self.driver, file_path)

    #locator = XPATH/ID/CLASS_NAME
    # def click_on(self, locator, value):
    #     element = self.driver.find_element(by=locator, value=value)
    #     element.click()
