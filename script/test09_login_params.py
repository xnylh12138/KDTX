import config
from api.login import Get_login
import pytest
import json
# test_data = [
#     ("admin","HM_2023_test",200,"成功",200),
#     ("","HM_2023_test",200,"错误",500),
#     ("linjx","HM_2023_test",200,"错误",500),
# ]


# 引用json文件
def setJson_data(json_file):
    test_data = []

    with open(json_file,"r") as f:
        # 加载json数据
        json_data = json.load(f)
        # 遍历json数据
        for case_data in json_data:
            username = case_data.get("username")
            password = case_data.get("password")
            status = case_data.get("status")
            message = case_data.get("message")
            code = case_data.get("code")
            test_data.append((username,password,status,message,code))

        return test_data









class Test_login:
    uuid=None
    # 前置条件
    def setup_method(self):
        self.loginApi = Get_login()
        Test_login.uuid=self.loginApi.get_Image().json().get("uuid")
    def teardown_method(self):
        pass

    # 登陆成功测试
    @pytest.mark.parametrize(("username","password","status","message","code"),setJson_data(json_file=config.BASE_PATH+"/data/login.json"))
    def test01_login(self,username,status,password,message,code):
        json_data={
            "username": username,
            "password": password,
            "code": "2",
            "uuid": Test_login.uuid
            }
        respond = self.loginApi.get_login(json_data)

        # 断言响应状态码
        assert status == respond.status_code
        # 断言响应数据包含  成功
        assert message in respond.text
        # 断言 json 数据中的code值
        assert code == respond.json().get("code")