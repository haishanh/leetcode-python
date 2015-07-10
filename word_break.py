#!/usr/bin/env python
from __future__ import print_function
#TODO TODO!!

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    def wordBreak(self, s, wordDict):
        if s in wordDict:
            return True
        new_list = []
        for i in wordDict:
            if i in s:
                new_list.append(i)
        if not new_list:
            return False
        stack = [-1]
        length = len(s)
        end = 0
        while len(stack) > 0:
            prt_dbg("stack = {s}".format(s=stack))
            begin = stack[-1] + 1
            if end < begin:
                end = begin
            for j in range(end, length):
                if s[begin:j+1] in new_list:
                    if j == length - 1:
                        return True
                    stack.append(j)
                    break
                else:
                    if j == length - 1:
                        end = stack.pop() + 1
                        if len(stack) == 1:
                            return False
                        break
            prt_dbg("stack = {s}".format(s=stack))
        return False

class Solution2:
    def wordBreak(self, s, wordDict):
            length = len(s)
            if length==0:
                return False
            stack = [] # Stack to track the last character in each word
            stack.append(-1)  # So that the program checks if the whole string is just one word
            for i in range(length):
                    for j in stack[::-1]:
                        prt_dbg("i = {0}, j = {1}, stack = {2}, string = {3}".format(i,j,stack,s[j+1:i+1]))
                        if s[j+1:i+1] in wordDict:
                            stack.append(i)
                            break
            if length-1 in stack:
                return True
            else:
                return False

def prt_dbg(fmt):
    fmt = ' - Debug: ' + fmt
    print(fmt)

def test():
    s = Solution2()
    _str = "leetcode"
    _set = set(['leet', 'co', 'de', 'leetc', 'leetcod'])
    print(_str, _set)
    assert True == s.wordBreak(_str, _set)
    print('-' * 10)
    #_str = "leetcode"
    #_set = set(['lee', 'yy'])
    #assert False == s.wordBreak(_str, _set)
    #print('-' * 10)
    #_str = "leetcode"
    #_set = set(['leetcode', 'yy'])
    #assert True == s.wordBreak(_str, _set)
    #print('-' * 10)
    #_str = "leetcode"
    #_set = set(['leetcod', 'e'])
    #assert True == s.wordBreak(_str, _set)
    #print('-' * 10)
    #_str = "leetcode"
    #_set = set(['lee', 'tco', 'd'])
    #assert False == s.wordBreak(_str, _set)
    #print('-' * 10)
    #_str = "thisisaverylongword"
    #_set = set(['th', 'is', 'a', 've', 'ry', 'longw', 'ord'])
    #assert True == s.wordBreak(_str, _set)
    #print('-' * 10)
    #_str = "thisisaverylongword"
    #_set = set(['th', 'is', 'a', 've', 'ry', 'longw', 'or'])
    #assert False == s.wordBreak(_str, _set)
    #print('-' * 10)
    #_str = "thisisaverylongword"
    #_set = set(['th', 'is', 'a', 've', 'ry', 'longw', 'or', 'thi', 's', 'ave', 'longwo', 'rd'])
    #assert True == s.wordBreak(_str, _set)
    #print('-' * 10)
    #_str = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa\
    #        aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    #_set = set(['a', 'aa', 'aaa', 'aaa', 'aaaa', 'aaaaa', 'aaaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', \
    #            'aaaaaaaa', 'aaaaaaaaa', 'aaaaaaaaaa'])
    #assert False == s.wordBreak(_str, _set)


if __name__ == '__main__':
    test()
