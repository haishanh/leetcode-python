#!/usr/bin/env python

class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):
        v1 = version1.split('.')
        v2 = version2.split('.')
        # padding the short one with zeros
        lenv1 = len(v1)
        lenv2 = len(v2)
        if lenv1 < lenv2:
            v1 += [0] * (lenv2 - lenv1)
        elif lenv1 > lenv2:
            v2 += [0] * (lenv1 - lenv2)
        #
        for i, j in zip(v1, v2):
            i, j = int(i), int(j)
            if i > j:
                return 1
            elif i < j:
                return -1
        return 0


def test():
    s = Solution()
    assert -1 == s.compareVersion('1.1', '1.2')
    assert -1 == s.compareVersion('1.1.1', '1.2')
    assert 1 == s.compareVersion('1.1.1', '1.1')
    assert 0 == s.compareVersion('01', '1')
    print('Test passed')

if __name__ == '__main__':
    test()
