#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: length_of_longest_substring.py
@time: 2018/9/27 23:36
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, m = 0, 0
        k_dict = dict()
        ans = 0
        while n <len(s) and m < len(s):
            if k_dict.has_key(s[m]):
                n = max(k_dict[s[m]],n)
            ans = max(ans, m-n+1)
            k_dict[s[m]] = m+1
            m += 1
        return ans



def stringToString(input):
    return input[1:-1].decode('string_escape')

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)

            ret = Solution().lengthOfLongestSubstring(s)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()