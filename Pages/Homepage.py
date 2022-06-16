from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class homepage:
    def __init__(self, driver):
        self.driver = driver

    Menu = (By.XPATH, "(//span[text()='Menu'])")
    signin = (By.XPATH, "(//a[text()=' Login '])")
    All_other_items = (By.XPATH, "(//span[text()='ALL OTHER ITEMS'])")
    product1 = (By.XPATH,
                "(//span[@class='MuiTypography-root MuiTypography-h5 MuiCardHeader-title css-1qvr50w-MuiTypography-root'])")
    Addcart = (By.XPATH,
               "//button[@class='MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root  css-sghohy-MuiButtonBase-root-MuiButton-root']")
    Addedsuccess = (
    By.XPATH, "(//*[@id='root']/div/div[1]/div[2]/div[2]/div[3]/div/div/div[1]/div/div[2]/div[2]/div/div)")
    Itemunavaialble = (By.XPATH, "(//div[text()=" "Item unavailable!""])")

    # other section
    Dinner=(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div[2]/div/div/button[5]")
    Breakfast=(By.XPATH,"(//span[text()='BREAKFAST'])")
    Lunch=(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div[2]/div/div/button[3]")
    Snacks=(By.XPATH,"//*[@id='root']/div/div[1]/div[2]/div[2]/div[2]/div/div/button[4]")
    listofproduct = (By.XPATH, "//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-4 css-15puw3s-MuiGrid-root']/div/div/div/div/span[1]")
    addtocart = (By.XPATH,"//div[@class='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-4 css-15puw3s-MuiGrid-root']/div/div/div[2]/div[2]/div/button")
    Mycart=(By.XPATH,"//*[@id='root']/div/div[1]/div[1]/div/nav/div/div[2]")


    def get_Menu(self):
        return self.driver.find_element(*homepage.Menu)

    def get_All_other_items(self):
        return self.driver.find_element(*homepage.All_other_items)

    def get_product1(self):
        return self.driver.find_element(*homepage.product1)

    def get_Addcart(self):
        return self.driver.find_element(*homepage.Addcart)

    def get_Addedsuccess(self):
        return self.driver.find_element(*homepage.Addedsuccess)

    def get_selectdineer(self):
        return self.driver.find_element(*homepage.Dinner)

    def get_productlist(self):
        return self.driver.find_elements(*homepage.listofproduct)

    def get_addtocart(self):
        return self.driver.find_elements(*homepage.addtocart)

    def get_Breakfast(self):
        return self.driver.find_element(*homepage.Breakfast)

    def get_gotomycart(self):
        return self.driver.find_element(*homepage.Mycart)

    def get_selectLunch(self):
        return  self.driver.find_element(*homepage.Lunch)

    def get_selectSnacks(self):
        return self.driver.find_element(*homepage.Snacks)