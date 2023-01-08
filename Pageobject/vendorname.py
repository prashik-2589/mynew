import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Vendors:
    customer_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    vendors_xpath = "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[4]"
    vendor_name_xpath = "//*[@id='SearchName']"
    search_xpath = "//*[@id='search-vendors']"
    search_result_xpath = "//*[@id='vendors-grid']/tbody/tr/td[1]"
    baseurl = "https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F"
    textbox_username_xpath = "//*[@id='Email']"
    textbox_password_id = "Password"
    button_login_xpath = "//button[contains(text(),'Log in')]"
    link_logout_linktext = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()


    # def clicklogout(self):
    #     self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def click_customer(self):
        self.driver.find_element(By.XPATH, self.customer_xpath).click()

    def click_vendor(self):
        self.driver.find_element(By.XPATH, self.vendors_xpath).click()

    def vendor_name(self, vendor_name):
        self.driver.find_element(By.XPATH, self.vendor_name_xpath).send_keys(vendor_name)

    def search_vendor(self):
        self.driver.find_element(By.XPATH, self.search_xpath).click()

    def result(self):
        return self.driver.find_element(By.XPATH, self.search_result_xpath).text





