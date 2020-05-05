import requests
from bs4 import BeautifulSoup

def getCompanyinfo(code):
    # crawling
    url = "https://finance.naver.com/item/main.nhn?code=068270"
    data = requests.get(url)
    bsObj = BeautifulSoup(data.content, "html.parser")

    wrapCompany = bsObj.find("div", {"class":"wrap_company"})
    print(wrapCompany)

    # 종목이름, 가격
    return {"name":"", "price":""}