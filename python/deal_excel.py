# encoding: utf-8
"""
Author: 沙振宇
CreateTime: 2019-12-3
UpdateTime: 2019-12-3
Info: 处理excel文件，目前只提供了读的功能
"""
import xlrd

# 读取Excel文件
def read_excel(path, page):
    # 打开文件
    workbook = xlrd.open_workbook(path)
    # 根据sheet索引或者名称获取sheet内容
    sheet = workbook.sheet_by_index(page)  # sheet索引从0开始

    # sheet的名称，行数，列数
    print("Sheet的名称:", sheet.name, ",行数:", sheet.nrows, ",列数:", sheet.ncols)
    tmp_tables = []
    for rown in range(sheet.nrows):
        array = []
        for coln in range(sheet.ncols):
            array.append(sheet.cell_value(rown, coln))
        tmp_tables.append(array)

    print(path, "一共%d条数据"%len(tmp_tables))
    return tmp_tables

if __name__ == '__main__':
    path = "../file/语料文件2.xlsx"
    tables = read_excel(path, 0)
    print("tables:",tables)
