# Python语言的应用 之 Demo_Jieba_Python
Jieba分词。先获取xlsx文件的语料内容，然后再针对语料进行分词。<BR/>
<BR/>  
# 更新信息
开发者：沙振宇（沙师弟专栏） <BR/>
创建时间：2019-12-2<BR/>
最后一次更新时间：2019-12-5<BR/> 
<BR/> 
# 分词
## 分词——全模式 
seg_list = jieba.cut(label, cut_all=True) <BR/> 
## 分词——精确模式 
seg_list = jieba.cut(label, cut_all=False) <BR/> 
## 分词——搜索引擎模式 
seg_list = jieba.cut_for_search(label) <BR/> 
## 分词——默认模式（默认是精确模式） 
seg_list = jieba.cut(label) <BR/> 
## 分词——TextRank 关键词抽取，只获取固定词性 
words = jieba.analyse.textrank(label, topK=50, withWeight=False, allowPOS=('ns', 'n', 'vn', 'v')) <BR/> 
## 分词——去除标点符号
### 分词——去除标点符号——去除所有半角全角符号，只留字母、数字、中文
rule = re.compile(u"[^a-zA-Z0-9\u4e00-\u9fa5]")<BR/>
label = rule.sub('',label)<BR/>
### 分词——去除标点符号——手工指定标点符号
punctuation ="""！？｡＂＃＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘'‛“”„‟…‧﹏"""<BR/>
re_punctuation ="[{}]+".format(punctuation)<BR/>
label = re.sub(re_punctuation, "", label).strip() <BR/>
<BR/> 
# 读取Excel文件
## 读取Excel文件——打开文件
workbook = xlrd.open_workbook(path)<BR/>
## 读取Excel文件——根据sheet索引或者名称获取sheet内容
sheet = workbook.sheet_by_index(page) <BR/>
## 读取Excel文件——sheet的名称，行数，列数
print("Sheet的名称:", sheet.name, ",行数:", sheet.nrows, ",列数:", sheet.ncols)<BR/>
## 读取Excel文件——获取内容
sheet.cell_value(rown, coln)<BR/>
# 去除item_arr中的\n
s = [x.strip() for x in item_arr] <BR/>
<BR/>
# 运行效果 
<BR/>