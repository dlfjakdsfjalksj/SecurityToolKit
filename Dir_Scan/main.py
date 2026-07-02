"""
#作者：西西弗斯先生
"""
#程序入口
# 输入网址--调用Scanner.py--输出结果
"""
作者：西西弗斯先生
"""

# 程序入口

from Scanner import scan


def main():
    # 提示用户输入目标网址
    target = input("请输入目标网址（例如：http://testphp.vulnweb.com）：")

    # 去掉输入前后的空格
    target = target.strip()

    # 判断用户是否输入了 http:// 或 https://
    if not target.startswith("http://") and not target.startswith("https://"):
        target = "http://" + target

    print("=" * 50)
    print("开始扫描：", target)
    print("=" * 50)

    # 调用扫描函数
    scan(target)

    print("=" * 50)
    print("扫描完成！")
    print("=" * 50)


# Python程序入口
if __name__ == "__main__":
    main()