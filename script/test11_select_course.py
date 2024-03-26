from api.login import Get_login
from api.course import CourseApi

class Test_select_course:
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
        Test_select_course.token = res_c.json().get("token")

    # 后置条件
    def teardown_method(self):
        pass

    # 查询课程成功
    def test01_select_course_success(self):
        test_data = "?name=测试开发提升课01"
        response = self.Course_api.select_course(test_data=test_data,token=Test_select_course.token)

        print(response.json())

        assert 200 == response.status_code
        assert "查询成功" in response.json().get("msg")
        assert 200 == response.json().get("code")

    def test01_select_course_fail(self):
        test_data = "?name=测试开发提升课01"
        response = self.Course_api.select_course(test_data=test_data, token="xxx")

        print(response.json())

        assert 200 == response.status_code
        assert "认证失败" in response.json().get("msg")
        assert 401 == response.json().get("code")