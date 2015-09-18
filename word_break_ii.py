#!/usr/bin/env python

class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        stack = [[-1]]
        length = len(s)
        while True:
            tmp_list = []
            count = 0
            for j in stack[-1]:
                print('j = {0}'.format(j))
                if j >= -1:
                    count += 1
                    for i in range(j, length):
                        if s[j+1:i+1] in wordDict:
                            if i == length-1:
                                # done
                                print('Done {0}'.format(s[j:i+1]))
                                tmp_list += [-2]
                            else:
                                print('in {0}'.format(s[j:i+1]))
                                tmp_list += [i]
                        else:
                            if i ==length-1:
                                # break
                                tmp_list += [-3]
                elif j == -2:
                    tmp_list += [-2]
                else:
                    tmp_list += [-3]
                print('tmp_list = {0}'.format(tmp_list))
                stack.append(tmp_list)
            if count == 0:
                break
        print(stack)


def test():
    s = Solution()
    string = 'catsanddog'
    wordDict = set(['cat', 'cats', 'and', 'sand', 'dog'])
    s.wordBreak(string, wordDict)

if __name__ == '__main__':
    test()
