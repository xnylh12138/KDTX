import config
from api.login import Get_login
from api.course import CourseApi
from api.constract import ConstractApi
import pytest

# @pytest.fixture
# def methed():
#     Login_api=Get_login()
#     return Login_api
#
# @pytest.fixture
# def methed2():
#     Course_api=CourseApi()
#     return Course_api

class Test_addHeTong:
    def setup_method(self):
        self.Login_api = Get_login()
        self.Course_api = CourseApi()
        self.Constract_api=ConstractApi()
    def teardown_method(self):
        pass
    # 初始化变量
    token = None
    filename = None

    # 1,登陆成功

    def test01_login_success(self):

        res_v=self.Login_api.get_Image()
        print(res_v.status_code)

        uuid = res_v.json().get("uuid")


        json_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": uuid
        }

        res_c=self.Login_api.get_login(json_data)
        print(res_c.json())

        Test_addHeTong.token=res_c.json().get("token")
        print("\n********")
        print(res_c.json().get("token"))
        print("\n********")

    # 2，添加课程成功
    def test02_addCourse(self):
        json_data={
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
            }

        res =self.Course_api.add_course(json_data,Test_addHeTong.token)
        print(res.json())

    # 3 合同上传成功
    def test03_uploadConstract(self):
        f = open(config.BASE_PATH + "/data/test.pdf","rb")
        res = self.Constract_api.upload_constract(test_data=f,token=Test_addHeTong.token)
        print(res.json())
        Test_addHeTong.filename = res.json().get("fileName")
    # 4 合同添加成功
    def test04_addConstract(self):
        json_data={
            "name": "测试888",
            "phone": "13612341888",
            "contractNo": "HT10012078",
            "subject": "6",
            "courseId": 99,
            "channel": "0",
            "activityId": 77,
            "fileName": Test_addHeTong.filename
            }
        res = self.Constract_api.add_constract(test_data=json_data,token=Test_addHeTong.token)
        print(res.json())