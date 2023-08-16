# 라이브러리 호출
import requests
import json

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "152831f2d43d3d3c3b003a24ec2fa088",
    "redirect_url" : "https://localhost:3000",
    "code" : "GA-XbIJWU-98ITZ0jTWcpuHuka257nf0yz6QK0kKdjrt_0T341E12eEnNPZlusN5eUVg2go9dJcAAAGJ_oLEWA"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "refresh_token",
    "client_id": "152831f2d43d3d3c3b003a24ec2fa088",
    "refresh_token": "b56UXEk_9_iADkrucCElSm4datx10Xzok9SauGAwCisNIAAAAYn-gwKG"
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
        "text":f"{user_name}가 {commit_time}에 {commit_message}로 merge 하였음을 기록합니다",
        "link":{
            "web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
            "mobile_web_url" : "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
        },
        "button_title": "깃허브로 가기!!"
    })
}
response = requests.post(url, headers=header, data=data)
response.status_code
