from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class orderhistorypage:
    def __init__(self, driver):
        self.driver = driver

    Menu = (By.XPATH, "(//span[text()='Menu'])")
    # signin = (By.XPATH, "(//a[text()=' Login '])")
    orderhistory = (By.XPATH, "(//span[text()='Order History'])")
    viewdetails = (By.XPATH, "(//u[text()='View Details'])")
    viewdetails_xpath = "//u[text()='View Details']"
    cancelorder = (By.XPATH, "(//button[@class='cancel-order'])")
    order_accepted = (By.XPATH, "(//div[@class='order-pending'])")
    order_accepted_xpath = "(//div[@class='order-pending'])"
    order_cancelled = (By.XPATH, "(//div[@class='pay-failure'])")
    order_cancelled_xpath = "(//div[@class='pay-failure'])"

    def get_Menu(self):
        return self.driver.find_element(*orderhistorypage.Menu)

    def get_orderhistory(self):
        return self.driver.find_element(*orderhistorypage.orderhistory)

    def get_viewdetails(self):
        return self.viewdetails_xapth

    def get_cancelorder(self):
        return self.driver.find_element(*orderhistorypage.cancelorder)

    def get_order_accepted(self):
        return self.driver.find_element(*orderhistorypage.order_accepted)

    def get_order_cancelled(self):
        return self.driver.find_element(*orderhistorypage.order_cancelled)

    def get_index_order(self,productpath):
        self.elements = self.driver.find_elements(By.XPATH, productpath)
        count=0
        for i in self.elements:
            count=count+1
        j= str(count)
        return j

    def get_getthetext(self):
        return self.driver.find_elements(*orderhistorypage.orderstatus)
