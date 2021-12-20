class Solution(object):
    def rot(self, num):
        return int(str(num).replace('6', '9', 1))
