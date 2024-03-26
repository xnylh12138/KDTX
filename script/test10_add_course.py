from api.login import Get_login
from api.course import CourseApi

class Test_add_course:
    # 初始化变量
    token = None
    # 前置条件
    def setup_method(self):
        self.Login_api=Get_login()
        self.Course_api=CourseApi()
        res_v = self.Login_api.get_Image()

        json_data = {
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": res_v.json().get("uuid")
        }

        res_c = self.Login_api.get_login(json_data)
        Test_add_course.token = res_c.json().get("token")

    # 后置条件
    def teardown_method(self):
        pass

    # 添加课程成功
    def test01_add_course_success(self):
        json_data ={
            "name": "测试开发提升课01",
            "subject": "6",
            "price": 899,
            "applicablePerson": "2",
            "info": "测试开发提升课01"
            }
        response = self.Course_api.add_course(json_data=json_data,token=Test_add_course.token)

        print(response.json())

        assert 200 == response.status_code
        assert "操作成功" in response.json().get("msg")
        assert 200 == response.json().get("code")

    # 添加课程失败
    def test02_add_course_fail(self):
        json_data = {
            "name": "测试开发提升课02",
            "subject": "4",
            "price": 899,
            "applicablePerson": "2",
            "info": "2"
        }
        response = self.Course_api.add_course(json_data=json_data, token="xxx")

        print(response.json())

        assert 200 == response.status_code
        assert "认证失败" in response.json().get("msg")
        assert 401 == response.json().get("code")

