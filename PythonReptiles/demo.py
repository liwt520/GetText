import urllib.request  
import requests 
import chardet
# response= urllib.request.urlopen('https://www.runoob.com/bootstrap/bootstrap-tutorial.html')
# html = response.read()
# print(len(html))
r=requests.get('https://www.runoob.com/bootstrap/bootstrap-tutorial.html')
print(chardet.detect(r.content))
r.encoding=chardet.detect(r.content)['encoding']
print(r.text)
print('12312312')