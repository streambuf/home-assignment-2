# _*_ coding: utf-8 _*_
__author__ = 'max'
from collections import namedtuple
import os

COMMAND_EXECUTOR_URL = 'http://127.0.0.1:4444/wd/hub'
LOGIN = 'ftest7@tech-mail.ru'
USERNAME = u'Феодулия Собакевич'
PROFILE_NAME = u'Феодулия'
TITLE = u'Тестовый заголовок'
OUTER_TEXT = u'Краткое описание темы'
INNER_TEXT = u'Текст под катом'
MAX_TITLE_LENGTH = 250
PATH_TO_IMAGE = u'/home/max/1.png'
URl = u'http://test.ru'
URL_TITLE = u'title'
BROWSER = USER_PASSWORD = os.environ['TTHA2BROWSER']

Panel = namedtuple("Panel", "text markdown html")

B = Panel('**test**', u'****', '<strong>test</strong>')
I = Panel('*test*', u'**', '<em>test</em>')
QUOTES = Panel('> test', u'> ', '&gt; test')
LIST = Panel('* test', u'* ', '<ul>\n<li>test</li>\n</ul>')
NUM_LIST = Panel('1. test', u'1. ', '<ol>\n<li>test</li>\n</ol>')
IMAGE = Panel('![](test.png)', '![](', '<img')
LINK = Panel('[name](http://test.ru "title")', '[](http://test.ru)', '<a href="http://test.ru')
LINK_PROFILE = Panel(u'[Феодулия Собакевич](/profile/f.sobakevich/)',
                     '[Феодулия Собакевич](/profile/f.sobakevich/)',
                     '<a href="/profile/f.sobakevich/">')


