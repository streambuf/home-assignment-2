__author__ = 'max'
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

TIMEOUT = 10
POLL_FREQUENCY = 0.1
EMPTY_FIELD = u''


class Action(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def click(self, locator):
        self.find(locator).click()

    def click_num(self, locator, num):
        self.find(locator)[num].click()

    def input(self, locator, text):
        self.find(locator).send_keys(text)

    def input_num(self, locator, text, num):
        self.find(locator)[num].send_keys(text)

    def get_attr(self, locator, attr):
        return self.find(locator).get_attribute(attr)

    def submit(self, locator):
        self.find(locator).submit()

    def get_text_with_wait(self, locator):
        return WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY).until(
            lambda d: d.find_element(*locator).text
        )

    def get_attr_with_wait(self, locator, attr):
        return WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY).until(
            lambda d: d.find_element(*locator).get_attribute(attr)
        )

    def open_page(self, url):
        self.driver.get(url)

    def is_exists(self, locator):
        try:
            self.find(locator)
        except NoSuchElementException:
            return False
        return True

    def is_displayed(self, locator):
        return self.find(locator).is_displayed()

    def click_if_not_selected(self, locator):
        checkbox = self.find(locator)
        if not checkbox.is_selected():
            checkbox.click()

    def click_if_selected(self, locator):
        checkbox = self.find(locator)
        if not checkbox.is_selected():
            checkbox.click()

    def execute_script(self, script):
        self.driver.execute_script(script)

    def wait_input_text(self, locator, attr):
        WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY).until(
            lambda d: self.get_attr(locator, attr) != EMPTY_FIELD
        )

    def wait_is_displayed(self, locator):
        WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY).until(
            lambda d: d.find_element(*locator).is_displayed()
        )

    def set_text_alert(self, text):
        wait = WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY)
        wait.until(EC.alert_is_present())
        alert = self.driver.switch_to_alert()
        alert.send_keys(text)
        alert.accept()