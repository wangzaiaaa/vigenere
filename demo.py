import requests
import bs4
from bs4 import BeautifulSoup
def getHTMLText(url):
    try:
        r = requests.get(url,timeout=1000)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
def fillUnivList(ulist,html):
    soup = BeautifulSoup(html,'html.parser')
    for tr in soup.find('tbody').children:   #所有的大学都在tbody中，每一个大学都在tr标签中
        if isinstance(tr,bs4.element.Tag):   #过滤掉非标签类型
            tds = tr('td')
            ulist.append([tds[0].string,tds[1].string,tds[2].string])
    return ulist
def printUnivList(ulist,nums=20):
    print("{:^10}\t\t{:^6}\t\t{:^10}".format("排名","学校名称","地区"))
    for i in range(nums):
        u = ulist[i]
        print("{:^10}\t\t{:^6}\t\t{:^10}".format(u[0],u[1],u[2]))
def main():
    u=[]
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = getHTMLText(url)
    ulist = fillUnivList(u,html)
    printUnivList(ulist,20)
main()