#!/usr/bin/env python

class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        d = {}
        dx = {} # No two characters may map to the same character
        for i,c in enumerate(s):
            if d.get(c) and d[c] != t[i]:
                return False
            d[c] = t[i]
            if dx.get(t[i]) and dx[t[i]] != c:
                return False
            dx[t[i]] = c
        return True



def test():
    s = Solution()
    assert True == s.isIsomorphic('egg', 'add')
    assert False == s.isIsomorphic('foo', 'bar')
    assert True == s.isIsomorphic('paper', 'title')
    assert False == s.isIsomorphic('ab', 'aa')
    print('Test passed!')

if __name__ == '__main__':
    test()
