# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-12-3
UpdateTime: 2019-12-3
Info: 分词
"""
import jieba
import jieba.analyse
import re

# 全模式
def cut_all(label):
    seg_list = jieba.cut(label, cut_all=True)
    return seg_list

# 精确模式
def cut_one(label):
    seg_list = jieba.cut(label, cut_all=False)
    return seg_list

# 搜索引擎模式
def cut_search(label):
    seg_list = jieba.cut_for_search(label)
    return seg_list

# 默认模式（默认是精确模式）
def cut_this(label):
    seg_list = jieba.cut(label)
    return seg_list

# TextRank 关键词抽取，只获取固定词性
def cut_text_rank(label):
    words = jieba.analyse.textrank(label, topK=50, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v'))
    return words

# 去除标点符号（strip_all True: 去除所有半角全角符号，只留字母、数字、中文,  False: 手工指定标点符号)
def remove_punctuation(label, strip_all=True):
    if strip_all:
        rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")
        label = rule.sub('',label)
    else:
        punctuation ="""！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""
        re_punctuation ="[{}]+".format(punctuation)
        label = re.sub(re_punctuation, "", label)
    return  label.strip()

def cut(label):
    content = remove_punctuation(label)
    sq_str = "|".join(cut_all(content))
    sq_list = sq_str.split("|")
    return sq_list

if __name__ == "__main__":
    content = "12345464我来到北京清华大学123456abAB？/ ，。,.:;:''';'''[]{}()（）《》"
    sq_list = cut(content)
    print(type(sq_list),sq_list)
