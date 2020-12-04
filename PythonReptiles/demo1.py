html_str="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie"class="sister"id="link1"><!--elsie--></a>,
<a href="http://example.com/lacie"class="sister"id="link2"><!--Lacie--></a> and
<a href="http://example.com/tillie"class="sister"id="link3">Tillie</a>; and they lived at the bottom of a well.</p>
<p clas8="story">...</p>
"""
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html_str, 'lxml')
# print(soup.title)
# print(soup.p['class'])
# print(soup.p.get('class'))
# print(soup.p.string)
# print(soup.find_all(['a','b']))
# print(soup.find_all(id='link1'))
# # print(soup.find_all(href=re.complie('elsie')))
# print(soup.find_all(text='elsie'))
# print(soup.find_all('a',text='elsie'))
# # print(soup.select('# link2'))
# print(soup.select('a[href]'))
# # print(soup.select('a[href='']'))

# from lxml import etree
# import json
# html=etree.HTML(html_str)
# result=etree.tostring(html)
# # print(result)
# html=etree.HTML(html_str)
# urls=html.xpath(".//*[@class='sister']/@href")
# json_str=json.dumps(urls,ensure_ascii=False)
# with open('qiye.txt','w') as fp:
#     json.dump(urls,fp=fp,ensure_ascii=False)
# print(json_str)

import requests 
import os
from importlib.resources import path
import json
import queue
url ='http://seputu.com/'
# current_path = os.getcwd()  #获取当前路径
# q=queue.Queue(100)
list = [] 
def openUrl(url):
    user_agent='Mozilla/4.0(compatible;MSIE 5.5; Windows NT)'
    headers={'User-Agent': user_agent}
    r=requests.get(url, headers=headers)
    if r.status_code==200:
        r.encoding='utf-8'
        return r.text
    return None

def getpage(r):
    soup=BeautifulSoup(r,'html.parser',)
    for mulu in soup.find_all(class_='mulu'):
        h2=mulu.find('h2')
        if h2!=None:   
            for a in mulu.find(class_='box').find_all('a'):
                href=a.get('href')
                # q.put(href)
                list.append(href)
                # print(href)


def GetPageText(url,f):
    r=openUrl(url)
    if r is None:
        return
    soup=BeautifulSoup(r,'html.parser')
    for mulu in soup.find_all(class_='bg'):
        h2=mulu.find('h1')
        if h2!=None:   
            f.write(h2.string+'\r\n')#获取标题
            print(h2.string)
            for p in mulu.find(class_='content-body').find_all('p'):
                # href=a.get('href')
                box_txt=p.string
                # f.write(href+':'+box_title+'\r\n')#获取标题
                # print(href,box_title)
                if box_txt!=None:
                    f.write(box_txt+'\r\n')#获取标题
  


if __name__ == '__main__':
    openUrl("http://baike.baidu.com/view/284853.htm")
    # getpage(openUrl(url))
    # f =open("abc.txt",mode="w+",encoding="utf-8") 
    # for li in list:
    #     GetPageText(li,f)
    # f.flush()
    # f.close()

