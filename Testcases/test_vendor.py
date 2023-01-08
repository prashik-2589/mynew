import logging

import selenium
import pytest
from selenium import webdriver
from Pageobject.loginpage import LoginPage
from Pageobject.vendorname import Vendors
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
from Utilities.readproperties import Readconfig
from Utilities.customlogger import Loggen



@pytest.mark.regression
class Test_002_login:
    baseurl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    username = "admin@yourstore.com"
    password = "admin"
    vendor_name = "vendor 1"
    logger = Loggen.loggen()
    def test_compare_vendors(self, setup):
        self.logger.info("**************start**************")
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseurl)
        self.vp = Vendors(self.driver)
        self.vp.setusername(self.username)
        self.vp.setpassword(self.password)
        self.vp.clicklogin()
        self.logger.info("**************login successfull**************")
        self.vp.click_customer()
        self.vp.click_vendor()
        self.vp.vendor_name(self.vendor_name)
        self.vp.search_vendor()
        print(self.vp.result())
        self.logger.info("**************test pass**************")
        self.driver.save_screenshot("screenshot/test_loginTitle.png")

        # for i in self.vp.result():
        #     a = print(self.vp.result().text)
        #     if a = ""
        #     assert True
        # else:
        #     assert False




