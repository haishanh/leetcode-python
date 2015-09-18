#!/usr/bin/env python
from __future__ import print_function
import time
import random

# take input as integer, leetcode.com runtime ~52ms
class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        def cal(x):
            '''x as a integer'''
            sum = 0
            while x:
                tmp = x % 10
                sum += tmp * tmp
                x //= 10
            return sum
        tmp = n
        check_list = []
        while True:
            x = cal(tmp)
            # print(x)
            if x == 1:
                return True
            if x in check_list:
                return False
            check_list.append(x)
            # time.sleep(0.5)
            tmp = x

# take input as string, leetcode.com runtime ~68ms
class Solution2:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        def cal(x):
            '''x as a string'''
            sum = 0
            digits = list(x)
            for i in digits:
                sum += int(i) * int(i)
            return str(sum)
        tmp = str(n)
        check_list = []
        while True:
            x = cal(tmp)
            if x == '1':
                return True
            if x in check_list:
                return False
            check_list.append(x)
            tmp = x

def gen_digits_list(n):
    l = []
    for i in range(n):
        l.append(random.randint(1,100000))
    return l


def test():
    s = Solution()
    assert True == s.isHappy(19)
    assert False == s.isHappy(18)
    s = Solution2()
    assert True == s.isHappy(19)
    assert False == s.isHappy(18)
    print('Test passed!')

    l = gen_digits_list(5000)
    print('Staring benchmarking...')

    before = time.time()
    for i in l:
        s = Solution()
        s.isHappy(i)
        # print(s.isHappy(i))
    after = time.time()
    total = (after - before) * 1000
    print('Solution A total time: %fms' % (total))

    before = time.time()
    for i in l:
        s = Solution2()
        s.isHappy(i)
        # print(s.isHappy(i))
    after = time.time()
    total = (after - before) * 1000
    print('Solution B total time: %fms' % (total))

if __name__ == '__main__':
    test()
