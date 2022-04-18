"""
이 서비스는 i3l3이 제공 중이며 MIT 라이선스로 https://github.com/i3l3/PizzzaBot 에서 배포중 입니다.
"""

from datetime import datetime

import win32api
import win32con
import win32gui
import time
import requests
import json


def crawlLunchMenu(schoolCode, year, month, day):
    url = 'https://schoolmenukr.ml/api/middle/{0}?year={1}&month={2}&date={3}'.format(schoolCode, year, month, day)
    response = requests.get(url)
    school_menu = json.loads(response.text)
    print(school_menu['menu'][0]['lunch'])
    return school_menu['menu'][0]['lunch']


def findWindow(openTalkName):
    hwndKakao = win32gui.FindWindow(None, '카카오톡')
    hwndKakao_edit1 = win32gui.FindWindowEx(hwndKakao, None, 'EVA_ChildWindow', None)
    hwndKakao_edit2_1 = win32gui.FindWindowEx(hwndKakao_edit1, None, 'EVA_Window', None)
    hwndKakao_edit2_2 = win32gui.FindWindowEx(hwndKakao_edit1, hwndKakao_edit2_1, 'EVA_Window', None)
    hwndKakao_edit3 = win32gui.FindWindowEx(hwndKakao_edit2_2, None, 'Edit', None)

    win32api.SendMessage(hwndKakao_edit3, win32con.WM_SETTEXT, 0, openTalkName)
    time.sleep(1)
    win32api.PostMessage(hwndKakao_edit3, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwndKakao_edit3, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


def sendMessage(message, openTalkName):
    kakao = win32gui.FindWindow(None, openTalkName)
    chat = win32gui.FindWindowEx(kakao, None, 'RICHEDIT50W', None)
    win32api.SendMessage(chat, win32con.WM_SETTEXT, 0, message)

    win32api.PostMessage(chat, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32api.PostMessage(chat, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


if __name__ == '__main__':
    with open('.\\secret.json') as f:
        json_data = json.load(f)
    openTalkTitle = json_data['talkTitle']
    today = datetime.today()
    menuList = crawlLunchMenu(json_data['schoolCode'], today.year, today.month, today.day)
    menu = '<오늘의 급식>\n\n'
    for i in menuList:
        menu = menu + i + '\n'
    menu = menu + '\n* 요리명에 표시된 번호는 알레르기를 유발할 수 있는 식자재입니다.\n1.난류, 2.우유, 3.메밀, 4.땅콩, 5.대두, 6.밀, 7.고등어, 8.게, 9.새우, ' \
                  '10.돼지고기, 11.복숭아, 12.토마토, 13.아황산염, 14.호두, 15.닭고기, 16.쇠고기, 17.오징어, 18.조개류(굴,전복,홍합 등)\n\n이 서비스는 MIT ' \
                  '라이선스로 https://github.com/i3l3/PizzzaBot 에서 소스 코드를 배포 중 입니다.\nBy i3l3(한기동) '

    findWindow(openTalkTitle)
    sendMessage(menu, openTalkTitle)
    with open('.\\' + str(today.year) + '-' + str(today.month) + '-' + str(today.day) + '-' + str(today.hour) + ':' + str(today.minute) + ':' + str(today.second) + '.log', 'a+') as log:
        log.write('Today\'s menu: ' + menu)
        log.write('Open Talk Title: ' + openTalkTitle)
        log.write('School Code: ' + json_data['schoolCode'])
