# _*_ coding: utf-8 _*_
__author__ = 'max'

import os
from locators import TopicLocators, TopMenuLocators, CreateTopicLocators, MainPageLocators
from constants import Tag

USER_PASSWORD = os.environ['TTHA2PASSWORD']
PANEL1 = 0
PANEL2 = 1


class BasePage(object):
    def __init__(self, action):
        self.action = action


class MainPage(BasePage):
    MAIN_PAGE_URL = 'http://ftest.stud.tech-mail.ru'

    def open(self):
        self.action.open_page(self.MAIN_PAGE_URL)

    def auth(self, login):
        self.action.click(MainPageLocators.SHOW_LOGIN_FORM_BUTTON)
        self.action.input(MainPageLocators.LOGIN_FIELD, login)
        self.action.input(MainPageLocators.PASSWORD_FIELD, USER_PASSWORD)
        self.action.submit(MainPageLocators.LOGIN_BUTTON)


class TopMenuPage(BasePage):
    def get_username(self):
        return self.action.get_text_with_wait(TopMenuLocators.USERNAME)


class TopicPage(BasePage):
    def get_title(self):
        return self.action.get_text_with_wait(TopicLocators.TITLE)

    def get_text(self):
        return self.action.get_text_with_wait(TopicLocators.TEXT)

    def get_html(self):
        return self.action.get_attr_with_wait(TopicLocators.CONTENT, 'innerHTopMenuLocators')

    def get_author(self):
        return self.action.get_text_with_wait(TopicLocators.AUTHOR)

    def open_blog(self):
        return self.action.click(TopicLocators.BLOG)

    def delete(self):
        self.action.click(TopicLocators.DELETE_BUTTON)
        self.action.click(TopicLocators.DELETE_BUTTON_CONFIRM)

    def comment_add_link_is_displayed(self):
        return self.action.is_exists(TopicLocators.COMMENT_ADD_LINK)

    def get_poll_answers(self):
        return [
            self.action.get_text_with_wait(TopicLocators.LABEL_ANSWER1),
            self.action.get_text_with_wait(TopicLocators.LABEL_ANSWER2),
            self.action.get_text_with_wait(TopicLocators.LABEL_ANSWER3)]


class BlogPage(BasePage):
    @property
    def topic(self):
        return TopicPage(self.action)


class CreateTopicPage(BasePage):
    CREATE_TOPIC_PAGE_URL = 'http://ftest.stud.tech-mail.ru/blog/topic/create/'

    def open(self):
        self.action.open_page(self.CREATE_TOPIC_PAGE_URL)
        TopMenuPage(self.action).get_username()

    def create_topic(self):
        self.action.submit(CreateTopicLocators.CREATE_TOPIC_BUTTON)

    def is_error(self):
        return self.action.wait_is_displayed(CreateTopicLocators.SYSTEM_MESSAGE_ERROR)

    def blog_select_open(self):
        self.action.click(CreateTopicLocators.BLOGSELECT)

    def blog_select_set_option_flood(self):
        self.action.click(CreateTopicLocators.OPTION_FLOOD)

    def set_title(self, title):
        self.action.input(CreateTopicLocators.TITLE, title)

    def set_outer_text(self, outer_text):
        self.action.input_num_with_imitation_user(CreateTopicLocators.TEXT_AREA, outer_text, PANEL1)

    def set_inner_text(self, inner_text):
        self.action.input_num_with_imitation_user(CreateTopicLocators.TEXT_AREA, inner_text, PANEL2)

    def set_forbid_comment_true(self):
        self.action.click_if_not_selected(CreateTopicLocators.FORBID_COMMENT_CHECKBOX)

    def set_publish_false(self):
        self.action.click_if_selected(CreateTopicLocators.PUBLISH_CHECKBOX)

    def insert_tag(self, tag):
        locator = {
            Tag.B: CreateTopicLocators.BUTTON_B,
            Tag.I: CreateTopicLocators.BUTTON_I,
            Tag.QUOTES: CreateTopicLocators.BUTTON_QUOTES,
            Tag.LIST: CreateTopicLocators.BUTTON_LIST,
            Tag.NUM_LIST: CreateTopicLocators.BUTTON_NUM_LIST,
            Tag.IMAGE: CreateTopicLocators.BUTTON_IMAGE,
            Tag.IMAGE_URL: CreateTopicLocators.BUTTON_IMAGE_URL,
            Tag.LINK: CreateTopicLocators.BUTTON_LINK,
            Tag.LINK_PROFILE: CreateTopicLocators.BUTTON_LINK_PROFILE
        }[tag]
        self.action.click_num(locator, PANEL1)

    def set_image(self, path):
        self.action.execute_script('$(".markdown-upload-photo-container").show()')
        self.action.input_num(CreateTopicLocators.INPUT_FILE, path, PANEL1)
        self.action.wait_is_displayed(CreateTopicLocators.IMAGE_STRING)

    def set_image_link(self, path):
        self.action.set_text_alert(path)

    def set_link(self, url):
        self.action.set_text_alert(url)

    def set_profile(self, profile_name):
        self.action.input(CreateTopicLocators.SEARCH_USER_FIELD, profile_name)
        self.action.wait_element_attaching(CreateTopicLocators.USER_PROFILE_LINK)
        self.action.wait_is_displayed(CreateTopicLocators.USER_PROFILE_LINK)
        self.action.click(CreateTopicLocators.USER_PROFILE_LINK)

    def get_outer_text(self):
        return self.action.get_text_with_wait(CreateTopicLocators.OUTER_AREA)

    def set_add_poll_true(self):
        self.action.click_if_not_selected(CreateTopicLocators.ADD_POLL_CHECKBOX)

    def add_answer_for_poll(self):
        self.action.click(CreateTopicLocators.ADD_ANSWER_LINK)

    def delete_answer_for_poll(self):
        self.action.click(CreateTopicLocators.DELETE_POLL_ANSWER)

    def new_answer_is_displayed(self):
        return self.action.is_displayed(CreateTopicLocators.POLL_ANSWER3_FIELD)

    def set_question_poll(self, question):
        self.action.input(CreateTopicLocators.POLL_QUESTION_FIELD, question)

    def set_answer_poll(self, num_answer, answer):
        locator = {
            0: CreateTopicLocators.POLL_ANSWER1_FIELD,
            1: CreateTopicLocators.POLL_ANSWER2_FIELD,
            2: CreateTopicLocators.POLL_ANSWER3_FIELD
        }[num_answer]
        self.action.input(locator, answer)



