import requests


url='http://kdtx-test.itheima.net/api/login'
headers={
    "Content-Type": "application/json"
}
login_data = {
"username": "admin",
"password": "HM_2023_test",
"code": "2",
"uuid": "981a3591fe3a49889308cf28c111ff06"
}

response = requests.post(url= url ,headers= headers,json= login_data )
print(response.json())
print(response.status_code)