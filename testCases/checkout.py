firefox_driver_path = "/Users/manish/PycharmProjects/pytest_01/drivers/geckodriver"
# firefox_driver_path = "drivers/geckodriver"
from selenium import webdriver
from time import sleep


driver = webdriver.Firefox(executable_path=firefox_driver_path)

driver.get("https://www.flightcentre.com.au/")
driver.maximize_window()
sleep(1)
driver.find_element_by_xpath("//span[@class='fcl-js-Header-MuiIconButton-label']").click()
sleep(2)
driver.find_element_by_xpath("//input[@class='swiftype-search-input form-text']").send_keys("gift card purchase")
sleep(2)
driver.find_element_by_id("edit-submit").click()
sleep(6)
driver.find_element_by_partial_link_text("Gift").click()
sleep(4)
# driver.find_element_by_css_selector("div:nth-of-type(2) > .entity.entity-paragraphs-item.paragraphs-item-fcc-text-and-video p")
driver.find_element_by_link_text("CLICK HERE").click()
sleep(4)
driver.find_element_by_class_name("btn-checkout").click()
sleep(4)
driver.find_element_by_id("firstname").send_keys("James")
sleep(1)
driver.find_element_by_id("firstname").send_keys("James")
sleep(1)
driver.find_element_by_id("lastname").send_keys("Bond")
sleep(1)
driver.find_element_by_id("email").send_keys("abc@gmail.com")
sleep(1)
driver.find_element_by_id("email_confirm").send_keys("abc@gmail.com")
sleep(1)
driver.find_element_by_id("phone").send_keys("778877")
sleep(1)
driver.find_element_by_id("AddressLine1").send_keys("avenue")
sleep(1)
driver.find_element_by_id("AddressLine2").send_keys("east street")
sleep(1)
driver.find_element_by_id("Suburb").send_keys("Melbourne")
sleep(4)
driver.find_element_by_css_selector(".nextDiv.show-if-states-found.siz1 > .selectedTxt").click()
sleep(2)
driver.find_element_by_xpath("//li/a[text()='Victoria']").click()
sleep(2)
driver.find_element_by_css_selector("form#frm-cusdetail  input#PostCode").send_keys("3000")
sleep(2)
driver.find_element_by_id("checktcs").click()
sleep(2)
driver.find_element_by_xpath("//a[@id='con-step-1']").click()
sleep(2)
driver.find_element_by_class_name("add-massage").click()
sleep(3)
driver.find_element_by_css_selector("#popup-Physical #form-submit-recipient-message-2 #RecipientTo").send_keys("abc")


driver.quit()