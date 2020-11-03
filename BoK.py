import requests
import BoK_CS
import BoK_HS
import BoK_SSL

# ECOS Open API service를 판다스 데이터프레임화
class OpenBoKAPI():
    def __init__(self, api_key):
        self.api_key = api_key

    #통계조회조건 설정
    def searchCS(self, lan, requestStart, requestEnd, sCode, period, searchStart, searchEnd, code1=[None], code2=[None], code3=[None]):
        return BoK_CS.condition_set(api_key=self.api_key, requestType='json', lan=lan, requestStart=requestStart, requestEnd=requestEnd, sCode=sCode, period=period, searchStart= searchStart, searchEnd=searchEnd, code1=code1, code2=code2, code3=code3)

    #100대 통계지표
    def searchHS(self, lan, requestStart=1, requestEnd=100000):
        return BoK_HS.searchHS(self.api_key, requestType='json', lan=lan, requestStart=requestStart, requestEnd=requestEnd)

    #서비스 통계목록
    def searchSSL(self, lan, requestStart=1, requestEnd=100000, code='?'):
        return BoK_SSL.search_SSL(self.api_key, requestType='json', lan=lan, requestStart=requestStart, requestEnd=requestEnd, code=code)


if __name__ == '__main__':
    test = OpenBoKAPI('A1ZKVEG8QC0Z046QUWP3')
    print(test.searchHS('kr', 1, 100))
    print(test.searchSSL('kr', 1, 100))

