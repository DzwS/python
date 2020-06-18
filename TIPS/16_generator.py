# -*- coding: utf-8 -*-
# 返回字符串空格的索引


# 原版
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index)
    return result

# text = "Four score and seven years ago..."
text = ''
result = index_words(text)
print(result)

# 改进版, 用生成器来改写章节返回列表的函数
# 好处1：代码变得更清晰简洁
# 好处2：数据量大时，生成器不会影响执行时消耗的内存
def new_index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index

result = new_index_words(text)
print(list(result))

