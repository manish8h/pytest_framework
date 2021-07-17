import pytest
import selenium.webdriver.support.wait as wait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select

from webdriver.logger_page import LoggerClass


class WebdriverBasePage(object):
    filepath = ""

    def __init__(self, x, filepath):
        self.driver = x
        self.web_driver_wait = wait.WebDriverWait(self.driver, 30)
        self.filepath = filepath
        """description of class"""

    def navigateto(self, url):
        self.driver.get(url)

    def elementWaitCondition(self, byelement, byindentifier):
        self.web_driver_wait.until(
            expected_conditions.presence_of_element_located((byelement, byindentifier)), "element is not present")

    def entertext(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.clear()
            element.send_keys(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nEnter value : " + byindentifier + " value :" + mvalue)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def click(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.click()
            LoggerClass.writeFile(self.filepath,
                                  "\nClick to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def submit(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            element.submit()
            LoggerClass.writeFile(self.filepath,
                                  "\nSubmit to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def selectdropdownvaluebytext(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_visible_text(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value" + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def driverquit(self):
        self.driver.quit()

    def pressTab(self):
        action = ActionChains(self.driver)
        action.send_keys(Keys.TAB)

    def isElementPresent(self, byelement, byindentifier):
        try:
            isElementPresent = False
            self.elementWaitCondition(byelement, byindentifier)
            if len(self.driver.find_elements(by=byelement, value=byindentifier)) > 0:
                isElementPresent = True
            else:
                isElementPresent = False

            return isElementPresent
        except WebDriverException as e:
            raise e

    def isElementEnabled(self, byelement, byindentifier):
        try:
            isElementEnabled = False
            self.elementWaitCondition(byelement, byindentifier)
            isElementEnabled = self.driver.find_element(by=byelement, value=byindentifier).is_enabled()
            return isElementEnabled;
        except WebDriverException as e:
            raise e

    def isDisplayed(self, byelement, byindentifier):
        try:
            isDisplayedStatus = False
            self.elementWaitCondition(byelement, byindentifier)
            isElementEnabled = self.driver.find_element(by=byelement, value=byindentifier).is_displayed()
            return isElementEnabled
        except WebDriverException as e:
            raise e

    def isAlertIsPresent(self):
        try:
            self.web_driver_wait.until(
                expected_conditions.alert_is_present(), "Alert is not present")

        except WebDriverException as e:
            raise e

    def selectDropDownValueByIndex(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_index(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def selectDropDownValueByVisibleText(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_visible_text(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def selectDropDownValueByValue(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.select_by_value(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "Selected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def clickAndHold(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.move_to_element(element).click().perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nClick and Hold to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def contextClick(self, byelement, byindentifier):
        try:
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.context_click(element).perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nContext Click to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def doubleClick(self, byelement, byindentifier):
        try:
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.double_click(element).perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nDouble Click to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def dragAndDrop(self, sourcebyelement, sourcebyindentifier, targetbyelement,
                    targetbyindentifier):
        try:
            sourceelement = self.driver.find_element(by=sourcebyelement, value=sourcebyindentifier)
            targetelement = self.driver.find_element(by=targetbyelement, value=targetbyindentifier)
            actions = ActionChains(self.driver)
            actions.click_and_hold(sourceelement).move_to(targetelement).release()
            LoggerClass.writeFile(self.filepath,
                                  "\nDrag element " + sourcebyindentifier + "Drop Element " + targetbyindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def clickByActionClass(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            actions = ActionChains(self.driver)
            actions.click(element).perform()
            LoggerClass.writeFile(self.filepath,
                                  "\nClick to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def clickToElementByJavaScript(self, byelement, byindentifier):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element = self.driver.find_element(by=byelement, value=byindentifier)
            self.driver.execute_script("arguments[0].click();", element)
            LoggerClass.writeFile(self.filepath,
                                  "\nClick to " + byindentifier)
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def scrollToView(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except WebDriverException as e:
            raise e

    def deSelectDropDownValueByIndex(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_index(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def deSelectDropDownValueByVisibleText(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_visible_text(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def deSelectDropDownValueByValue(self, byelement, byindentifier, mvalue):
        try:
            self.elementWaitCondition(byelement, byindentifier)
            element1 = self.driver.find_element(by=byelement, value=byindentifier)
            element = Select(element1)
            element.deselect_by_value(mvalue)
            LoggerClass.writeFile(self.filepath,
                                  "\nSelected DropDown " + byindentifier + "And Value " + mvalue + "deselected")
        except WebDriverException as e:
            LoggerClass.writeFile(self.filepath, "\n" + e.msg)
            raise e

    def back(self):
        self.driver.back()
