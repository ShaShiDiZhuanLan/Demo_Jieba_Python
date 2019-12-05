# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-12-2
UpdateTime: 2019-12-3
Info: 分词。先获取文件内容，然后再针对语料进行分词。
"""
import deal_excel
import deal_txt
import cut_word_jieba
import remove_duplicates

# 读取Excel文件，处理标签，返回Label数组——使用方法：直接调用 get_label() 方法即可
class Read_Excel_Label:
    # 初始化
    def __init__(self, flow_path, kg_path):
        self.flow_path = flow_path
        self.kg_path = kg_path

    # 读取文件并返回table型数组 flow_tables, kg_tables
    def __read_flow_id(self):
        flow_path = self.flow_path
        kg_path = self.kg_path
        flow_tables = deal_excel.read_excel(flow_path, 0)
        kg_tables = deal_excel.read_excel(kg_path, 0)
        return flow_tables, kg_tables

    # 给列表增加语料（语料间用||分割）
    def __add_data(self, old_list, labels):
        if "||" in labels:
            labels_list = labels.split("||")
            for item in labels_list:
                old_list.append(item.strip())
        return old_list

    # 获取全部标签
    def get_label(self):
        flow_tables, kg_tables = self.__read_flow_id()
        total_label = []
        # 增加流程语料
        for i,flow_item in enumerate(flow_tables):
            item = flow_item[3]
            if item != '' and i != 0:
                total_label = self.__add_data(total_label, item)

        print("total_label addFlowID:", len(total_label), total_label)
        # 增加知识库语料
        for i,kg_item in enumerate(kg_tables):
            item = kg_item[1]
            if item != '' and i != 0:
                total_label = self.__add_data(total_label, item)

        print("total_label:",len(total_label),total_label)
        return total_label

# 把语料转换成分词后的词汇
def label_to_words():
    D_Label = Read_Excel_Label("../file/语料文件2.xlsx", "../file/语料文件1.xlsx")
    label_list = D_Label.get_label()
    words = []
    for item in label_list:
        cur_list = cut_word_jieba.cut(item)
        words = cur_list + words
    return words

# 去除重复词汇，得到真实词汇
def label_remove_duplicates(words):
    new_words = remove_duplicates.remove(words)
    return new_words

# 去除列表中重复的值
def array_remove_duplicates(old_list):
    new_list = []
    total_words = []
    for cur_arr in old_list:
        if cur_arr not in new_list:
            total_words = cur_arr+total_words
            new_list.append(cur_arr)
    return new_list, total_words

# 核心处理——读取此词表中是否包含相似词，包含则输出词表当前序列
def read_txt_to_words():
    words = label_to_words()
    print("words:", len(words), words)
    deal_words = label_remove_duplicates(words)
    print("deal_words:", len(deal_words), deal_words)
    list_words, total_words = deal_txt.deal_txt()
    print("list_words:", len(list_words), list_words)
    print("total_list_words:", len(total_words), total_words)
    new_words = []
    for cur_list in list_words:
        for cur_label in deal_words:
            if cur_label in cur_list:
                new_words.append(cur_list)
    return new_words

# 写文件，把处理后的结果用txt文件记录下来
def write_file(path, content):
    with open(path, "w+", encoding="utf-8") as fp:
        fp.truncate(0)
        if isinstance(content, list):
            for cur_list in content:
                for word in cur_list:
                    fp.write(word)
                    fp.write(" ")
                fp.write("\n")

if __name__ == '__main__':
    intersect_words = read_txt_to_words()
    print("intersect_words:", len(intersect_words), intersect_words)
    new_words, total_words = array_remove_duplicates(intersect_words)
    print("new_words:", len(new_words), new_words)
    print("total_words:", len(total_words), total_words)
    write_file("../file/生成的相似文件.txt", new_words)