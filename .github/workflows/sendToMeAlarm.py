import requests
import json
import os
# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "152831f2d43d3d3c3b003a24ec2fa088",
    "redirect_url" : "https://localhost:3000",
    "code" : "-nimEXsni1ON7FWibwRrxuoFhk94n2jDewgY9lCcXFoXNjqhpMOCk3OTVAynlVA5ZGe8jQo9dJcAAAGKASweug"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "j2n-z7QYj1dNW8acGxnyWi9AC4DNeYTmFshMHQ9TCj102QAAAYoBLb1Y"
}

# Get user information from environment variables
user_name = os.environ.get('USER_NAME')
commit_time = os.environ.get('COMMIT_TIME')
commit_message = os.environ.get('COMMIT_MESSAGE')

data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "{os.environ.get('USER_NAME')}이 {os.environ.get('COMMIT_TIME')}에 {os.environ.get('COMMIT_MESSAGE')} 라고 보냄",
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
