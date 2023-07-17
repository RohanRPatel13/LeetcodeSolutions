class Solution(object):
    def countEven(self, num):
        """
        :type num: int
        :rtype: int
        """
        count = 0
        for i in range(2, num + 1):
            res = [int(x) for x in str(i)]
            if sum(res) % 2 == 0:
                count += 1
        return count