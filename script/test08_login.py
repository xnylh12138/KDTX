# 登陆测试

from api.login import Get_login

class Test_login:
    uuid=None
    # 前置条件
    def setup_method(self):
        self.loginApi = Get_login()
        Test_login.uuid=self.loginApi.get_Image().json().get("uuid")
    def teardown_method(self):
        pass

    # 登陆成功测试
    def test01_login(self):
        json_data={
            "username": "admin",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": self.uuid
            }
        respond = self.loginApi.get_login(json_data)

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据包含  成功
        assert "成功" in respond.text
        # 断言 json 数据中的code值
        assert 200 == respond.json().get("code")

    # 登陆失败（用户名为空）
    def test02_without_username(self):
        json_data = {
            "username": "",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": Test_login.uuid
        }
        respond = self.loginApi.get_login(json_data=json_data)

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据包含  成功
        assert "错误" in respond.text
        # 断言 json 数据中的code值
        assert 500 == respond.json().get("code")



    # 登陆失败（未注册用户名）
    def test03_username_not_exist(self):
        json_data = {
            "username": "linjx",
            "password": "HM_2023_test",
            "code": "2",
            "uuid": Test_login.uuid
        }
        respond = self.loginApi.get_login(json_data=json_data)

        # 断言响应状态码
        assert 200 == respond.status_code
        # 断言响应数据包含  成功
        assert "错误" in respond.text
        # 断言 json 数据中的code值
        assert 500 == respond.json().get("code")