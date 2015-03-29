# _*_ coding: utf-8 _*_
__author__ = 'max'

import os
from locators import *
from constants import Tag
from action import Action

USER_PASSWORD = os.environ['TTHA2PASSWORD']
NUM_OUTER_PANEL = 1
NUM_PROFILE = 1


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.action = Action(self.driver)


class MainPage(BasePage):
    MAIN_PAGE_URL = 'http://ftest.stud.tech-mail.ru'

    def open(self):
        self.action.open_page(self.MAIN_PAGE_URL)

    def auth(self, login):
        self.action.click(MPL.SHOW_LOGIN_FORM_BUTTON)
        self.action.input(MPL.LOGIN_FIELD, login)
        self.action.input(MPL.PASSWORD_FIELD, USER_PASSWORD)
        self.action.submit(MPL.LOGIN_BUTTON)


class TopMenuPage(BasePage):
    def get_username(self):
        return self.action.get_text_with_wait(TML.USERNAME)


class TopicPage(BasePage):
    def get_title(self):
        self.action.get_text_with_wait(TL.TITLE)

    def get_text(self):
        self.action.get_text_with_wait(TL.TEXT)

    def get_html(self):
        self.action.get_attr_with_wait(TL.CONTENT, 'innerHTML')

    def get_author(self):
        self.action.get_text_with_wait(TL.AUTHOR)

    def open_blog(self):
        self.action.click(TL.BLOG)

    def delete(self):
        self.action.click(TL.DELETE_BUTTON)
        self.action.click(TL.DELETE_BUTTON_CONFIRM)

    def comment_add_link_is_displayed(self):
        self.action.is_exists(TL.COMMENT_ADD_LINK)


class BlogPage(BasePage):
    @property
    def topic(self):
        return TopicPage(self.driver)


class CreateTopicPage(BasePage):
    CREATE_TOPIC_PAGE_URL = 'http://ftest.stud.tech-mail.ru/blog/topic/create/'

    def open(self):
        self.action.open_page(self.CREATE_TOPIC_PAGE_URL)
        self.action.execute_script('$("#id_text_short").show()')
        TopMenuPage(self.driver).get_username()

    def create_topic(self):
        self.action.submit(CTL.CREATE_TOPIC_BUTTON)

    def is_error(self):
        return self.action.is_displayed(CTL.SYSTEM_MESSAGE_ERROR)

    def blog_select_open(self):
        self.action.click(CTL.BLOGSELECT)

    def blog_select_set_option_flood(self):
        self.action.click(CTL.OPTION_FLOOD)

    def set_title(self, title):
        self.action.input(CTL.TITLE, title)

    def set_outer_text(self, outer_text):
        self.action.input(CTL.SHORT_TEXT, outer_text)

    def set_inner_text(self, inner_text):
        self.action.input(CTL.MAIN_TEXT, inner_text)

    def set_forbid_comment_true(self):
        self.action.click_if_not_selected(CTL.FORBID_COMMENT_CHECKBOX)

    def set_publish_false(self):
        self.action.click_if_selected(CTL.PUBLISH_CHECKBOX)

    def insert_tag(self, tag):
        locator = {
            Tag.H4: CTL.BUTTON_H4,
            Tag.H5: CTL.BUTTON_H5,
            Tag.H6: CTL.BUTTON_H6,
            Tag.B: CTL.BUTTON_B,
            Tag.I: CTL.BUTTON_I,
            Tag.QUOTES: CTL.BUTTON_QUOTES,
            Tag.CODE: CTL.BUTTON_CODE,
            Tag.LIST: CTL.BUTTON_LIST,
            Tag.NUM_LIST: CTL.BUTTON_NUM_LIST,
            Tag.IMAGE: CTL.BUTTON_IMAGE,
            Tag.LINK: CTL.BUTTON_LINK,
            Tag.LINK_PROFILE: CTL.BUTTON_LINK_PROFILE
        }[tag]
        self.action.click_num(locator, NUM_OUTER_PANEL)

    def set_image(self, path):
        self.action.execute_script('$(".markdown-upload-photo-container").show()')
        self.action.input_num(CTL.INPUT_FILE, NUM_OUTER_PANEL, path)
        self.action.wait_input_text(CTL.SHORT_TEXT, 'value')

    def set_link(self, url, title):
        self.action.set_text_alert(url)
        self.action.set_text_alert(title)

    def set_profile(self, profile_name):
        self.action.input(CTL.SEARCH_USER_FIELD, profile_name)
        self.action.wait_is_displayed(CTL.USER_PROFILE_LINK)
        self.action.click(CTL.USER_PROFILE_LINK)

    def get_outer_text(self):
        return self.action.get_attr(CTL.SHORT_TEXT, 'value')

    def set_add_poll_true(self):
        self.action.click_if_selected(CTL.ADD_POLL_CHECKBOX)

    def add_answer_for_poll(self):
        self.action.click(CTL.ADD_ANSWER_LINK)

    def set_question_poll(self, question):
        self.action.input(CTL.POLL_QUESTION_FIELD, question)

    def set_answer_poll(self, num_answer, answer):
        locator = {
            0: CTL.POLL_ANSWER1_FIELD,
            1: CTL.POLL_ANSWER2_FIELD,
            2: CTL.POLL_ANSWER3_FIELD
        }[num_answer]
        self.action.input(locator, answer)



