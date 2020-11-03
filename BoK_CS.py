import requests
import pandas as pd
import json
# 통계 조회 조건 설정
def condition_set(api_key, requestType, lan, requestStart, requestEnd, sCode, period, searchStart, searchEnd, code1=[None], code2=[None], code3=[None]):
    '''
    :param api_key:
    :param requestType:     xml, json
    :param lan:             kr(국문), en(영문)
    :param requestStar:
    :param requestEnd:
    :param sCode:
    :param period:          YY(연간), QQ(분기), MM(월간), DD(일간)
    :param searchStart:     YYYYMMDD
    :param searchEnd:       YYYYMMDD
    :param code1:           반드시 리스트 형태로 입력
    :param code2:           반드시 리스트 형태로 입력
    :param code3:           반드시 리스트 형태로 입력
    :return: pandas obj
    '''

    df = pd.DataFrame()
    tf = None
    for x in code1:
        for y in code2:
            for z in code3:
                url = 'http://ecos.bok.or.kr/api/StatisticSearch/' + api_key + '/' + requestType + '/' + lan + '/' + requestStart + '/' + requestEnd + '/' + sCode + '/' + period + '/' + searchStart + '/' + searchEnd + '/' + x + '/' + y + '/' + str(z)

                r = requests.get(url)

                jo = json.loads(r.text)

                tf = pd.json_normalize(jo['StatisticSearch']['row'])
                statName = tf['STAT_NAME'][0]
                itemName1 = tf['ITEM_NAME1'][0]
                itemName2 = tf['ITEM_NAME2'][0]
                itemName3 = tf['ITEM_NAME3'][0]
                data_value = tf['DATA_VALUE'].tolist()
                unitName = tf['UNIT_NAME'][0]
                data_value.insert(0, unitName)
                data_value.insert(0, itemName3)
                data_value.insert(0, itemName2)
                data_value.insert(0, itemName1)
                data_value.insert(0, statName)

                df = df.append([data_value])

    columns = tf['TIME'].tolist()
    columns.insert(0,'단위')
    columns.insert(0,'항목3')
    columns.insert(0,'항목2')
    columns.insert(0,'항목1')
    columns.insert(0,'통계표')

    df.columns = columns

    df.reset_index(drop=True, inplace=True)

    return df