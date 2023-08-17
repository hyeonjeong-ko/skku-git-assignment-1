import requests
import json
import os
# 카카오톡 메시지 API 입니다 !
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "152831f2d43d3d3c3b003a24ec2fa088", # {restapi}
    "redirect_url" : "https://localhost:3000", 
    "code" : "6aNDgkpGaoC7s1dakW3tyX9wtolhjxOI5sZNec04Bfki1gpdtI0ZezTu9oQZxhGn2JJHIQoqJQ0AAAGKAdRViA" # {code}
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "9W75yjDo7gX1PboGk-kR5c__iMsZ5J2L0y5g9LsQCj10aAAAAYoB1IS6" # {access token}
}

# Get user information from environment variables
user_name = os.environ.get('USER_NAME')
commit_time = os.environ.get('COMMIT_TIME')
commit_message = os.environ.get('COMMIT_MESSAGE')


# Print the user information
print("User Name:", user_name)
print("Commit Time:", commit_time)
print("Commit Message:", commit_message)


# 환경 변수 불러오기
origin_branch = os.environ.get('ORIGIN_BRANCH')
branch_name = os.environ.get('BRANCH_NAME')

# 환경 변수 출력
print(f"User Name: {user_name}")
print(f"Origin Branch: {origin_branch}")
print(f"Branch Name: {branch_name}")




data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : f"{user_name} : {commit_message} -{commit_time} ● pull request {branch_name} to {origin_branch} sendTomeAlarm파일",
                                     "link" : {
                                                 "web_url" : "https://foss4g.tistory.com/1624",
                                                 "mobile_web_url" : "https://www.google.co.kr/search?q=drone&source=lnms&tbm=nws"
                                              }
    })
}
response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
