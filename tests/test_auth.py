# _*_ coding: utf-8 _*_
__author__ = 'max'
import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from page_objects.page import MainPage, TopMenuPage
from page_objects.action import Action
from test_constants import Const


class AuthTestCase(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Remote(
            command_executor=Const.COMMAND_EXECUTOR_URL,
            desired_capabilities=getattr(DesiredCapabilities, Const.BROWSER).copy())
        self.action = Action(driver)

    def test_auth(self):
        main_page = MainPage(self.action)
        main_page.open()
        main_page.auth(Const.LOGIN)
        self.username = TopMenuPage(self.action).get_username()
        self.assertEqual(self.username, Const.USERNAME)

    def tearDown(self):
        self.action.close()