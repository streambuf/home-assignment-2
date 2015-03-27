# _*_ coding: utf-8 _*_
__author__ = 'max'
from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SHOW_LOGIN_FORM_BUTTON = (By.CLASS_NAME, 'button-login')
    LOGIN_FIELD = (By.XPATH, '//input[@name="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.ID, 'popup-login-form')


class TopMenuLocators(object):
    USERNAME = (By.XPATH, '//a[@class="username"]')


class TopicLocators(object):
    NOTICE = (By.CLASS_NAME, 'system-message-notice')
    TITLE = (By.XPATH, '//*[@class="topic-title"]/a')
    TEXT = (By.XPATH, '//*[@class="topic-content text"]/p')
    CONTENT = (By.CLASS_NAME, 'topic-content')
    BLOG = (By.XPATH, '//*[@class="topic-blog"]')
    DELETE_BUTTON = (By.XPATH, '//a[@class="actions-delete"]')
    DELETE_BUTTON_CONFIRM = (By.XPATH, '//input[@value="Удалить"]')
    AUTHOR = (By.XPATH, '//a[@rel="author"]')
    COMMENT_ADD_LINK = (By.CLASS_NAME, 'comment-add-link')


class CreateTopicLocators(object):
    CREATE_TOPIC_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SYSTEM_MESSAGE_ERROR = (By.CLASS_NAME, 'system-message-error')
    BLOGSELECT = (By.XPATH, '//a[@class="chzn-single"]')
    OPTION_FLOOD = (By.XPATH, '//li[text()="Флудилка"]')
    TITLE = (By.XPATH, '//input[@name="title"]')
    SHORT_TEXT = (By.XPATH, '//textarea[@name="text_short"]')
    MAIN_TEXT = (By.XPATH, '//textarea[@id="id_text"]')
    FORBID_COMMENT_CHECKBOX = (By.ID, 'id_forbid_comment')
    PUBLISH_CHECKBOX = (By.ID, 'id_publish')
    MARKDOWN_H4 = (By.CLASS_NAME, 'editor-h4')
