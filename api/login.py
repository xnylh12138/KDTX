import requests
from config import BASE_URL
class Get_login:
    def __init__(self):
        self.url_Image=BASE_URL+ "/api/captchaImage"
        self.url_login=BASE_URL+"/api/login"
    def get_Image(self):
        return requests.get(self.url_Image)

    def get_login(self,json_data):
        return requests.post(url=self.url_login,json=json_data)