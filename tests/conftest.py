import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config


from demoqa_tests.utils import attach


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser = Browser(Config(driver))

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()





#import os
#
#from selene.support.shared import browser
#import pytest
#
#
#@pytest.fixture(scope='function', autouse=True)
#def browser_management():
#    browser.config.base_url = os.getenv('selene.base_url', 'https://demoqa.com')
#    browser.config.browser_name = os.getenv('selene.browser_name', 'chrome')
#    browser.config.hold_browser_open = (
#        os.getenv('selene.hold_browser_open', 'false').lower() == 'true'
#    )
#    browser.config.timeout = float(os.getenv('selene.timeout', '3'))
#