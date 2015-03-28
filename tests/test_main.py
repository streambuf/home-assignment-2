# _*_ coding: utf-8 _*_
__author__ = 'max'
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.page import *
from page_objects.constants import Tag

COMMAND_EXECUTOR_URL = 'http://127.0.0.1:4444/wd/hub'
LOGIN = 'ftest7@tech-mail.ru'
USERNAME = u'Феодулия Собакевич'
PROFILE_NAME = u'Феодулия'
TITLE = u'Тестовый заголовок'
OUTER_TEXT = u'Краткое описание темы'
INNER_TEXT = u'Текст под катом'
MAX_TITLE_LENGTH = 250
PATH_TO_IMAGE = u'/undefined'
URl = u'http://test.ru'
URL_TITLE = u'title'

MARKDOWN_H4 = u'#### '
MARKDOWN_H5 = u'##### '
MARKDOWN_H6 = u'###### '
MARKDOWN_B = u'****'
MARKDOWN_I = u'**'
MARKDOWN_QUOTES = u'> '
MARKDOWN_CODE = u'``'
MARKDOWN_LIST = u'* '
MARKDOWN_NUM_LIST = u'1. '
MARKDOWN_IMAGE = '![](undefined)'
MARKDOWN_LINK = '(http://test.ru "title")'
MARKDOWN_LINK_PROFILE = '[Феодулия Собакевич](/profile/f.sobakevich/)'

TEST_H4 = '#### test'
TEST_H5 = '##### test'
TEST_H6 = '###### test'
TEST_B = '**test**'
TEST_I = '*test*'
TEST_QUOTES = '> test'
TEST_CODE = '`test`'
TEST_LIST = '* test'
TEST_NUM_LIST = '1. test'
TEST_IMAGE = '![](test.png)'
TEST_LINK = '[name](http://test.ru "title")'
TEST_LINK_PROFILE = u'[Феодулия Собакевич](/profile/f.sobakevich/)'

HTML_H4 = '<h4>test</h4>'
HTML_H5 = '<h5>test</h5>'
HTML_H6 = '<h6>test</h6>'
HTML_B = '<strong>test</strong>'
HTML_I = '<em>test</em>'
HTML_QUOTES = '&gt; test'
HTML_CODE = '<code>test</code>'
HTML_LIST = '<ul>\n<li>test</li>\n</ul>'
HTML_NUM_LIST = '<ol>\n<li>test</li>\n</ol>'
HTML_IMAGE = '<img'
HTML_LINK = '<a href="http://test.ru'
HTML_LINK_PROFILE = '<a href="/profile/f.sobakevich/">'


def not_create_topic(fn):
    def wrapper(*args):
        args[0].post_created = False
        return fn(*args)
    return wrapper


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

    @not_create_topic
    def test_auth(self):
        self.assertEqual(self.username, USERNAME)

    @not_create_topic
    def test_create_topic_with_empty_fields(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_blog_option(self):
        args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT, False)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_title(self):
        args = (self.driver, '', OUTER_TEXT, INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_outer_text(self):
        args = (self.driver, TITLE, '', INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_inner_text(self):
        args = (self.driver, TITLE, OUTER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    def test_create_topic_with_default_settings(self):
        args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()

        self.topic_page = TopicPage(self.driver)
        self.assertEqual(self.topic_page.get_title(), TITLE)
        self.assertEqual(self.topic_page.get_text(), INNER_TEXT)
        self.assertEqual(self.topic_page.get_author(), USERNAME)
        self.assertTrue(self.topic_page.comment_add_link_is_displayed())
        self.topic_page.open_blog()

        blog_page = BlogPage(self.driver)
        self.assertEqual(blog_page.topic.get_title(), TITLE)
        self.assertEqual(blog_page.topic.get_text(), OUTER_TEXT)
        self.assertEqual(blog_page.topic.get_author(), USERNAME)

    @not_create_topic
    def test_create_topic_with_title_greater_max(self):
        title_greater_max = 'a' * (MAX_TITLE_LENGTH + 1)
        args = (self.driver, title_greater_max, OUTER_TEXT, INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    def test_create_topic_with_forbid_comment(self):
        args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.set_forbid_comment_true()
        create_topic_page.create_topic()

        self.topic_page = TopicPage(self.driver)
        self.assertFalse(self.topic_page.comment_add_link_is_displayed())

    @not_create_topic
    def test_create_topic_with_publish_false(self):
        args = (self.driver, TITLE, OUTER_TEXT, INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.set_publish_false()
        create_topic_page.create_topic()

        self.topic_page = TopicPage(self.driver)
        self.topic_page.open_blog()

        blog_page = BlogPage(self.driver)
        self.assertNotEqual(blog_page.topic.get_title(), TITLE)

    def test_create_topic_with_tag_h4(self):
        self.topic_page = create_topic_with_tag(self, TEST_H4)
        self.assertIn(HTML_H4, self.topic_page.get_html())

    def test_create_topic_with_tag_h5(self):
        self.topic_page = create_topic_with_tag(self, TEST_H5)
        self.assertIn(HTML_H5, self.topic_page.get_html())

    def test_create_topic_with_tag_h6(self):
        self.topic_page = create_topic_with_tag(self, TEST_H6)
        self.assertIn(HTML_H6, self.topic_page.get_html())

    def test_create_topic_with_tag_b(self):
        self.topic_page = create_topic_with_tag(self, TEST_B)
        self.assertIn(HTML_B, self.topic_page.get_html())

    def test_create_topic_with_tag_i(self):
        self.topic_page = create_topic_with_tag(self, TEST_I)
        self.assertIn(HTML_I, self.topic_page.get_html())

    def test_create_topic_with_tag_code(self):
        self.topic_page = create_topic_with_tag(self, TEST_CODE)
        self.assertIn(HTML_CODE, self.topic_page.get_html())

    def test_create_topic_with_tag_quotes(self):
        self.topic_page = create_topic_with_tag(self, TEST_QUOTES)
        self.assertIn(HTML_QUOTES, self.topic_page.get_html())

    def test_create_topic_with_tag_list(self):
        self.topic_page = create_topic_with_tag(self, TEST_LIST)
        self.assertIn(HTML_LIST, self.topic_page.get_html())

    def test_create_topic_with_tag_num_list(self):
        self.topic_page = create_topic_with_tag(self, TEST_NUM_LIST)
        self.assertIn(HTML_NUM_LIST, self.topic_page.get_html())

    def test_create_topic_with_tag_image(self):
        self.topic_page = create_topic_with_tag(self, TEST_IMAGE)
        self.assertIn(HTML_IMAGE, self.topic_page.get_html())

    def test_create_topic_with_tag_link(self):
        self.topic_page = create_topic_with_tag(self, TEST_LINK)
        self.assertIn(HTML_LINK, self.topic_page.get_html())

    def test_create_topic_with_tag_link_profile(self):
        self.topic_page = create_topic_with_tag(self, TEST_LINK_PROFILE)
        self.assertIn(HTML_LINK_PROFILE, self.topic_page.get_html())

    @not_create_topic
    def test_create_topic_markdown_h4(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.H4)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_H4)

    @not_create_topic
    def test_create_topic_markdown_h5(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.H5)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_H5)

    @not_create_topic
    def test_create_topic_markdown_h6(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.H6)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_H6)

    @not_create_topic
    def test_create_topic_markdown_b(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.B)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_B)

    @not_create_topic
    def test_create_topic_markdown_i(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.I)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_I)

    @not_create_topic
    def test_create_topic_markdown_quotes(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.QUOTES)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_QUOTES)

    @not_create_topic
    def test_create_topic_markdown_code(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.CODE)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_CODE)

    @not_create_topic
    def test_create_topic_markdown_list(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.LIST)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_LIST)

    @not_create_topic
    def test_create_topic_markdown_num_list(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.NUM_LIST)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_NUM_LIST)

    @not_create_topic
    def test_create_topic_markdown_image(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.IMAGE)
        create_topic_page.set_image(PATH_TO_IMAGE)
        self.assertEqual(create_topic_page.get_text_from_text_area_outer(), MARKDOWN_IMAGE)

    @not_create_topic
    def test_create_topic_markdown_link(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.LINK)
        create_topic_page.set_link(URl, URL_TITLE)
        self.assertIn(MARKDOWN_LINK, create_topic_page.get_text_from_text_area_outer())

    @not_create_topic
    def test_create_topic_markdown_link_profile(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.LINK_PROFILE)
        create_topic_page.set_profile(PROFILE_NAME)
        self.assertIn(unicode(MARKDOWN_LINK_PROFILE, "utf-8"), create_topic_page.get_text_from_text_area_outer())





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


