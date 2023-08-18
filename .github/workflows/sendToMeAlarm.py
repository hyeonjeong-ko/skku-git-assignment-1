import requests
import json
import os
#from datetime import datetime, timedelta

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

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "152831f2d43d3d3c3b003a24ec2fa088",
    "redirect_url" : "https://localhost:3000",
    "code" : "FSon6-E5EvlIHTsl7WKCca9dgdvVI6L2fr_gnUpcDlh77LREpaj9hTEbt8ETNPUUCXY1ZworDKcAAAGKCZyiRg"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# 추가된 부분

#token_json = json.loads(tokens)

access_token = tokens['access_token']

print(access_token)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
headers = {
    "Authorization": "Bearer " + "pdi-JBM7TDaPrdB1i6ENLG5lSKdkJR_nqBKp51xsCisMpwAAAYoJnO6P" # {access token}
}

# Get user information from environment variables
user_name = os.environ.get('USER_NAME')
commit_time = os.environ.get('COMMIT_TIME')
commit_message = os.environ.get('COMMIT_MESSAGE')
#origin_branch = os.environ.get('ORIGIN_BRANCH')
#branch_name = os.environ.get('BRANCH_NAME')
from_branch = os.environ.get('FROM_BRANCH')
to_branch = os.environ.get('TO_BRANCH')

# pull request과정에서의 시간 변수는 시차 존재
# Commit time을 문자열에서 datetime 객체로 변환
#commit_time_datetime = datetime.strptime(commit_time, '%Y-%m-%d %H:%M:%S %z')

# 9시간을 추가하여 새로운 datetime 객체 생성
#new_commit_time_datetime = commit_time_datetime + timedelta(hours=9)

# new_commit_time을 원하는 형식으로 변환하여 출력
#new_commit_time = new_commit_time_datetime.strftime('%Y-%m-%d %H:%M:%S')

# Print the user information
print("User Name:", user_name)
print("Commit Time:", commit_time)
#print("New Commit Time:", new_commit_time)
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

# 조건문을 사용하여 데이터 준비
if event_name == 'Push':
    description = f"{to_branch}(으)로 push 완료\n'{commit_message}'"
elif event_name == 'Pull Request':
    description = f"{from_branch}→{to_branch}\n'{commit_message}'"

# 사용자 템플릿 변수에 따라 텍스트, 피드 설정
template_type = 'Feed'
#template_type = 'Text'

if template_type == 'Feed':
    data = {
        "template_object" : json.dumps({ "object_type" : "feed",
                                         "content":{
                                             "title":f"{user_name}님이 {event_name}(을)를 했어요!",
                                             "description": description,
                                             "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/1200px-Font_Awesome_5_brands_github.svg.png",  # Replace with your image URL
                                             "link": {
                                                    "web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
                                                    "mobile_web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
                                              }
                                         },
                                        "button_title": "깃헙으로 이동하기"                            
        })
    }
elif template_type == 'Text':
    data = {
        "template_object" : json.dumps({ "object_type" : "text",
                                         "text" : f"{user_name}님이 {event_name}을 했어요!\n{description}",
                                         "link" : {
                                                     "web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
                                                     "mobile_web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
                                                  },
                                        "buttons": [
                                            {
                                                "title": "깃헙으로 이동하기",
                                                "link": {
                                                "web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
                                                  "mobile_web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
                                                }
                                            }
                                          ]
                                         
        })
    }
        

#data = {
#    "template_object" : json.dumps({ "object_type" : "feed",
#                                     "content":{
#                                         "title":f"{user_name}님이 {event_name}을 했어요!!",
#                                         "description": description,
#                                         "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Font_Awesome_5_brands_github.svg/1200px-Font_Awesome_5_brands_github.svg.png",  # Replace with your image URL
#                                         "link": {
#                                                "web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
#                                                "mobile_web_url": "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
#                                          }
#                                     },
#                                    "button_title": f"message: '{commit_message}'"                            
#    })
#}

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
