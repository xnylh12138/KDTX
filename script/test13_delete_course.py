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

    # 删除课程成功
    def test01_delete_course_success(self):

        response = self.Course_api.delete_course(course_id="79",token=Test_add_course.token)

        print(response.json())

        assert 200 == response.status_code
        assert "操作成功" in response.json().get("msg")
        assert 200 == response.json().get("code")

    # 删除课程失败（课程id不存在）
    def test02_delete_course_fail01(self):

        response = self.Course_api.delete_course(course_id="455555",token=Test_add_course.token)

        print(response.json())

        assert 200 == response.status_code
        assert "操作失败" in response.json().get("msg")
        assert 500 == response.json().get("code")

    # 删除课程失败（用户未登录）
    def test03_delete_course_fail02(self):
        response = self.Course_api.delete_course(course_id="79", token="xxx")

        print(response.json())

        assert 200 == response.status_code
        assert "认证失败" in response.json().get("msg")
        assert 401 == response.json().get("code")