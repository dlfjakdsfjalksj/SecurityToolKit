"""
#作者：西西弗斯先生
"""
#扫描逻辑
# 读取字典--拼接URL--发送HTTP请求--判断状态码--如果存在--打印结果
import requests

def scan(target):
    #target ： 目标网址
    #打开wordlist文件
    with open("WordList.txt") as f:
        words = f.readlines()
    #遍历文件中的每一行
    for word in words:
    #去掉换行符
        word = word.strip()
    #拼接url
        url = target + '/' + word
    #发送get请求
        try:
            response = requests.get(url,timeout=3)
        #判断状态码
            if response.status_code == 200:
                print(f"[+]找到目录：{url}")
            elif response.status_code == 403:
                print(f"[!] 目录存在但禁止访问：{url}")
            elif response.status_code == 301 or response.status_code == 302:
                print(f"[*] 目录发生重定向：{url}")


        except requests.exceptions.RequestException as e:

            print(f"[-] 无法连接：{url}")

            print(e)
            #try ... except 异常处理
    #打印存在的目录


