# 判断一个变量是不是字符串，应该使用isinstance(s,basestring)
# 因为basestring才是str和unicode的基类，包含了普通字符串和unicode类型

some_string = "some string"
# isalnum()
# isalpha()
# isdigit()
# islower()
# isupper()
# isspace()
# istitle()
# startwtith(prefix, start, end)
# endswith()
# count(sub, start, end)
# find(sub, start, end)
print(some_string.find("s"))
# index(sub, start, end)
# rfind(sub, start, end)
print(some_string.rfind("s"))
# rindex(sub, start, end)
# replace()
# partition(sep)
# rpartition(sep)
# splitlines([keepends])
# split()
# rsplit()
## 大小写
# lower()
# upper()
# capitalize() 首写字母大写
# swapcase()
# title()
# 删减 和 填充
# strip([chars])
