# _*_ coding: utf-8 _*_
__author__ = 'max'
from collections import namedtuple
import os


class Const(object):
    COMMAND_EXECUTOR_URL = 'http://127.0.0.1:4444/wd/hub'
    LOGIN = 'ftest7@tech-mail.ru'
    USERNAME = u'Феодулия Собакевич'
    PROFILE_NAME = u'Феодулия'
    TITLE = u'Тестовый заголовок'
    OUTER_TEXT = u'Краткое описание темы'
    INNER_TEXT = u'Текст под катом'
    MAX_TITLE_LENGTH = 250
    PATH_TO_IMAGE = os.path.dirname(__file__) + '/img/kotik.jpg'
    URl = u'http://test.ru'
    POLL_QUESTION = u'Вопрос для голосования'
    POLL_ANSWER1 = u'Answer1'
    POLL_ANSWER2 = u'Answer2'
    POLL_ANSWER3 = u'Answer3'
    BROWSER = os.environ['TTHA2BROWSER']

PanelTuple = namedtuple("Panel", "text markdown html")


class Panel(object):
    B = PanelTuple('**test**', u'****', '<strong>test</strong>')
    I = PanelTuple('*test*', u'**', '<em>test</em>')
    QUOTES = PanelTuple('> test', u'> ', '&gt; test')
    LIST = PanelTuple('* test', u'* ', '<ul>\n<li>test</li>\n</ul>')
    NUM_LIST = PanelTuple('1. test', u'1. ', '<ol>\n<li>test</li>\n</ol>')
    IMAGE = PanelTuple('![](test.png)', '![](', '<img')
    LINK = PanelTuple('[name](http://test.ru "title")', '[](http://test.ru)', '<a href="http://test.ru')
    LINK_PROFILE = PanelTuple(u'[Феодулия Собакевич](/profile/f.sobakevich/)',
                         '[Феодулия Собакевич](/profile/f.sobakevich/)',
                         '<a href="/profile/f.sobakevich/">')


