"""
이 서비스는 i3l3이 제공 중이며 MIT 라이선스로 https://github.com/i3l3/PizzzaBot 에서 배포중 입니다.
"""

from datetime import datetime

import requests
import json


def crawlLunchMenu(schoolCode, year, month, day):
    url = 'https://schoolmenukr.ml/api/middle/{0}?year={1}&month={2}&date={3}'.format(schoolCode, year, month, day)
    response = requests.get(url)
    school_menu = json.loads(response.text)
    print(school_menu['menu'][0]['lunch'])
    return school_menu['menu'][0]['lunch']


def post(content, accessToken, bandKey, do_push=True):
    today = datetime.today()
    url = 'https://openapi.band.us/v2.2/band/post/create?access_token={0}&band_key={1}&content={2}&do_push={3}'.format(accessToken, bandKey, content, do_push)
    failed = 0
    response = requests.get(url)
    result = json.load(response.text)['result_code'] == 1
    with open('.\\' + str(today.year) + '-' + str(today.month) + '-' + str(today.day) + '-' + str(today.hour) + ':' + str(today.minute) + ':' + str(today.second) + '.log', 'a+') as log:
        if not result:
            failed += 1
            log.write('Request failed; Try again. ({} Failed)'.format(failed))
            response = requests.get(url)
            result = json.load(response.text)['result_code'] == 1
            if not result:
                failed += 1
                log.write('Request failed; Try again. ({} Failed)'.format(failed))
                response = requests.get(url)
                result = json.load(response.text)['result_code'] == 1
                if not result:
                    failed += 1
                    log.write('Request failed; Try again. ({} Failed)'.format(failed))
                    response = requests.get(url)
                    result = json.load(response.text)['result_code'] == 1


if __name__ == '__main__':
    with open('.\\secret.json') as f:
        json_data = json.load(f)
    accessKey = json_data['accessKey']
    bandKey = json_data['bandKey']
    doPush = json_data['doPush']
    schoolCode = json_data['schoolCode']
    today = datetime.today()
    menuList = crawlLunchMenu(schoolCode, today.year, today.month, today.day)
    menu = '<오늘의 급식>\n\n'
    for i in menuList:
        menu = menu + i + '\n'
    menu = menu + '\n* 요리명에 표시된 번호는 알레르기를 유발할 수 있는 식자재입니다.\n1.난류, 2.우유, 3.메밀, 4.땅콩, 5.대두, 6.밀, 7.고등어, 8.게, 9.새우, ' \
                  '10.돼지고기, 11.복숭아, 12.토마토, 13.아황산염, 14.호두, 15.닭고기, 16.쇠고기, 17.오징어, 18.조개류(굴,전복,홍합 등)\n\n이 서비스는 MIT ' \
                  '라이선스로 https://github.com/i3l3/PizzzaBot 에서 소스 코드를 배포 중 입니다.\nBy i3l3(한기동) '

    post(menu, accessKey, bandKey, doPush)
    with open('.\\' + str(today.year) + '-' + str(today.month) + '-' + str(today.day) + '-' + str(today.hour) + ':' + str(today.minute) + ':' + str(today.second) + '.log', 'a+') as log:
        log.write('Today\'s menu: ' + menu)
        log.write('School Code: ' + json_data['schoolCode'])
