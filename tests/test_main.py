# _*_ coding: utf-8 _*_
__author__ = 'max'
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.page import *
from page_objects.constants import Tag
from test_constants import *


def not_create_topic(fn):
    def wrapper(*args):
        args[0].post_created = False
        return fn(*args)
    return wrapper


class MainTestCase(unittest.TestCase):
    def setUp(self):
        #browser = DesiredCapabilities.CHROME
        browser = DesiredCapabilities.FIREFOX
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
        self.topic_page = create_topic_with_tag(self, H4.text)
        self.assertIn(H4.html, self.topic_page.get_html())

    def test_create_topic_with_tag_h5(self):
        self.topic_page = create_topic_with_tag(self, H5.text)
        self.assertIn(H5.html, self.topic_page.get_html())

    def test_create_topic_with_tag_h6(self):
        self.topic_page = create_topic_with_tag(self, H6.text)
        self.assertIn(H6.html, self.topic_page.get_html())

    def test_create_topic_with_tag_b(self):
        self.topic_page = create_topic_with_tag(self, B.text)
        self.assertIn(B.html, self.topic_page.get_html())

    def test_create_topic_with_tag_i(self):
        self.topic_page = create_topic_with_tag(self, I.text)
        self.assertIn(I.html, self.topic_page.get_html())

    def test_create_topic_with_tag_code(self):
        self.topic_page = create_topic_with_tag(self, CODE.text)
        self.assertIn(CODE.html, self.topic_page.get_html())

    def test_create_topic_with_tag_quotes(self):
        self.topic_page = create_topic_with_tag(self, QUOTES.text)
        self.assertIn(QUOTES.html, self.topic_page.get_html())

    def test_create_topic_with_tag_list(self):
        self.topic_page = create_topic_with_tag(self, LIST.text)
        self.assertIn(LIST.html, self.topic_page.get_html())

    def test_create_topic_with_tag_num_list(self):
        self.topic_page = create_topic_with_tag(self, NUM_LIST.text)
        self.assertIn(NUM_LIST.html, self.topic_page.get_html())

    def test_create_topic_with_tag_image(self):
        self.topic_page = create_topic_with_tag(self, IMAGE.text)
        self.assertIn(IMAGE.html, self.topic_page.get_html())

    def test_create_topic_with_tag_link(self):
        self.topic_page = create_topic_with_tag(self, LINK.text)
        self.assertIn(LINK.html, self.topic_page.get_html())

    def test_create_topic_with_tag_link_profile(self):
        self.topic_page = create_topic_with_tag(self, LINK_PROFILE.text)
        self.assertIn(LINK_PROFILE.html, self.topic_page.get_html())

    @not_create_topic
    def test_create_topic_markdown_h4(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.H4)
        self.assertEqual(create_topic_page.get_outer_text(), H4.markdown)

    @not_create_topic
    def test_create_topic_markdown_h5(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.H5)
        self.assertEqual(create_topic_page.get_outer_text(), H5.markdown)

    @not_create_topic
    def test_create_topic_markdown_h6(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.H6)
        self.assertEqual(create_topic_page.get_outer_text(), H6.markdown)

    @not_create_topic
    def test_create_topic_markdown_b(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.B)
        self.assertEqual(create_topic_page.get_outer_text(), B.markdown)

    @not_create_topic
    def test_create_topic_markdown_i(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.I)
        self.assertEqual(create_topic_page.get_outer_text(), I.markdown)

    @not_create_topic
    def test_create_topic_markdown_quotes(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.QUOTES)
        self.assertEqual(create_topic_page.get_outer_text(), QUOTES.markdown)

    @not_create_topic
    def test_create_topic_markdown_code(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.CODE)
        self.assertEqual(create_topic_page.get_outer_text(), CODE.markdown)

    @not_create_topic
    def test_create_topic_markdown_list(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.LIST)
        self.assertEqual(create_topic_page.get_outer_text(), LIST.markdown)

    @not_create_topic
    def test_create_topic_markdown_num_list(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.NUM_LIST)
        self.assertEqual(create_topic_page.get_outer_text(), NUM_LIST.markdown)

    @not_create_topic
    def test_create_topic_markdown_image(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.IMAGE)
        create_topic_page.set_image(PATH_TO_IMAGE)
        self.assertIn(IMAGE.markdown, create_topic_page.get_outer_text())

    @not_create_topic
    def test_create_topic_markdown_link(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.LINK)
        create_topic_page.set_link(URl, URL_TITLE)
        self.assertIn(LINK.markdown, create_topic_page.get_outer_text())

    @not_create_topic
    def test_create_topic_markdown_link_profile(self):
        create_topic_page = fill_topic_data(self.driver)
        create_topic_page.insert_tag(Tag.LINK_PROFILE)
        create_topic_page.set_profile(PROFILE_NAME)
        profile_markdown = unicode(LINK_PROFILE.markdown, "utf-8")
        self.assertIn(profile_markdown, create_topic_page.get_outer_text())

    def tearDown(self):
        if self.post_created:
            self.topic_page.delete()
        self.driver.close()



