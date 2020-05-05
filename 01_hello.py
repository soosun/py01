# def plus(val1, val2):
#     return val1 + val2
# result = plus(10, 20)
# print(result)
#
#
# for item in range(0, 10):
#     print(item)
#
# for item in [1, 2, 3, 4, 4]:
#     print(item)
# name_list = ["A", "B", "C"]
# for name in name_list:
#     print(name)
# def print_gu(dan):
#     for item in range(1,10):
#         print(dan * item)
# print_gu(3)

# import urllib.request
# url = "https://www.naver.com/"
# html = urllib.request.urlopen(url)
# print(html.read())

# pip install bs4
# import bs4
# html_str = "<html><div></div></html>"
# bs_obj = bs4.BeautifulSoup(html_str, "html.parser")
# print(type(bs_obj))
# print(bs_obj)
# print(bs_obj.find("div"))
# top_right = bsObj.find("div", {"class":"area_links"})
# first_a = top_right.find("a")
# print(first_a.text)


# import urllib.request
# import bs4
#
# url = "https://www.naver.com/"
# html = urllib.request.urlopen(url)
#
# bs_obj = bs4.BeautifulSoup(html, "html.parser")
# ul = bs_obj.find("ul", {"class":"list_nav NM_FAVORITE_LIST"})
# lis = ul.findAll("li", {"class":"nav_item"})

# for li in lis:
#     a_tag = li.find("a")
#     span = a_tag.find("span", {"class":"an_txt"})
#     print(span.text)

# import requests
# from bs4 import BeautifulSoup
# url = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcNrgTrade'
# queryParams = '?' + 'LAWD_CD=' +'11110' \
#               + '&DEAL_YMD=' + '201811' \
#               + '&serviceKey=' + 'MG64fVo85yeR9N1YHX1F8bxgj5uBicvrWO1LV+1hrwNK8YmaYuEdNoiIjphfYd9AoemjU4uu2+6eBNOS1XhoVA=='
#
# url = url + queryParams
#
# result = requests.get(url)
# bs_obj = BeautifulSoup(result.content, "html.parser")
# print(bs_obj)
