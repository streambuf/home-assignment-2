# _*_ coding: utf-8 _*_
__author__ = 'max'

import os
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException

TIMEOUT = 10
POLL_FREQUENCY = 0.1
USER_PASSWORD = os.environ['TTHA2PASSWORD']


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    MAIN_PAGE_URL = 'http://ftest.stud.tech-mail.ru'

    def open(self):
        self.driver.get(self.MAIN_PAGE_URL)

    def auth(self, login):
        self.driver.find_element(*MainPageLocators.SHOW_LOGIN_FORM_BUTTON).click()
        self.driver.find_element(*MainPageLocators.LOGIN_FIELD).send_keys(login)
        self.driver.find_element(*MainPageLocators.PASSWORD_FIELD).send_keys(USER_PASSWORD)
        self.driver.find_element(*MainPageLocators.LOGIN_BUTTON).submit()


class TopMenuPage(BasePage):
    def get_username(self):
        wait = WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY)
        return wait.until(
            lambda d: d.find_element(*TopMenuLocators.USERNAME).text
        )


class TopicPage(BasePage):
    def get_title(self):
        return WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY).until(
            lambda d: d.find_element(*TopicLocators.TITLE).text
        )

    def get_text(self):
        return WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY).until(
            lambda d: d.find_element(*TopicLocators.TEXT).text
        )

    def get_author(self):
        return WebDriverWait(self.driver, TIMEOUT, POLL_FREQUENCY).until(
            lambda d: d.find_element(*TopicLocators.AUTHOR).text
        )

    def open_blog(self):
        self.driver.find_element(*TopicLocators.BLOG).click()

    def delete(self):
        self.driver.find_element(*TopicLocators.DELETE_BUTTON).click()
        self.driver.find_element(*TopicLocators.DELETE_BUTTON_CONFIRM).click()

    def comment_add_link_is_displayed(self):
        try:
            self.driver.find_element(*TopicLocators.COMMENT_ADD_LINK)
        except NoSuchElementException:
            return False
        return True


class BlogPage(BasePage):
    @property
    def topic(self):
        return TopicPage(self.driver)


class CreateTopicPage(BasePage):
    CREATE_TOPIC_PAGE_URL = 'http://ftest.stud.tech-mail.ru/blog/topic/create/'

    def open(self):
        self.driver.get(self.CREATE_TOPIC_PAGE_URL)
        TopMenuPage(self.driver).get_username()

    def create_topic(self):
        self.driver.find_element(*CreateTopicLocators.CREATE_TOPIC_BUTTON).submit()

    def is_error(self):
        return self.driver.find_element(*CreateTopicLocators.SYSTEM_MESSAGE_ERROR).is_displayed()

    def blog_select_open(self):
        self.driver.find_element(*CreateTopicLocators.BLOGSELECT).click()

    def blog_select_set_option_flood(self):
        self.driver.find_element(*CreateTopicLocators.OPTION_FLOOD).click()

    def set_title(self, title):
        self.driver.find_element(*CreateTopicLocators.TITLE).send_keys(title)

    def set_outer_text(self, outer_text):
        self.driver.find_element(*CreateTopicLocators.SHORT_TEXT).send_keys(outer_text)

    def set_inner_text(self, inner_text):
        self.driver.find_element(*CreateTopicLocators.MAIN_TEXT).send_keys(inner_text)

    def set_forbid_comment_true(self):
        checkbox = self.driver.find_element(*CreateTopicLocators.FORBID_COMMENT_CHECKBOX)
        if not checkbox.is_selected():
            checkbox.click()

    def set_publish_false(self):
        checkbox = self.driver.find_element(*CreateTopicLocators.PUBLISH_CHECKBOX)
        if checkbox.is_selected():
            checkbox.click()


def fill_topic_data(driver, title='', outer_text='', inner_text='', blog_select=True):
    create_topic_page = CreateTopicPage(driver)
    create_topic_page.open()
    if blog_select:
        create_topic_page.blog_select_open()
        create_topic_page.blog_select_set_option_flood()
    create_topic_page.set_title(title)
    create_topic_page.set_outer_text(outer_text)
    create_topic_page.set_inner_text(inner_text)
    return create_topic_page



