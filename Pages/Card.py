from selenium.webdriver.common.by import By


class cartandpayment:
    def __init__(self, driver):
        self.driver = driver



    MyCart = (By.XPATH, "(//span[text()='My Cart'])")
    Item1name = (By.XPATH, "(//tbody/tr[1]/td[2])")
    Item1price = (By.XPATH, "(//tbody/tr[1]/td[5])")
    #Item2name = (By.XPATH, "(//tbody/tr[2]/td[2])")
    #Item2price = (By.XPATH, "(//tbody/tr[2]/td[5])")
    Clicktopay = (By.XPATH, "(//b[text()='Click To Pay'])")
    Paymentname= (By.XPATH, "(//input[@id='cname'])")
    Paymentnumber=(By.XPATH,"(//input[@id='ccnum'])")
    Expmonth=(By.XPATH,"(//input[@id='expmonth'])")
    Expyear=(By.XPATH,"(//input[@id='expyear'])")
    CVV=(By.XPATH,"(//input[@id='cvv'])")
    Continue=(By.XPATH,"(//input[@class='confirm-btn'])")


    def get_Mycart(self):
        return self.driver.find_element(*cartandpayment.MyCart)

    def get_Itemname(self):
        return self.driver.find_element(*cartandpayment.Item1name)

    def get_Itemprice(self):
        return self.driver.find_element(*cartandpayment.Item1price)

    def get_Clicktopay(self):
        return self.driver.find_element(*cartandpayment.Clicktopay)

    def get_Paymentname(self):
        return self.driver.find_element(*cartandpayment.Paymentname)

    def get_Paymentnumber(self):
        return self.driver.find_element(*cartandpayment.Paymentnumber)

    def get_Expyear(self):
        return self.driver.find_element(*cartandpayment.Expyear)

    def get_CVV(self):
        return self.driver.find_element(*cartandpayment.CVV)

    def get_Continue(self):
        return self.driver.find_element(*cartandpayment.Continue)
        self.driver.switchTo().alert().getText()
