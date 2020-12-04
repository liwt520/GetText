import urllib.request  
import requests 
import chardet
import re 
from bs4 import BeautifulSoup
# response= urllib.request.urlopen('https://www.runoob.com/bootstrap/bootstrap-tutorial.html')
# html = response.read()
# print(len(html))
# r=requests.get('https://www.runoob.com/bootstrap/bootstrap-tutorial.html')
# print(chardet.detect(r.content))
# r.encoding=chardet.detect(r.content)['encoding']
# print(r.text)
# print('12312312')

p=re.compile(r'(?P<wordl>\w+) (?P<word2>\w+)')
#使用名称引用
s='i say, hello world'
print (p.sub(r'\g<word2> \g<wordl>',s))
p=re.compile(r'(\w+) (\w+)')#使用编号
print (p.sub(r'\2 \1',s))
def func(m):
    return m.group(1).title()+' '+m.group(2).title()
print (p.sub(func,s))