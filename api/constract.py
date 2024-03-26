# 合同上传接口

import requests

from config import BASE_URL


class ConstractApi:
    def __init__(self):
        # self.url_upload_constract = "http://kdtx-test.itheima.net/api/common/upload"
        self.url_upload_constract =BASE_URL +  "/api/common/upload"
        # self.url_add_constract = "http://kdtx-test.itheima.net/api/contract"
        self.url_add_constract = BASE_URL + "/api/contract"

    # 上传合同
    def upload_constract(self,test_data,token):
        return requests.post(url=self.url_upload_constract,headers={"Authorization":token},files={"file":test_data})
    # 新增合同
    def add_constract(self,test_data,token):
        return requests.post(url= self.url_add_constract,headers={"Authorization":token},json=test_data)