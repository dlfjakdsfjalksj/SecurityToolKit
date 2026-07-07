"""
#作者：西西弗斯先生
"""
#扫描逻辑
# 读取字典--拼接URL--发送HTTP请求--判断状态码--如果存在--打印结果


import requests

def scan(target):
    with open("WordList.txt") as f:
        words = f.readlines()
        for word in words:
            word = word.strip()
            url = target + '/' + word
        try:
            response = requests.get(url,timeout=5)
            if response.status_code == 200:
                print(f"[+]找到目录{url}")
            elif response.status_code == 403:
                print(f"[+] 目录存在，但禁止访问{url}")
            elif response.status_code == 301 or response.status_code == 302:
                print(f"目录发生重定向:{url}")
        except requests.exceptions.RequestException as e:
            print(e)
