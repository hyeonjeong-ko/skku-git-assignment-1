import requests
import json
import os

event_name = os.environ.get('EVENT_NAME')
merged_status = os.environ.get('MERGED_STATUS')

if event_name == 'Pull Request':
    if merged_status == 'true':
        print("This is a merged Pull Request.")
        event_name = 'Merge'
    else:
        print("This is an open Pull Request.")
elif event_name == 'Push':
    print("This is a Push event.")
else:
    print("Event type:", event_name)

# 카카오톡 메시지 API 입니다 !!
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "152831f2d43d3d3c3b003a24ec2fa088", # {restapi}
    "redirect_url" : "https://localhost:3000", 
    "code" : "bE7Sd9c-h2RX_yNyIM3T-dFmKT9KV8NLyacKnXTm1O2MaeAapMdzKng9fwgssRIaAwS-5wo9cxgAAAGKB_Z8pw" # {code}
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "KOUxuFFG7jQdht5GwkA2Ik2qVXjk6XMMNq3cchlPCiolUgAAAYoH952N" # {access token}
}

# Get user information from environment variables
user_name = os.environ.get('USER_NAME')
commit_time = os.environ.get('COMMIT_TIME')
commit_message = os.environ.get('COMMIT_MESSAGE')
#origin_branch = os.environ.get('ORIGIN_BRANCH')
#branch_name = os.environ.get('BRANCH_NAME')
from_branch = os.environ.get('FROM_BRANCH')
to_branch = os.environ.get('TO_BRANCH')

# Convert UTC time to the desired timezone (e.g., Asia/Seoul)
korea_timezone = datetime.timezone(datetime.timedelta(hours=9))  # UTC+9
new_commit_time = commit_time.astimezone(korea_timezone)

# Print the user information
print("User Name:", user_name)
print("Commit Time:", commit_time)
print("New Commit Time:", new_commit_time)
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
    "template_object" : json.dumps({ "object_type" : "feed",
                                     "content":{
                                         "title":f"{user_name}님이 {event_name}을 했어요!!",
                                         if event_name == 'Push':
                                             "description":(
                                                 f"'{commit_time}'에\n{to_branch}로 push 완료"
                                             ),
                                        elif event_name == 'Pull Request':
                                             "description": (
                                                 f"'{new_commit_time}'에\n{from_branch}→{to_branch}"
                                              ),
                                         "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/1200px-Font_Awesome_5_brands_github.svg.png",  # Replace with your image URL
                                         "link": {
                                                "web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
                                                "mobile_web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
                                          }
                                     },
                                    "button_title": f"message: '{commit_message}'"                            
    })
}

#data = {
#    'receiver_uuids': f'["{friend_id}"]',
#    "template_object": json.dumps({
#        "object_type": "feed",
#        "content": {
#            "title": f"{user_name}님이 {from_branch}에서 {to_branch}으로 {event_name}을 했어요!!",
#            "description": (
#                f"메시지:'{commit_message}'\n시간:'{commit_time}'\n"
#            ),
#            "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/1200px-Font_Awesome_5_brands_github.svg.png",  # Replace with your image URL
#            "link": {
#                "web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
#                "mobile_web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
#            }
#        },
#        "button_title": "깃헙으로 이동하기"
#    })
#}
response = requests.post(url, headers=headers, data=data)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
