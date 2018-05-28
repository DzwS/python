# -*- coding:utf-8 -*-
import json
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        pass_room = [0]
        if len(pass_room) == len(rooms):
            return True
        else:
            for i in range(len(rooms[0])):
                if rooms[0][i] not in pass_room:
                    pass_room.append(rooms[0][i])
                    pass_room = self.recursion(pass_room, rooms, rooms[0][i])
                #print 'pass_room', pass_room
                if len(pass_room) == len(rooms):
                    return True
        return False
    
    def recursion(self, pass_room, rooms, key):
        print 'recirsion'
        if len(pass_room) == len(rooms):
            return pass_room
        else:
            for i in range(len(rooms[key])):
                #如果房间i没有访问，则访问该房间
                if rooms[key][i] not in pass_room:
                    pass_room.append(rooms[key][i])
                    #print 'function', pass_room
                    pass_room = self.recursion(pass_room, rooms, rooms[key][i])
            return pass_room