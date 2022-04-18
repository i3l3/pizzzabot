# PizzzaBot
학교의 급식을 카카오톡으로 전송해주는 봇입니다.

------------

# 목차
1. 카카오 피자봇
  + 설명
  + secrets.json 작성법
2. 밴드 피자봇 (개발중)
  + 설명
  + secrets.json 작성법

------------

# 1. 카카오 피자봇

## 설명
카카오 피자봇은 pywin32 라이브러리를 이용하여 메시지를 보내는 방식입니다.

## secrets.json 작성법
```json
{
  "talkName": "",
  "schoolCode": ""
}
```
여기서 ```talkName```은 채팅방 이름을 작성하면 됩니다.
```schoolCode```는 schoolmenukr.ml/code/app 에서 찾으실 수 있습니다.

------------

# 2. 밴드 피자봇

## 설명
밴드 피자봇은 네이버 밴드가 제공하는 Open API를 이용하여 만들어 졌습니다.

## secrets.json 작성법
```json
{
  "accessKey": "",
  "bandKey": "",
  "doPush": "",
  "schoolCode": ""
}
```
```schoolCode```는 schoolmenukr.ml/code/app 에서 찾으실 수 있습니다.
```accessKey```는 https://developers.band.us/develop/guide/api/get_authorization_code_from_user 에서, 
```bandKey```는 https://developers.band.us/develop/guide/api/get_bands 에서 얻으실 수 있습니다.
```doPush```는 사용자들에게 알림을 보낼지 결정하는 것입니다. true나 false를 입력합니다.
