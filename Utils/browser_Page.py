
import os
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class TestData:
    #Login test Data
    chrome_path=BASE_DIR+"/drivers/chromedriver"
    base_url='https://may-hasherfoodswipe-frontend-urtjok3rza-wl.a.run.app/login'

    excel_location=BASE_DIR+"/TestData/FoodSwipeDatabase.xlsx"

#     User
    BASEURL = "https://may-hasherfoodswipe-frontend-urtjok3rza-wl.a.run.app/Login"
    productlist = []
    pricelist = []
    admin_test_data_file_path = BASE_DIR+"/TestData/FoodSwipeDatabase.xlsx"




