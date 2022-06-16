import time

from Pages.locators_AdminPage import locators
from selenium.webdriver.support.ui import Select


class SignUP_Page:
    def __init__(self, driver):
        self.driver = driver

    def goto_signUp(self):
        signUp_link=self.driver.find_element_by_xpath(locators.signUp_link)
        signUp_link.click()

    def do_signUp(self,fname,lname,email,ph,pass1,pass2):
        firstName_textbox = self.driver.find_element_by_xpath(locators.firstName_textbox)
        firstName_textbox.send_keys(fname)
        lastName_textbox =self.driver.find_element_by_xpath(locators.lastName_textbox)
        lastName_textbox.send_keys(lname)
        emailAddr_textbox =self.driver.find_element_by_xpath(locators.emailAddr_textbox)
        emailAddr_textbox.send_keys(email)
        PhoneNo_textbox=self.driver.find_element_by_xpath(locators.PhoneNo_textbox)
        PhoneNo_textbox.send_keys(ph)
        password_textbox =self.driver.find_element_by_xpath(locators.password_textbox)
        password_textbox.send_keys(pass1)
        confirm_Password_textbox =self.driver.find_element_by_xpath(locators.confirm_Password_textbox)
        confirm_Password_textbox.send_keys(pass2)
        login_button=self.driver.find_element_by_xpath(locators.login_button)
        login_button.click()


