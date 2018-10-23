#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: luanxutonggou.py
@time: 2018/8/18 19:27
"""

# -*- coding:utf-8 -*-
class Same:
    def checkSam(self, stringA, stringB):
        # write code here
        if len(stringA) != len(stringB):
            return False

        dictA = {}
        dictB = {}

        for _ch in stringA:
            if _ch not in dictA:
                dictA[_ch] = 1
            else:
                dictA[_ch] += 1

        for _ch in stringB:
            if _ch not in dictB:
                dictB[_ch] = 1
            else:
                dictB[_ch] += 1

        for item in dictA:
            if item not in dictB or dictA[item] != dictB[item]:
                return False

        return True

if __name__ == '__main__':
    same = Same()
    print(same.checkSam('This is nowcoder','is This nowcoder'))

