import requests
import pandas as pd
import json

#서비스 통계목록
def search_SSL(api_key, requestType, lan, requestStart=1, requestEnd=100000, code='?'):
    url = 'http://ecos.bok.or.kr/api/StatisticTableList/' + api_key + '/' + requestType + '/' + lan + '/' + str(requestStart) + '/' + str(requestEnd) + '/' + str(code)

    r = requests.get(url)

    jo = json.loads(r.text)

    df = pd.json_normalize(jo['StatisticTableList']['row'])

    df.columns = ['검색가능여부', '출처', '주기', '통계명', '통계표코드', '상위통계표코드']
    df = df[['통계명', '통계표코드', '상위통계표코드', '주기', '검색가능여부', '출처']]

    return df