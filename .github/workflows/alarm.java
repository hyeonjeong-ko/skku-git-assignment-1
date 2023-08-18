const fetch = require('node-fetch'); // Node.js에서 HTTP 요청을 보내기 위한 모듈
const fs = require('fs'); // 파일 시스템 모듈

// 환경 변수 설정
const event_name = process.env.EVENT_NAME;
let merged_status = process.env.MERGED_STATUS;

if (event_name === 'Pull Request') {
    if (merged_status === 'true') {
        console.log("This is a merged Pull Request.");
        merged_status = 'Merge';
    } else {
        console.log("This is an open Pull Request.");
    }
} else if (event_name === 'Push') {
    console.log("This is a Push event.");
} else {
    console.log("Event type:", event_name);
}

const clientId = "152831f2d43d3d3c3b003a24ec2fa088";
const clientSecret = "YOUR_CLIENT_SECRET"; // 클라이언트 시크릿 값

// 카카오톡 메시지 API를 위한 토큰 발급
const tokenUrl = "https://kauth.kakao.com/oauth/token";
const tokenData = new URLSearchParams({
    "grant_type": "authorization_code",
    "client_id": clientId,
    "redirect_url": "https://localhost:3000",
    "code": "S9Ds94R43DJfMfNYXmofOZsELBgdo8JMlVUpf0YXm74v6eLCXz_W3oK46WU0vQrHn1OlWQopyWAAAAGKA-7C7w"
});

fetch(tokenUrl, {
    method: "POST",
    body: tokenData
})
.then(response => response.json())
.then(tokens => {
    console.log(tokens);

    // 카카오톡 메시지 API를 위한 엑세스 토큰 발급
    const refreshTokenData = new URLSearchParams({
        "grant_type": "refresh_token",
        "client_id": clientId,
        "refresh_token": "NPaNY_Ik0qXTWTJMAh04eMrY6UAzwWFDiFcaIvLBCiolEAAAAYoD8AMU"
    });

    return fetch(tokenUrl, {
        method: "POST",
        body: refreshTokenData
    });
})
.then(response => response.json())
.then(tokens => {
    // kakao_code.json 파일 저장
    fs.writeFileSync("kakao_code.json", JSON.stringify(tokens));

    // kakao_code.json 파일 읽기
    const tokenFile = fs.readFileSync("kakao_code.json", "utf-8");
    const access_token = JSON.parse(tokenFile).access_token;
    console.log(access_token);

    // 친구 목록 가져오기
    const friendUrl = "https://kapi.kakao.com/v1/api/talk/friends";
    const friendHeader = { "Authorization": `Bearer ${access_token}` };

    return fetch(friendUrl, { headers: friendHeader });
})
.then(response => response.json())
.then(result => {
    const friends_list = result.elements;
    console.log(friends_list);

    const friend_id = friends_list[0].uuid;
    console.log(friend_id);

    // 카카오톡 메시지 전송
    const messageUrl = "https://kapi.kakao.com/v1/api/talk/friends/message/default/send";
    const messageHeader = { "Authorization": `Bearer ${access_token}` };

    // Git Action에서 받은 정보를 사용하여 메시지 내용 구성
    const user_name = process.env.USER_NAME;
    const commit_time = process.env.COMMIT_TIME;
    const commit_message = process.env.COMMIT_MESSAGE;

    const data = {
        receiver_uuids: JSON.stringify([friend_id]),
        template_object: JSON.stringify({
            object_type: "feed",
            content: {
                title: `${user_name}님의 Git 이벤트`,
                description: (
                    `'${commit_message}' (${event_name} 요청) - ${commit_time}\n` +
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. " +
                    "Vestibulum vel lacus vitae nisl pharetra volutpat."
                ),
                image_url: "https://cdn-icons-png.flaticon.com/512/25/25231.png",
                link: {
                    web_url: "https://github.com/hyeonjeong-ko/skku-git-assignment-1",
                    mobile_web_url: "https://github.com/hyeonjeong-ko/skku-git-assignment-1"
                }
            },
            button_title: "깃헙으로 이동하기"
        })
    };

    return fetch(messageUrl, {
        method: "POST",
        headers: messageHeader,
        body: new URLSearchParams(data)
    });
})
.then(response => {
    console.log(response.status);
})
.catch(error => {
    console.error(error);
});
