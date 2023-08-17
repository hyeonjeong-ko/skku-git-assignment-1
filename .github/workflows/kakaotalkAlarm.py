# 라이브러리 호출
import os
import requests
import json

event_name = os.environ.get('EVENT_NAME')

if event_name == 'Pull Request':
    print("This is a Pull Request event.")
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
    "code" : "QafJ7dHcgaG7U9ha0n89SJiqweTZVGR6owuJBafh2dvds1gH0ONwG4FkZByoSmP5QmslRAorDKgAAAGJ_1r6HA"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "refresh_token",
    "client_id": "152831f2d43d3d3c3b003a24ec2fa088",
    "refresh_token": "9cOL-jFByjLqxSjtGxSvs_vyLUrbs66Nc4I4yq-cCj11XAAAAYn_W145"
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
        "text":f"{user_name}(이)가 {commit_time}에 '{commit_message}'라는 message와 함께 pull_request를 요청했어요!",
        "link":{
            "web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
            "mobile_web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
        },
        "button_title": "깃허브로 가기!!"
    })
}
response = requests.post(url, headers=header, data=data)
response.status_code
