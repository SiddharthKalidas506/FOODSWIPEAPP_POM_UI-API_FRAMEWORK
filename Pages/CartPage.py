from selenium.webdriver.common.by import By


class cartpage:
    def __init__(self, driver):
        self.driver = driver

    listofiteamsincart=(By.XPATH,"//tbody[@class='MuiTableBody-root css-apqrd9-MuiTableBody-root']/tr/td[2]")
    clicktopay=(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[2]/div/div[1]/button/b")


    def get_iteamsincart(self):
        return self.driver.find_elements(*cartpage.listofiteamsincart)
    def get_clicktopay(self):
        return  self.driver.find_element(*cartpage.clicktopay)
