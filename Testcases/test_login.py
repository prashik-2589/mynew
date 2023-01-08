import logging

import selenium
import pytest
from selenium import webdriver
from Pageobject.loginpage import LoginPage
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from Utilities.customlogger import Loggen


class Test_001_login:
    baseurl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    logger = Loggen.loggen()


    def test_homepagetitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Your store. Login":
            assert True
            self.logger.info("*********test home page is pass************")
        else:
            self.logger.info("**************home page login is failed***************")
            assert False

#     @pytest.mark.regression
#     def test_login(self, setup):
#         self.driver = setup
#         self.driver.get(self.baseurl)
#         self.lp = LoginPage(self.driver)
#         self.lp.setusername(self.username)
#         self.lp.setpassword(self.password)
#         self.lp.clicklogin()
#         act_title = self.driver.title
#         if act_title == "Dashboard / nopCommerce administration":
#             assert True
#             self.logger.info("**********test login is pass************")
#         else:
#             self.driver.save_screenshot(".\\Screenshots\\" + "test_loginTitle.png")
#             self.driver.close()
#             assert False
# # #
#
#
#
#
