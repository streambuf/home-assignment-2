# _*_ coding: utf-8 _*_
__author__ = 'max'
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.page import MainPage, TopicPage, TopMenuPage, BlogPage
from utils import create_poll, create_topic_with_tag, not_create_topic, fill_topic_data
from page_objects.constants import Tag
from page_objects.action import Action
from test_constants import Panel, Const


class MainTestCase(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Remote(
            command_executor=Const.COMMAND_EXECUTOR_URL,
            desired_capabilities=getattr(DesiredCapabilities, Const.BROWSER).copy())
        self.action = Action(driver)
        main_page = MainPage(self.action)
        main_page.open()
        main_page.auth(Const.LOGIN)
        self.username = TopMenuPage(self.action).get_username()
        self.post_created = True

    @not_create_topic
    def test_create_topic_with_empty_fields(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_blog_option(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT, Const.INNER_TEXT, False)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_title(self):
        args = (self.action, '', Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_outer_text(self):
        args = (self.action, Const.TITLE, '', Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    @not_create_topic
    def test_create_topic_with_empty_inner_text(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    def test_create_topic_with_default_settings(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()

        self.topic_page = TopicPage(self.action)
        self.assertEqual(self.topic_page.get_title(), Const.TITLE)
        self.assertEqual(self.topic_page.get_text(), Const.INNER_TEXT)
        self.assertEqual(self.topic_page.get_author(), Const.USERNAME)
        self.assertTrue(self.topic_page.comment_add_link_is_displayed())
        self.topic_page.open_blog()

        blog_page = BlogPage(self.action)
        self.assertEqual(blog_page.topic.get_title(), Const.TITLE)
        self.assertEqual(blog_page.topic.get_text(), Const.OUTER_TEXT)
        self.assertEqual(blog_page.topic.get_author(), Const.USERNAME)

    @not_create_topic
    def test_create_topic_with_title_greater_max(self):
        title_greater_max = 'a' * (Const.MAX_TITLE_LENGTH + 1)
        args = (self.action, title_greater_max, Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.create_topic()
        self.assertTrue(create_topic_page.is_error())

    def test_create_topic_with_forbid_comment(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.set_forbid_comment_true()
        create_topic_page.create_topic()

        self.topic_page = TopicPage(self.action)
        self.assertFalse(self.topic_page.comment_add_link_is_displayed())

    @not_create_topic
    def test_create_topic_with_publish_false(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.set_publish_false()
        create_topic_page.create_topic()

        self.topic_page = TopicPage(self.action)
        self.topic_page.open_blog()

        blog_page = BlogPage(self.action)
        self.assertNotEqual(blog_page.topic.get_title(), Const.TITLE)

    def test_create_topic_with_tag_b(self):
        self.topic_page = create_topic_with_tag(self, Panel.B.text)
        self.assertIn(Panel.B.html, self.topic_page.get_html())

    def test_create_topic_with_tag_i(self):
        self.topic_page = create_topic_with_tag(self, Panel.I.text)
        self.assertIn(Panel.I.html, self.topic_page.get_html())

    def test_create_topic_with_tag_quotes(self):
        self.topic_page = create_topic_with_tag(self, Panel.QUOTES.text)
        self.assertIn(Panel.QUOTES.html, self.topic_page.get_html())
    #
    def test_create_topic_with_tag_list(self):
        self.topic_page = create_topic_with_tag(self, Panel.LIST.text)
        self.assertIn(Panel.LIST.html, self.topic_page.get_html())

    def test_create_topic_with_tag_num_list(self):
        self.topic_page = create_topic_with_tag(self, Panel.NUM_LIST.text)
        self.assertIn(Panel.NUM_LIST.html, self.topic_page.get_html())

    def test_create_topic_with_tag_image(self):
        self.topic_page = create_topic_with_tag(self, Panel.IMAGE.text)
        self.assertIn(Panel.IMAGE.html, self.topic_page.get_html())

    def test_create_topic_with_tag_link(self):
        self.topic_page = create_topic_with_tag(self, Panel.LINK.text)
        self.assertIn(Panel.LINK.html, self.topic_page.get_html())

    def test_create_topic_with_tag_link_profile(self):
        self.topic_page = create_topic_with_tag(self, Panel.LINK_PROFILE.text)
        self.assertIn(Panel.LINK_PROFILE.html, self.topic_page.get_html())

    @not_create_topic
    def test_create_topic_markdown_b(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.B)
        self.assertEqual(create_topic_page.get_outer_text(), Panel.B.markdown)

    @not_create_topic
    def test_create_topic_markdown_i(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.I)
        self.assertEqual(create_topic_page.get_outer_text(), Panel.I.markdown)

    @not_create_topic
    def test_create_topic_markdown_quotes(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.QUOTES)
        self.assertEqual(create_topic_page.get_outer_text(), Panel.QUOTES.markdown)

    @not_create_topic
    def test_create_topic_markdown_unordered_list(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.LIST)
        self.assertEqual(create_topic_page.get_outer_text(), Panel.LIST.markdown)

    @not_create_topic
    def test_create_topic_markdown_ordered_list(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.NUM_LIST)
        self.assertEqual(create_topic_page.get_outer_text(), Panel.NUM_LIST.markdown)

    @not_create_topic
    def test_create_topic_markdown_image_url(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.IMAGE_URL)
        create_topic_page.set_image_link(Const.PATH_TO_IMAGE)
        self.assertIn(Panel.IMAGE.markdown, create_topic_page.get_outer_text())

    @not_create_topic
    def test_create_topic_markdown_image(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.IMAGE)
        create_topic_page.set_image(Const.PATH_TO_IMAGE)
        self.assertIn(Panel.IMAGE.markdown, create_topic_page.get_outer_text())

    @not_create_topic
    def test_create_topic_markdown_link(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.LINK)
        create_topic_page.set_link(Const.URl)
        self.assertIn(Panel.LINK.markdown, create_topic_page.get_outer_text())

    @not_create_topic
    def test_create_topic_markdown_link_profile(self):
        create_topic_page = fill_topic_data(self.action)
        create_topic_page.insert_tag(Tag.LINK_PROFILE)
        create_topic_page.set_profile(Const.PROFILE_NAME)
        profile_markdown = unicode(Panel.LINK_PROFILE.markdown, "utf-8")
        self.assertIn(profile_markdown, create_topic_page.get_outer_text())

    def test_create_topic_with_poll(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_poll(self, create_topic_page)
        create_topic_page.create_topic()

        self.topic_page = TopicPage(self.action)
        answers = self.topic_page.get_poll_answers()
        self.assertIn(answers[0], Const.POLL_ANSWER1)
        self.assertIn(answers[1], Const.POLL_ANSWER2)
        self.assertIn(answers[2], Const.POLL_ANSWER3)

    @not_create_topic
    def test_create_topic_add_answer_for_poll(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.set_add_poll_true()
        create_topic_page.add_answer_for_poll()
        self.assertTrue(create_topic_page.new_answer_is_displayed())

    @not_create_topic
    def test_create_topic_del_answer_for_poll(self):
        args = (self.action, Const.TITLE, Const.OUTER_TEXT, Const.INNER_TEXT)
        create_topic_page = fill_topic_data(*args)
        create_topic_page.set_add_poll_true()
        create_topic_page.add_answer_for_poll()
        create_topic_page.delete_answer_for_poll()
        self.assertFalse(create_topic_page.new_answer_is_displayed())

    def tearDown(self):
        if self.post_created:
            self.topic_page.delete()
        self.action.close()



