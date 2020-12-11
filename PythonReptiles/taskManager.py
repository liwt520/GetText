#coding:utf-8  服务
#taskManager.py for windows
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support,Queue
import time
#任务个数
task_number=10
#定义收发队列
task_queue = Queue(task_number)
result_gueue= Queue(task_number)
def get_task():
    return task_queue 
def get_result():
    return result_gueue
    #创建类似的QueueManager：
class QueueManager(BaseManager):
    pass
def win_run():
    #Windows下绑定调用接口不能使用1ambda，所以只能先定义函数再绑定
    QueueManager.register('get_task_queue',callable=get_task)
    QueueManager.register('get_result_queue',callable=get_result)
    #绑定端口并设置验证口令，Windows下需要填写IP地址，Linux下不填默认为本地
    manager=QueueManager(address=('192.168.10.130',8002),authkey='qiye'.encode())
    #启动
    manager.start()
    try:
        #通过网络获取任务队列和结果队列
        task=manager.get_task_queue()
        result=manager.get_result_queue()
        #添加任务
        for url in ["ImageUrl_"+str(i)for i in range(10)]:
            print('put task %s...'% url)
            task.put(url)
        print ('try get result...')
        while(True):
            if result.empty():
                time.sleep(1)
                continue
            print('result is %s'%result.get(timeout=10))
    except Exception as e:
        print('Manager error %s' % e)
    finally:
        #一定要关闭，否则会报管道未关闭的错误
        manager.shutdown()

if __name__=='__main__':
    # freeze_support()
    win_run()
