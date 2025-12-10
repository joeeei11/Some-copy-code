# coding=utf-8
import time
import threading
import os

def ciji():
    os.system('python E:\\chengxu\\ciji.py')

def client():
    os.system('python E:\\chengxu\\client.py')

threads = []
threads.append(threading.Thread(target=ciji))  # args为函数接受的参数，多个
threads.append(threading.Thread(target=client))
print(threads)

if __name__ == '__main__':
    os.system('/usr/local/bin/frpc')
    for t in threads:
        # t.setDaemon(True)
        t.start()
    # t.join()
    # print("all over %s" %ctime())

