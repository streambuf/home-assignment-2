# _*_ coding: utf-8 _*_
__author__ = 'max'
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.page import *

LOGIN = 'ftest7@tech-mail.ru'
USERNAME = 'Феодулия Собакевич'
COMMAND_EXECUTOR_URL = 'http://127.0.0.1:4444/wd/hub'


def create_topic(driver, title='', outer_text='', inner_text='', blog_select=True):
    create_topic_page = CreateTopicPage(driver)
    create_topic_page.open()
    if blog_select:
        create_topic_page.blog_select_open()
        create_topic_page.blog_select_set_option_flood()
    create_topic_page.set_title(title)
    create_topic_page.set_outer_text(outer_text)
    create_topic_page.set_inner_text(inner_text)
    create_topic_page.create_topic()
    return create_topic_page



class MainTestCase(unittest.TestCase):
    TITLE = u'Тестовый заголовок'
    OUTER_TEXT = u'Краткое описание темы'
    INNER_TEXT = u'Текст под катом'

    def setUp(self):
        browser = DesiredCapabilities.CHROME
        #browser = DesiredCapabilities.FIREFOX
        self.driver = webdriver.Remote(
            command_executor=COMMAND_EXECUTOR_URL,
            desired_capabilities=browser)
        main_page = MainPage(self.driver)
        main_page.open()
        main_page.auth(LOGIN)
        self.username = TopMenuPage(self.driver).get_username()

    # def test_auth(self):
    #     self.assertEqual(self.username, unicode(USERNAME, "utf-8"))
    #
    # def test_create_topic_with_empty_fields(self):
    #     create_topic_page = create_topic(self.driver)
    #     self.assertTrue(create_topic_page.is_error())

    # def test_create_topic_with_empty_blog_option(self):
    #     args = (self.driver, self.TITLE, self.OUTER_TEXT, self.INNER_TEXT, False)
    #     create_topic_page = create_topic(*args)
    #     self.assertTrue(create_topic_page.is_error())

    # def test_create_topic_with_empty_title(self):
    #     args = (self.driver, '', self.OUTER_TEXT, self.INNER_TEXT)
    #     create_topic_page = create_topic(*args)
    #     self.assertTrue(create_topic_page.is_error())

    # def test_create_topic_with_empty_outer_text(self):
    #     args = (self.driver, self.TITLE, '', self.INNER_TEXT)
    #     create_topic_page = create_topic(*args)
    #     self.assertTrue(create_topic_page.is_error())
    #
    # def test_create_topic_with_empty_inner_text(self):
    #     args = (self.driver, self.TITLE, self.OUTER_TEXT)
    #     create_topic_page = create_topic(*args)
    #     self.assertTrue(create_topic_page.is_error())

    def test_create_topic_with_default_settings(self):
        args = (self.driver, self.TITLE, self.OUTER_TEXT, self.INNER_TEXT)
        create_topic(*args)
        self.assertTrue(TopicPage(self.driver).is_success())

    def tearDown(self):
        pass
        #self.driver.close()

