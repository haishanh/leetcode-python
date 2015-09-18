#!/usr/bin/env python

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        pass

def test():
    s = Solution()
    str = 'catsanddog'
    wordDict = set(['cat', 'cats', 'and', 'sand', 'dog'])
    res = s.wordBreak(str, wordDict)
    assert set(res) == set(['cats and dog', 'cat sand dog'])

if __name__ == '__main__':
    test()
