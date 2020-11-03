import requests
import pandas as pd
import json

#100대 통계지표
def searchHS(api_key, requestType, lan, requestStart=1, requestEnd=100000):
    url = 'http://ecos.bok.or.kr/api/KeyStatisticList/' + api_key + '/' + requestType + '/' + lan + '/' + str(requestStart) + '/' + str(requestEnd)

    r = requests.get(url)

    jo = json.loads(r.text)

    df = pd.json_normalize(jo['KeyStatisticList']['row'])
    df.columns = ['통계그룹명', '단위', '주기', '통계명', '값']
    df = df[['통계그룹명', '통계명', '주기', '단위', '값']]

    return df
