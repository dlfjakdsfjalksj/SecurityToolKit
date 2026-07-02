# 端口扫描器

#单线程扫描端口
# import socket
# import threading
# target = "127.0.0.1"
#
# for port in range(1, 100001):
#     sock = socket.socket(
#         socket.AF_INET,# ipv4
#         socket.SOCK_STREAM# tcp
#     )#实际上创建一个ipv4 + tcp的socket
#     sock.settimeout(1)
#     result = sock.connect_ex((target,port)) # 尝试与127.0.0.1： 8000建立连接
#     if result == 0:
#         print("Port {} is open".format(port))
#
#     sock.close()
# 以上是单线程部分
# 下面是增加的多线程部分
#核心思想：把单线程封装成一个函数，然后让多个线程同时调用这个函数
import socket
import threading

target = "127.0.0.1"

def scan(port):
    for port in range(1, 100001):
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        sock.close()

threads = []#创建一个空的线程列表
for port in range(1, 100001):
    t = threading.Thread(target=scan, args=(port,)) #创建一个线程 让他去执行scan（port）这个函数
    threads.append(t) #把刚创建好的线程保存起来
    t.start()#启动线程
for t in threads:
    t.join()