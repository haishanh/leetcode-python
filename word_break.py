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
                print('here')
                new_list.append(i)
        if not new_list:
            return False
        stack = [-1]
        length = len(s)
        while len(stack) > 0:
            print("stack = ", stack)
            begin = stack[-1] + 1
            for j in range(begin, length):
                if s[begin:j+1] in new_list:
                    if j == length - 1:
                        return True
                    stack.append(j)
                    break
                else:
                    if j == length - 1:
                        stack.pop()
                        break
            print("stack = ", stack)
        return False



def test():
    s = Solution()
    _str = "leetcode"
    _set = set(['leet', 'code'])
    print(s.wordBreak(_str, _set))
    _str = "leetcode"
    _set = set(['lee', 'yy'])
    print(s.wordBreak(_str, _set))


if __name__ == '__main__':
    test()
