# 使用Counter进行计数
# 属于字典类的子类，是一个容器对象，主要用来统计散列对象。
#支持集合操作 + = & |，其中&和|操作分别返回两个Conter对象各元素的最小值和最大值。


from collections import Counter
some_data = ["a", "2", 2, 4, 5, "2", "b", 4, 7, "a", 5, "d", "a", "z"]
print(Counter(some_data))

# 初始化
print(Counter("success"))
print(Counter(s=3, c=2, e=1, u=1))
print(Counter({'s': 3, 'c': 2, 'e': 1, 'u': 1}))

# 获取key
list(Counter(some_data).elements())

# 获取元素出现频率最高的元素以及他们的次数
Counter(some_data).most_common(2)

# 访问不存在的元素时，默认返回为0而不是抛出KeyError异常
Counter(some_data)["y"]

# update方法用于被统计对象元素的更新，原有Counter计数器对象与新增元素的统计计数值相加
# 不是直接替换他们
print(Counter(some_data).update({"a": 100}))
