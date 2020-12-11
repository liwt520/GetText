#coding:utf-8控制调度器
from DataOutput import Dataoutput 
from HtmlDownloader import Htm1Downloader 
from HtmlParser import Htmlparser
from UrlManager import UrlManager 
import queue
import time
from multiprocessing import Process, Queue
from multiprocessing.managers import BaseManager

url_g=Queue()
result_g=Queue()
def get_task():
    return url_g 
def get_result():
    return result_g
class NodeManager():
    def start_Manager(self):           
                '''创建一个分布式管理器
                ：param url_g:url队列
                ：param result_q：结果队列
                ：return：'''
                #把创建的两个队列注册在网络上,利用register方法,callable参数关联了Queue对象,
                #将 Queue对象在网络中暴露
                BaseManager.register('get_task_queue',callable=get_task)
                BaseManager.register('get_result_queue',callable=get_result)
                #绑定端口8001,设置验证口令“baike”。这个相当于对象的初始化
                manager=BaseManager(address=('192.168.10.130',8002),authkey='baike'.encode())
                #返回 manager对象
                return manager
    def url_manager_proc(self,url_q,conn_q,root_url):
        url_manager=UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while(url_manager.has_new_url()):
                #从URL管理器获取新的URL 
                new_url=url_manager.get_new_url()
                #将新的URL发给工作节点
                url_q.put(new_url)
                print('old_url=',url_manager.old_url_size(),new_url)
                #加一个判断条件,当爬取2000个链接后就关闭,并保存进度
                if(url_manager.old_url_size()>2000):
                    #通知爬行节点工作结束
                    url_q.put('end')
                    print('控制节点发起结束通知！')
                    #关闭管理节点,同时存储 set状态
                    url_manager.save_progress('new_urls.txt',url_manager.new__urls)
                    url_manager.save_progress('old_urls.txt',url_manager.old_urls)
                    return
            #将从result_solve_proc获取到的URL添加到URL管理器
            try:
                if not conn_q.empty():
                    urls=conn_q.get()
                    url_manager.add_new_urls(urls)
            except BaseException as e:
                pass
    def result_solve_proc(self,result_q,conn_q,store_q):
        while True:
            try:
                if not result_q.empty():
                    content=result_q.get(True)
                    if content['new_ur1s']=='end':
                        #结果分析进程接收通知然后结束
                        print('结果分析进程接收通知然后结束！')
                        store_g.put('end')
                        return 
                    conn_q.put(content['new_ur1s'])#ur1为set类型
                    store_q.put(content['data'])#解析出来的数据为dict类型else:
                    time.sleep(1)#延时休息
                else:
                    time.sleep(1)#延时休息
            except BaseException as e:
                pass
    def store_proc(self,store_g):
        output=Dataoutput()
        while True:
            if not store_g.empty():
                data=store_g.get()
                if data=='end':
                    print('存储进程接受通知然后结束！')
                    output.output_end(output.filepath)
                    return 
                output.store_data(data)
            else:
                time.sleep(1)

if __name__=='__main__':
    #初始化4个队列
    store_g=Queue()
    conn_g=Queue()
    #创建分布式管理器
    node=NodeManager()
    manager=node.start_Manager()
    manager.start()
    task=manager.get_task_queue()
    result=manager.get_result_queue()
    #创建URL管理进程、数据提取进程和数据存储进程
    # node.url_manager_proc(url_g,conn_g,'http://baike.baidu.com/view/284853.htm')
    url_manager_proc=Process(target=node.url_manager_proc,args=(task,conn_g,'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc=Process(target=node.result_solve_proc,args=(result,conn_g,store_g,))
    store_proc=Process(target=node.store_proc,args=(store_g,))
    #启动3个进程和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()

    while(True):
            time.sleep(1)
        
# class SpiderMan(object):
#     def __init__(self):
#         self.manager=UrlManager()
#         self.downloader= Htm1Downloader()
#         self.parser=Htmlparser()
#         self.output=Dataoutput()
#     def crawl(self,root_url):
#         #添加入口URL 
#         self.manager.add_new_url(root_url)
#         #判断ur1管理器中是否有新的ur1,同时判断抓取了多少个url 
#         while(self.manager.hasnewurl()and self.manager.old_url_size()<100):
#             try:
#                 #从URL管理器获取新的ur1
#                 new_url=self.manager.get_new_url()
#                 #HTL下载器下载网页
#                 html=self.downloader.download(new_url)
#                 #HTML解析器抽取网页数据
#                 new_urls,data=self.parser.parser(new_url,html)
#                 #将抽取的ur1添加到URL管理器中
#                 self.manager.add_new_urls(new_urls)
#                 #数据存储器存储文件
#                 self.output.store_data(data)
#                 print('已经抓取%s个链接'% self.manager.old_url_size())
#             except Exception as e:
#                 print("crawlfailed")
#                 #数据存储器将文件输出成指定格式
#         self.output.output_end()

     
# if __name__=="__main__":
#     spider_man=SpiderMan()
#     spider_man.crawl("http://baike.baidu.com/view/284853.htm")
