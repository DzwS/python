# -*- coding: utf-8 -*-
import datetime


# 配额(quota)比作桶底露出的水
# 
class Bucket(object):
    def __init__(self, period):
        self.period_delta = datetime.timedelta(seconds=period)
        self.reset_time = datetime.datetime.now()
        self.quota = 0

    def __repr__(self):
        return "Bucket(quota=%d)" % self.quota

def fill(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount

def deduct(bucket, amount):
    now = datetime.datetime.now()
    if now - bucket.reset_time > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True

