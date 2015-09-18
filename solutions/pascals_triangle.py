#!/usr/bin/env python

class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        def gen_one(n):
            tmp = [0] + n + [0]
            for i in range(len(tmp) - 1):
                tmp[i] += tmp[i+1]
            return tmp[:-1]
        if numRows == 0:
            return []
        res = []
        tmp = [1]
        for i in range(numRows):
            res.append(tmp)
            tmp = gen_one(tmp)
        return res

def test():
    s = Solution()
    assert [] == s.generate(0)
    assert [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]] == s.generate(5)
    print('Test passed')


if __name__ == '__main__':
    test()
