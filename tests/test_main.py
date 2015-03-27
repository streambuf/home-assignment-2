# _*_ coding: utf-8 _*_
__author__ = 'max'
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.page import *
import time

COMMAND_EXECUTOR_URL = 'http://127.0.0.1:4444/wd/hub'
LOGIN = 'ftest7@tech-mail.ru'
USERNAME = u'Феодулия Собакевич'
TITLE = u'Тестовый заголовок'
OUTER_TEXT = u'Краткое описание темы'
INNER_TEXT = u'Текст под катом'
MAX_TITLE_LENGTH = 250

MARKDOWN_H4 = "#### test"
MARKDOWN_H5 = "##### test"
MARKDOWN_H6 = "###### test"
MARKDOWN_B = "**test**"
MARKDOWN_I = "*test*"
MARKDOWN_QUOTES = "> test"
MARKDOWN_CODE = "`test`"
MARKDOWN_LIST = "* test"
MARKDOWN_NUM_LIST = "1. test"
MARKDOWN_IMAGE = "![](test.png)"
'[name](http://test.ru "title")'
'[Феодулия Собакевич](/profile/f.sobakevich/)'

TAG_H4 = "<h4>test</h4>"
TAG_H5 = "<h5>test</h5>"
TAG_H4 = "<h4>test</h4>"
'<strong>test</strong>'
'<em>test</em>'
'&gt; test'
'<code>test</code>'
'<ul><li>test</li></ul>'
'<ol><li>test</li></ol>'
'<img'
'<a href="http://test.ru'
'<a href="/profile/f.sobakevich/">'

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
        self.post_created = True

    # def test_auth(self):
    #     self.assertEqual(self.username, USERNAME)
    #     self.post_created = False
    #
    # def test_create_topic_with_empty_fields(self):
    #     create_topic_page = fill_topic_data(self.driver)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #     self.post_created = False
    #
    # def test_create_topic_with_empty_blog_option(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT, False)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #     self.post_created = False
    #
    # def test_create_topic_with_empty_title(self):
    #     args = (self.driver, '', OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #     self.post_created = False
    #
    # def test_create_topic_with_empty_outer_text(self):
    #     args = (self.driver, TITLE, '', INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #     self.post_created = False
    #
    # def test_create_topic_with_empty_inner_text(self):
    #     args = (self.driver, TITLE, OUTER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #     self.post_created = False
    #
    # def test_create_topic_with_default_settings(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #
    #     self.topic_page = TopicPage(self.driver)
    #     self.assertEqual(self.topic_page.get_title(), TITLE)
    #     self.assertEqual(self.topic_page.get_text(), INNER_TEXT)
    #     self.assertEqual(self.topic_page.get_author(), USERNAME)
    #     self.assertTrue(self.topic_page.comment_add_link_is_displayed())
    #     self.topic_page.open_blog()
    #
    #     blog_page = BlogPage(self.driver)
    #     self.assertEqual(blog_page.topic.get_title(), TITLE)
    #     self.assertEqual(blog_page.topic.get_text(), OUTER_TEXT)
    #     self.assertEqual(blog_page.topic.get_author(), USERNAME)
    #
    # def test_create_topic_with_title_greater_max(self):
    #     title_greater_max = 'a' * (MAX_TITLE_LENGTH + 1)
    #     args = (self.driver, title_greater_max, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     self.assertTrue(create_topic_page.is_error())
    #     self.post_created = False
    #
    # def test_create_topic_with_forbid_comment(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.set_forbid_comment_true()
    #     create_topic_page.create_topic()
    #
    #     self.topic_page = TopicPage(self.driver)
    #     self.assertFalse(self.topic_page.comment_add_link_is_displayed())
    #
    # def test_create_topic_with_publish_false(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.set_publish_false()
    #     create_topic_page.create_topic()
    #
    #     self.topic_page = TopicPage(self.driver)
    #     self.topic_page.open_blog()
    #
    #     blog_page = BlogPage(self.driver)
    #     self.assertNotEqual(blog_page.topic.get_title(), TITLE)
    #     self.post_created = False

    # def test_create_topic_with_tag_h4(self):
    #     self.topic_page = create_topic_with_tag(self, MARKDOWN_H4)
    #     self.assertIn(TAG_H4, self.topic_page.get_html())







    def test_create_topic_markdown_h4(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_h4_tag()
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), u'#### ')
        self.post_created = False

    def tearDown(self):
        if self.post_created:
            self.topic_page.delete()
        self.driver.close()


    # def test_clear(self):
    #     args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
    #     create_topic_page = fill_topic_data(*args)
    #     create_topic_page.create_topic()
    #     topic_page = TopicPage(self.driver)
    #     topic_page.open_blog()
    #     while True:
    #         blog_page = BlogPage(self.driver)
    #         blog_page.topic.delete()

