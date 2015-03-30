# _*_ coding: utf-8 _*_
__author__ = 'max'
from page_objects.page import CreateTopicPage, TopicPage
from test_constants import Const


def not_create_topic(fn):
    def wrapper(*args):
        args[0].post_created = False
        return fn(*args)
    return wrapper


def fill_topic_data(action, title='', outer_text='', inner_text='', blog_select=True):
    create_topic_page = CreateTopicPage(action)
    create_topic_page.open()
    if blog_select:
        create_topic_page.blog_select_open()
        create_topic_page.blog_select_set_option_flood()
    create_topic_page.set_title(title)
    create_topic_page.set_outer_text(outer_text)
    create_topic_page.set_inner_text(inner_text)
    return create_topic_page


def create_topic_with_tag(self, inner_text):
    args = (self.action, Const.TITLE, Const.OUTER_TEXT, inner_text)
    create_topic_page = fill_topic_data(*args)
    create_topic_page.create_topic()
    return TopicPage(self.action)


def create_poll(self, create_topic_page):
    create_topic_page.set_add_poll_true()
    create_topic_page.add_answer_for_poll()
    create_topic_page.set_question_poll(Const.POLL_QUESTION)
    create_topic_page.set_answer_poll(0, Const.POLL_ANSWER1)
    create_topic_page.set_answer_poll(1, Const.POLL_ANSWER2)
    create_topic_page.set_answer_poll(2, Const.POLL_ANSWER3)