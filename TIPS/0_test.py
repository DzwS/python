# -*- coding: utf-8 -*-



class TestClass(object):
    def __init__(self):
        self.first = 1
        self.second = 2
    
    def _get(self):
        # 保护函数
        return self.first
    
    def __get(self):
        # 私有函数
        return self.first
    
    @property
    def delata(self):
        return self.second - self.first
    
    @delata.setter
    def delata(self, num):
        print("This is test for property", num)

a = TestClass()
print(a.delata)
a.delata = 10