import time

from Pages.locators_AdminPage import locators
from selenium.webdriver.support.ui import Select


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def do_logout(self):
        accountHolder_nameIcon_button=self.driver.find_element_by_xpath(locators.accountHolder_nameIcon_button)
        accountHolder_nameIcon_button.click()
        logout_link=self.driver.find_element_by_xpath(locators.logout_link)
        logout_link.click()

    def goto_settings(self):
        accountHolder_nameIcon_button = self.driver.find_element_by_xpath(locators.accountHolder_nameIcon_button)
        accountHolder_nameIcon_button.click()
        settings_link=self.driver.find_element_by_xpath(locators.settings_link)
        settings_link.click()

    def do_clickAddItems(self):
        addItem_button=self.driver.find_element_by_xpath(locators.addItem_button)
        addItem_button.click()

    def do_addItems(self,iName,iDesc,price,cat,quantity):
        itemName_textbox =self.driver.find_element_by_xpath(locators.itemName_textbox)
        itemName_textbox.send_keys(iName)
        itemDesc_textbox = self.driver.find_element_by_xpath(locators.itemDesc_textbox)
        itemDesc_textbox.send_keys(iDesc)
        Price_textbox = self.driver.find_element_by_xpath(locators.Price_textbox)
        Price_textbox.send_keys(price)

        category_dropdown = self.driver.find_element_by_xpath(locators.category_dropdown)
        category_dropdown.click()
        self.driver.find_element_by_xpath("//li[contains(text(),'"+cat+"')]").click()
        # se = Select(category_dropdown)
        # se.select_by_index(2)

        quantity_textbox = self.driver.find_element_by_xpath(locators.quantity_textbox)
        quantity_textbox.send_keys(quantity)
        mnuStatus_enable_radio=self.driver.find_element_by_xpath(locators.mnuStatus_enable_radio)
        mnuStatus_enable_radio.click()
        submit_button=self.driver.find_element_by_xpath(locators.submit_button)
        submit_button.click()

    def successLink_isvisible(self):
        successmsg_link = self.driver.find_element_by_xpath(locators.successmsg_link)
        successmsg_link.isDisplayed()

    def get_successLink(self):
        successmsg_link=self.driver.find_element_by_xpath(locators.successmsg_link)
        return successmsg_link.text
    def close_addItemScreen(self):
        close_icon=self.driver.find_element_by_xpath(locators.close_icon)
        close_icon.click()

    def do_searchItem(self,item):
        searchItem_textbox=self.driver.find_element_by_xpath(locators.searchItem_textbox)
        searchItem_textbox.send_keys(item)

    def goto_settings(self):
        accountHolder_nameIcon_button = self.driver.find_element_by_xpath(locators.accountHolder_nameIcon_button)
        accountHolder_nameIcon_button.click()
        settings_link=self.driver.find_element_by_xpath(locators.settings_link)
        settings_link.click()


    def click_adduser(self):
        addUser_button=self.driver.find_element_by_xpath(locators.addUser_button)
        addUser_button.click()

    def addUser_Employee(self,fname,lname,email,ph):
        firstName_textbox = self.driver.find_element_by_xpath(locators.firstName_textbox)
        firstName_textbox.send_keys(fname)
        lastName_textbox = self.driver.find_element_by_xpath(locators.lastName_textbox)
        lastName_textbox.send_keys(lname)
        emailAddr_textbox = self.driver.find_element_by_xpath(locators.emailAddr_textbox)
        emailAddr_textbox.send_keys(email)
        PhoneNo_textbox = self.driver.find_element_by_xpath(locators.PhoneNo_textbox)
        PhoneNo_textbox.send_keys(ph)
        employee_radio = self.driver.find_element_by_xpath(locators.employee_radio)
        employee_radio.click()
        submit_button = self.driver.find_element_by_xpath(locators.submit_button)
        submit_button.click()

    def addUser_Admin(self,fname,lname,email,ph):
        firstName_textbox = self.driver.find_element_by_xpath(locators.firstName_textbox)
        firstName_textbox.send_keys(fname)
        lastName_textbox = self.driver.find_element_by_xpath(locators.lastName_textbox)
        lastName_textbox.send_keys(lname)
        emailAddr_textbox = self.driver.find_element_by_xpath(locators.emailAddr_textbox)
        emailAddr_textbox.send_keys(email)
        PhoneNo_textbox = self.driver.find_element_by_xpath(locators.PhoneNo_textbox)
        PhoneNo_textbox.send_keys(ph)
        admin_radio=self.driver.find_element_by_xpath(locators.admin_radio)
        admin_radio.click()
        submit_button = self.driver.find_element_by_xpath(locators.submit_button)
        submit_button.click()

    def setAvailabilityCheckbox(self):
        availability_checkbox1=self.driver.find_element_by_xpath(locators.availability_checkbox1)
        availability_checkbox1.click()










