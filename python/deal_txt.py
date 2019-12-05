# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-12-3
UpdateTime: 2019-12-3
Info: 处理txt，读取文件内容，并返回
"""

# 读取txt
def read_txt():
    with open("../file/已有相似词.txt","r",encoding="utf-8") as fp:
        read_list = fp.readlines()
    return read_list

# 处理txt，形成list
def deal_lines(txt):
    arr = []
    total_arr = []
    for item in txt:
        item_arr = item.split(" ")
        s = [x.strip() for x in item_arr] # 去除item_arr中的\n
        arr.append(s)
        total_arr = total_arr + s
    return arr,total_arr

# 处理txt核心
def deal_txt():
    rl = read_txt()
    dl, tl = deal_lines(rl)
    return dl, tl

if __name__ == "__main__":
    deal_txt()