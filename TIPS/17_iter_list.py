# -*- coding: utf-8 -*-


# 迭代器对象（容器） 和 迭代器的区别
# 迭代一个list,如果list数据量太大，可以存入到文件中，然后
#实现一个文件迭代器，



# 原版
data_path = '/usr/local/python/TIPS/17_data.txt'

def read_visit(data_path):
    with open(data_path, 'r') as f:
        for line in f:
            yield int(line)

def normalizer_copy(read_visit):
    total = sum(read_visit(data_path))
    result = []
    for value in read_visit(data_path):
        percent = 100 * value / total
        result.append(percent)
    return result

ge = read_visit(data_path)
for i in ge:
    print(i)
print()
print(normalizer_copy(read_visit))
