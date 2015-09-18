from collections import OrderedDict

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capa = capacity
        self.kv = OrderedDict()

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.kv:
            val = self.kv[key]
            del self.kv[key]
            self.kv[key] = val
            return val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.kv:
            del self.kv[key]
        self.kv[key] = value
        if len(self.kv) > self.capa:
            self.kv.popitem(False)

if __name__ == '__main__':
    x = LRUCache(4)
    assert x.get(1) == -1
    x.set(1,1)
    assert x.get(1) == 1
    x.set(2,2)
    assert x.get(2) == 2
    x.set(3,3)
    x.set(4,4)
    x.set(5,5)
    assert x.get(1) == -1
    assert x.get(2) == 2
    x.set(6,6)
    assert x.get(3) == -1
    assert x.get(2) == 2
    print('Test passed!')
