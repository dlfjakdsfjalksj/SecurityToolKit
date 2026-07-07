"""
#作者：西西弗斯先生
"""
#程序入口
# 输入网址--调用Scanner.py--输出结果
"""
作者：西西弗斯先生
"""

from Scanner import scan

def main():
    target = input("请输入目标网址:")
    target = target.strip()
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    scan(target)

if __name__ == '__main__':
    main()