# -*- coding: utf-8 -*-
from collections import defaultdict


def increment_with_report(current, increments):
    added_count = 0

    def missing():
        nonlocal added_count
        added_count += 1
        return 0
    
    result = defaultdict(missing, current)
    for key, amount in increments.items():
        result[key] += amount
    
    return result, added_count



current = {"test": 0, "test1": 1}
increment = {"test2": 2, "test3": 3}

result, count = increment_with_report(current, increment)
print(result)
print(count)


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0
    
    def __call__(self):
        self.added += 1
        return  0

counter = BetterCountMissing()
result = defaultdict(counter, current)
for key, amount in increment.items():
    result[key] += amount

print(result)
print(counter.added)
