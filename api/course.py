# 封装课程接口测试类

import requests
from config import BASE_URL
class CourseApi:
    def __init__(self):
        # self.url_add_course = "http://kdtx-test.itheima.net/api/clues/course"
        self.url_add_course = BASE_URL + "/api/clues/course"
        self.url_select_course = BASE_URL + "/api/clues/course/list"
    def add_course(self,json_data,token):
        return requests.post(url=self.url_add_course,headers={"Authorization":token},json = json_data)
    def select_course(self,test_data,token):
        return requests.get(url=self.url_select_course+f"/{test_data}",headers={"Authorization":token})

    def upload_course(self,test_data,token):
        return requests.put(url=self.url_add_course,headers={"Authorization":token},json = test_data)

    def delete_course(self,course_id,token):
        return requests.delete(url=self.url_add_course+f"/{course_id}",headers={"Authorization":token})