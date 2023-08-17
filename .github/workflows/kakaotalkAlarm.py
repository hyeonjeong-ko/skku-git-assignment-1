# 라이브러리 호출
import os
import requests
import json

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
    "code" : "S9Ds94R43DJfMfNYXmofOZsELBgdo8JMlVUpf0YXm74v6eLCXz_W3oK46WU0vQrHn1OlWQopyWAAAAGKA-7C7w"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "refresh_token",
    "client_id": "152831f2d43d3d3c3b003a24ec2fa088",
    "refresh_token": "NPaNY_Ik0qXTWTJMAh04eMrY6UAzwWFDiFcaIvLBCiolEAAAAYoD8AMU"
}
response = requests.post(url, data=data)
tokens = response.json()
# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)

# 카카오 API 엑세스 토큰
with open("kakao_code.json", "r") as fp:
    tokens = json.load(fp)
print(tokens["access_token"])

url = "https://kapi.kakao.com/v1/api/talk/friends" #친구 목록 가져오기
header = {"Authorization": 'Bearer ' + tokens["access_token"]}
result = json.loads(requests.get(url, headers=header).text)
friends_list = result.get("elements")
print(friends_list)

friend_id = friends_list[0].get("uuid")
print(friend_id)

# 카카오톡 메시지
url= "https://kapi.kakao.com/v1/api/talk/friends/message/default/send"
header = {"Authorization": 'Bearer ' + tokens["access_token"]}

# Git Action에서 받은 정보를 사용하여 메시지 내용 구성
user_name = "'${{ steps.user_info.outputs.user_name }}'"
commit_time = "'${{ steps.user_info.outputs.commit_time }}'"
commit_message = "'${{ steps.user_info.outputs.commit_message }}'"

data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        #"text":"pull request요청이 왔어요!! 리뷰해주세요!!",
        "text":f"{user_name} : '{commit_message}' {event_name} 요청! - {commit_time}",
        "link":{
            "web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
            "mobile_web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
        },
        "button_title": "무야호!!"
    })
}
response = requests.post(url, headers=header, data=data)
response.status_code
