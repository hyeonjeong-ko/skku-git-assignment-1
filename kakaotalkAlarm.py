# 라이브러리 호출
import requests
import json

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "152831f2d43d3d3c3b003a24ec2fa088",
    "redirect_url" : "https://localhost:3000",
    "code" : "G7tIxp7QQW7uBrLEb8bSABLeHH3FRL9AwakSnmGL5WI8W--A8Dj1hvE1qlrV8MnbUc3gUQo9dNoAAAGJ_hZm_w"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type": "refresh_token",
    "client_id": "152831f2d43d3d3c3b003a24ec2fa088",
    "refresh_token": "tyeCXX8Gj6UvEO7cqzkyiiGmO8xapwcqZPUpBwT4CiolkAAAAYn-Frtj"
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
data={
    'receiver_uuids': '["{}"]'.format(friend_id),
    "template_object": json.dumps({
        "object_type":"text",
        "text":"고현정 테스트~~!하이!",
        "link":{
            "web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws",
            "mobile_web_url" : "https://www.google.co.kr/search?q=deep+learning&source=lnms&tbm=nws"
        },
        "button_title": "뉴스 보기"
    })
}
response = requests.post(url, headers=header, data=data)
response.status_code
