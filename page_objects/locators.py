# _*_ coding: utf-8 _*_
__author__ = 'max'
from selenium.webdriver.common.by import By


class MPL(object):
    SHOW_LOGIN_FORM_BUTTON = (By.CLASS_NAME, 'button-login')
    LOGIN_FIELD = (By.XPATH, '//input[@name="login"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@name="password"]')
    LOGIN_BUTTON = (By.ID, 'popup-login-form')


class TML(object):
    USERNAME = (By.XPATH, '//a[@class="username"]')


class TL(object):
    NOTICE = (By.CLASS_NAME, 'system-message-notice')
    TITLE = (By.XPATH, '//*[@class="topic-title"]/a')
    TEXT = (By.XPATH, '//*[@class="topic-content text"]/p')
    CONTENT = (By.CLASS_NAME, 'topic-content')
    BLOG = (By.XPATH, '//*[@class="topic-blog"]')
    DELETE_BUTTON = (By.XPATH, '//a[@class="actions-delete"]')
    DELETE_BUTTON_CONFIRM = (By.XPATH, '//input[@value="Удалить"]')
    AUTHOR = (By.XPATH, '//a[@rel="author"]')
    COMMENT_ADD_LINK = (By.CLASS_NAME, 'comment-add-link')
    LABEL_ANSWER1 = (By.XPATH, '//*[@class=("poll-vote")]/li[1]/label')
    LABEL_ANSWER2 = (By.XPATH, '//*[@class=("poll-vote")]/li[2]/label')
    LABEL_ANSWER3 = (By.XPATH, '//*[@class=("poll-vote")]/li[3]/label')


class CTL(object):
    CREATE_TOPIC_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SYSTEM_MESSAGE_ERROR = (By.CLASS_NAME, 'system-message-error')
    BLOGSELECT = (By.XPATH, '//a[@class="chzn-single"]')
    OPTION_FLOOD = (By.XPATH, '//li[text()="Флудилка"]')
    TITLE = (By.XPATH, '//input[@name="title"]')
    TEXT_AREA = (By.CLASS_NAME, 'CodeMirror-scroll')
    FORBID_COMMENT_CHECKBOX = (By.ID, 'id_forbid_comment')
    PUBLISH_CHECKBOX = (By.ID, 'id_publish')
    ADD_POLL_CHECKBOX = (By.NAME, 'add_poll')
    POLL_QUESTION_FIELD = (By.ID, 'id_question')
    POLL_ANSWER1_FIELD = (By.ID, 'id_form-0-answer')
    POLL_ANSWER2_FIELD = (By.ID, 'id_form-1-answer')
    POLL_ANSWER3_FIELD = (By.XPATH, '//*[contains(@id, "id_form-2-answer")][2]')
    ADD_ANSWER_LINK = (By.CLASS_NAME, 'add-poll-answer')
    INPUT_FILE = (By.NAME, 'filedata')
    BUTTON_B = (By.CLASS_NAME, 'markdown-editor-icon-bold')
    BUTTON_I = (By.CLASS_NAME, 'markdown-editor-icon-italic')
    BUTTON_QUOTES = (By.CLASS_NAME, 'markdown-editor-icon-quote')
    BUTTON_LIST = (By.CLASS_NAME, 'markdown-editor-icon-unordered-list')
    BUTTON_NUM_LIST = (By.CLASS_NAME, 'markdown-editor-icon-ordered-list')
    BUTTON_IMAGE_URL = (By.XPATH, '//*[contains(@class, "markdown-editor-icon-image")][1]')
    BUTTON_IMAGE = (By.XPATH, '//*[contains(@class, "markdown-editor-icon-image")][2]')
    BUTTON_LINK = (By.XPATH, '//*[contains(@class, "markdown-editor-icon-link")][1]')
    BUTTON_LINK_PROFILE = (By.XPATH, '//*[contains(@class, "markdown-editor-icon-link")][2]')
    SEARCH_USER_FIELD = (By.ID, 'search-user-login-popup')
    USER_PROFILE_LINK = (By.CSS_SELECTOR, '.realname>.user_profile_path')
    OUTER_AREA = (By.XPATH, '//div[@class="CodeMirror-code"]/pre')
    IMAGE_STRING = (By.CLASS_NAME, 'cm-string')
    DELETE_POLL_ANSWER = (By.XPATH, '//*[@id="question_list"]/li[3]/a')


