import os

import  requests
import json
import jsonpath

from Utils.XLConfig import XLConfig

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



class Test_API_uswerService:

    def test_1_loginUser(self):
        login_User_url = "https://may-hasherfoodswipe-backend-user-urtjok3rza-wl.a.run.app/v1/public/user/login-user"
        file = open(BASE_DIR + "/TestData/loginUser.json")
        json_ip = file.read()
        request_json = json.loads(json_ip)
        response = requests.post(login_User_url, json=request_json)
        try:
            assert response.status_code == 200
            resp_json=response.headers.get('authorization')
            print(resp_json)
            sht = 'API_URL'
            loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
            XLConfig.writeData(loc,sht,2,10,resp_json)
        except:
            resp = response.text
            assert False

    def test2_2_getMenu(self):
        category='Dinner'
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        toc=XLConfig.readData(loc,sht,2,10)
        menu_url="https://may-hasherfoodswipe-backend-api-urtjok3rza-wl.a.run.app/search-service/v1/auth/search/getAllMenuByCategory/"+category
        headers_dict = {"Authorization": "Bearer " + toc}
        resp = requests.get(menu_url, headers=headers_dict)
        try:
            assert resp.status_code==200
            #print(resp.text)
        except:
            assert False

    def test2_3_getItem(self):
        item='MangoShake'
        sht = 'API_URL'
        loc = BASE_DIR + "/TestData/FoodSwipeDatabase.xlsx"
        toc=XLConfig.readData(loc,sht,2,10)
        menu_url="https://may-hasherfoodswipe-backend-api-urtjok3rza-wl.a.run.app/search-service/v1/auth/search/getAllMenuByMenuCategory/Other%20Items/"+item
        headers_dict = {"Authorization": "Bearer " + toc}
        resp = requests.get(menu_url, headers=headers_dict)
        try:
            assert resp.status_code==200
            #print(resp.text)
        except:
            assert False







