# -*- coding: utf-8 -*-


# 核心概念
# python支持闭包：闭包是一种定义在某个作用域中的函数，这种函数引用了那个作用域的变量。
#helper函数之所以能够访问sort_priority的group参数，原因就在于它是闭包
# python的函数是一级对象（first-class object),也就是说，我们可以直接引用函数，把函数


# 原版
numbers = [8, 3, 1, 2, 5, 4, 7, 6]
group = {4, 3, 5, 7} 

def sort_priority(values, group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    return found[0]

found = sort_priority(numbers, group)
print(numbers)
print(found)

# 改进版
# 添加一个辅助类，helper class.
# __call__, 调用实例本身就可以执行的方法。
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False
    
    def __call__(self,x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)
sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)
assert sorter.found is True



