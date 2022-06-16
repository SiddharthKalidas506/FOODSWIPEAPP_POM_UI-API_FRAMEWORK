from selenium.webdriver.common.by import By


class loginpage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "(//input[@id='emailId'])")
    password = (By.XPATH, "(//input[@id='password'])")
    login_button = (By.XPATH, "(//button[text()='Login'])")
    Profilename = (By.XPATH, "//div[@class='MuiToolbar-root MuiToolbar-gutters MuiToolbar-regular css-1pezmv3-MuiToolbar-root']/div/span/b")
    listofproduct=(By.XPATH,"//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-4 css-15puw3s-MuiGrid-root']/div/div/div/div/span[1]")
    addtocart=(By.XPATH,"//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-4 css-15puw3s-MuiGrid-root']/div/div/div[2]/div[2]/div/button/span[1]")


    def get_addtocart(self):
        return self.driver.find_elements(*loginpage.addtocart)

    def get_Profilenames(self):
        return self.driver.find_element(*loginpage.Profilename)

    def get_username(self):
        return self.driver.find_element(*loginpage.username)

    def get_password(self):
        return self.driver.find_element(*loginpage.password)

    def get_login_button(self):
        return self.driver.find_element(*loginpage.login_button)

    def get_login_button(self):
        return self.driver.find_element(*loginpage.login_button)

    def get_productlist(self):
        return self.driver.find_elements(*loginpage.listofproduct)