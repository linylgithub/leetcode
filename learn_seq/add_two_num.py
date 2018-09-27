#!/usr/bin/env python
#-*-coding: utf-8 -*-
"""
@version: 0.1
@author:linyl
@file: add_two_num.py
@time: 2018/9/27 11:23
"""

"""
    给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
    你可以假设除了数字 0 之外，这两个数字都不会以零开头
    示例：
        输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
        输出：7 -> 0 -> 8
        原因：342 + 465 = 807
"""
import json

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self,l1,l2):
        """
        :param l1:
        :param l2:
        :return: ListNode
        """
        head, p1, p2 = ListNode(0), l1, l2
        tail = head
        carry = 0
        while p1 and p2: #遍历两条链表的公共部分
            num = p1.val + p2.val + carry
            if num>9:
                num -= 10
                carry = 1
            else:
                carry = 0
            tail.next = ListNode(num)
            tail = tail.next
            p1 = p1.next
            p2 = p2.next

        if p2:
            p1 = p2
        while p1:
            num = p1.val + carry
            if num > 9:
                num -= 10
                carry = 1
            else:
                carry = 0
            tail.next = ListNode(num)
            tail = tail.next

            p1 = p1.next
        print('---------')
        print(carry)
        print('---------')
        if carry:
            tail.next = ListNode(1)
            tail = tail.next

        tail.next = None

        return head.next

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = dict()

        for k,v in enumerate(nums):
            diff = target - v
            if num_dict.has_key(diff):
                return [num_dict[diff],k]
            else:
                num_dict[diff] = k

        for i in range(len(nums)):

            diff = target - nums[i]

            if diff not in num_dict.keys():
                num_dict[diff] = i
            else:
                return [num_dict[diff],i]


def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    def readlines():
        while True:
            line =  sys.stdin.readline().strip('\n')
            if not line:
                break
            yield line

    lines = readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)

            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()
