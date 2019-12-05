# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-12-3
UpdateTime: 2019-12-3
Info: 去除列表中重复的词，并且去除空数组, 请调用remove方法
"""

# set方法
def set_fuc(words):
    new_words = list(set(words))
    return new_words

# keys方法  list()方法是把字符串str或元组转成数组
def list_fuc(words):
    new_words = list({}.fromkeys(words).keys())
    return new_words

# 按照索引再次排序
def sort_fuc(words):
    new_words = list(set(words))
    new_words.sort(key=words.index)
    return new_words

# 循环遍历法
def for_fuc(words):
    new_words = []
    for id in words:
        if id not in new_words:
            new_words.append(id)
    return words

# 去除空数组
def remove_null(words):
    while "" in words:
        words.remove("")  # 把数组内的""这玩意清理掉
    return words

# 去除重复，并且去除空数组
def remove(words):
    new_words = set_fuc(words)
    remove_null_words = remove_null(new_words)
    return remove_null_words

if __name__ == "__main__":
    words = ["你","我","你和","我","你","拉拉","是","苏打",""]
    new_words = remove(words)
    print("words:", len(words), words)
    print("new_words:", len(new_words), new_words)