import requests
import json
import os
# 카카오톡 메시지 API 입니다 !!
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "152831f2d43d3d3c3b003a24ec2fa088", # {restapi}
    "redirect_url" : "https://localhost:3000", 
    "code" : "RdowTz42p3dMCoHaq7nsuaOH__uy1ccD167oMrf2Iiut6Vs8BX86udCcrOCbJUWyguFPCQo9dGkAAAGKA0_kCg" # {code}
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "cjQ8x_-UT3hokKyVroMeaGFqT6zHmR32N8KmZ2sECiolEAAAAYoD8AMV" # {access token}
}

# Get user information from environment variables
user_name = os.environ.get('USER_NAME')
commit_time = os.environ.get('COMMIT_TIME')
commit_message = os.environ.get('COMMIT_MESSAGE')
#origin_branch = os.environ.get('ORIGIN_BRANCH')
#branch_name = os.environ.get('BRANCH_NAME')
from_branch = os.environ.get('FROM_BRANCH')
to_branch = os.environ.get('TO_BRANCH')


# Print the user information
print("User Name:", user_name)
print("Commit Time:", commit_time)
print("Commit Message:", commit_message)
print("From Branch:", from_branch)
print("To Branch:", to_branch)


# 환경 변수 불러오기
#origin_branch = os.environ.get('ORIGIN_BRANCH')
#branch_name = os.environ.get('BRANCH_NAME')

# 환경 변수 출력
#print(f"User Name: {user_name}")
#print(f"Origin Branch: {origin_branch}")
#print(f"Branch Name: {branch_name}")




data = {
    'receiver_uuids': f'["{friend_id}"]',
    "template_object": json.dumps({
        "object_type": "feed",
        "content": {
            "title": f"{user_name}님이 {from_branch}에서 {to_branch}으로 {event_name}을 했어요!!",
            "description": (
                f"메시지:'{commit_message}'\n시간:'{commit_time}'\n"
            ),
            "image_url": ".github/workflows/github.png",  # Replace with your image URL
            "link": {
                "web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
                "mobile_web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
            }
        },
        "button_title": "깃헙으로 이동하기"
    })
}
response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
