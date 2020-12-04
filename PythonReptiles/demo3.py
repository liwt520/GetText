from lxml import etree 
import requests 
from urllib.request import urlretrieve
def Schedule(blocknum,blocksize,totalsize):
    # blocknum:已经下载的数据块
    # blocksize:数据块的大小
    # totalsize：远程文件的大小
    per=100.0*blocknum*blocksize/totalsize 
    if per>100:
        per=100
        print('当前下载进度：%d '% per)
user_agent='Mozilla/4.0(compatible;MSIE 5.5;Windows NT)'
headers={'User-Agent':user_agent}
r=requests.get('http://www.ivsky.com/tupian/ziranfengguang/',headers=headers)
#使用1xm1解析网页
html=etree.HTML(r.text)
img_ur1s=html.xpath('.//img/@src')#先找到所有的img 
i=0
for img_url in img_ur1s:
    urlretrieve("http://img.ivsky.com/img/tupian/li/202005/03/xiliu_pubu-014.jpg",'img'+str(i)+'.jpg',Schedule)
    i+=1