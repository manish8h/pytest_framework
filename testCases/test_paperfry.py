from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



#run it on travis ci
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.headless = False
# chrome_options.headless = True
# driver = webdriver.Chrome(ChromeDriverManager().install(), options= chrome_options)

# driver.get("https://www.pepperfry.com/")
# driver.set_page_load_timeout(10)
# driver.implicitly_wait(5)

# dwn_link = driver.find_element_by_xpath("//*[text()='playstore']")

# or
# driver.execute_script("arguments[0].click();", dwn_link)

# or

# function getElementByXpath(path) {
#     return document.evaluate(path, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
# }

# getElementByXpath("//a[text()='playstore']").click();

# or
# document.evaluate("//a[text()='playstore']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();

# driver.quit()