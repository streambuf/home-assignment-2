# _*_ coding: utf-8 _*_
__author__ = 'max'
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.page import *

COMMAND_EXECUTOR_URL = 'http://127.0.0.1:4444/wd/hub'
LOGIN = 'ftest7@tech-mail.ru'
USERNAME = u'Феодулия Собакевич'
TITLE = u'Тестовый заголовок'
OUTER_TEXT = u'Краткое описание темы'
INNER_TEXT = u'Текст под катом'


class MainTestCase(unittest.TestCase):
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
    #     self.assertEqual(self.username, USERNAME)
    #
    # def test_create_topic_with_empty_fields(self):
    #     create_topic_page = fill_topic_data(self.driver)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #
    # def test_create_topic_with_empty_blog_option(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT, False)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #
    # def test_create_topic_with_empty_title(self):
    #     args = (self.driver, '', OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #
    # def test_create_topic_with_empty_outer_text(self):
    #     args = (self.driver, TITLE, '', INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #
    # def test_create_topic_with_empty_inner_text(self):
    #     args = (self.driver, TITLE, OUTER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #
    # def test_create_topic_with_default_settings(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()

    #     topic_page = TopicPage(self.driver)
    #     self.assertEqual(topic_page.get_title(), TITLE)
    #     self.assertEqual(topic_page.get_text(), INNER_TEXT)
    #     self.assertEqual(topic_page.get_author(), USERNAME)
    #     self.assertTrue(topic_page.comment_add_link_is_displayed())
    #     topic_page.open_blog()
    #
    #     blog_page = BlogPage(self.driver)
    #     self.assertEqual(blog_page.topic.get_title(), TITLE)
    #     self.assertEqual(blog_page.topic.get_text(), OUTER_TEXT)
    #     self.assertEqual(blog_page.topic.get_author(), USERNAME)
    #
    #     blog_page.topic.delete()
    #
    # def test_create_topic_with_title_greater_max(self):
    #     title_greater_max = 'a' * 251
    #     args = (self.driver, title_greater_max, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())

    # def test_create_topic_with_forbid_comment(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.set_forbid_comment_true()
    #     create_topic_page.create_topic()

    #     topic_page = TopicPage(self.driver)
    #     self.assertFalse(topic_page.comment_add_link_is_displayed())
    #     topic_page.delete()

    # def test_create_topic_with_publish_false(self):
    #     unique_title = u'unique_title'
    #     args = (self.driver, unique_title, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.set_publish_false()
    #     create_topic_page.create_topic()
    #
    #     topic_page = TopicPage(self.driver)
    #     topic_page.open_blog()
    #
    #     blog_page = BlogPage(self.driver)
    #     self.assertNotEqual(blog_page.topic.get_title(), unique_title)
    #     blog_page.topic.delete()


    def tearDown(self):
        pass
        #self.driver.close()

