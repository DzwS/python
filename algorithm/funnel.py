# coding: utf8

import time


class Funnel(object):
    def __init__(self, capacity, leaking_rate):
        self.capacity = capacity # 漏斗容量
        self.leadking_rate = leaking_rate # 漏嘴流水速率
        self.left_quota = capacity # 漏斗剩余空间
        self.leaking_ts = time.time() #上一次漏水时间
    
    def make_space(self):
        now_ts = time.time()
        delta_quota = now_ts - self.        #
        if delta_quota < 1:
            return
        self.left_quota += delta_quota
        self.leaking_ts = now_ts
        if self.left_quota > self.capacity:
            self.left_quota = self.capacity
        
    def watering(self, quota):
        self.make_space()
        if self.left_quota >= quota:
            self.left_quota -= quota
            return True
        return False

funnels = {}

def is_action_allowed(user_id, action_key, capacity, leaking_rate):
    key = "%s: %s" % (user_id, action_key)
    funnel = funnels.get(key)
    if not funnel:
        funnel = Funnel(capacity, leaking_rate)
        funnels[key] = funnel
    return funnel.watering(1)

for i in range(20):
    print(is_action_allowed('laoqian', 'reply', 15, 0.5))