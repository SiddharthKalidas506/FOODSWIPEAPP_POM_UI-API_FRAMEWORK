import time

from Pages.locators_AdminPage import locators

class SignInPage:
    def __init__(self,driver):
        self.driver=driver

    def do_login(self,username,password):
        emailId_textbox=self.driver.find_element_by_xpath(locators.emailId_textbox)
        emailId_textbox.send_keys(username)
        # driver.execute_script("arguments[0].scrollIntoView();", emailId_textbox)
        password_textbox=self.driver.find_element_by_xpath(locators.password_textbox)
        password_textbox.send_keys(password)
        login_button=self.driver.find_element_by_xpath(locators.login_button)
        login_button.click()


