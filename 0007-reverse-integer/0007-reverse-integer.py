class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        copy = x
        if copy < 0:
            copy *= -1
        result = 0
        while copy > 0:
            result += copy%10
            copy = copy/10
            if copy != 0:
                result = result*10
        if x < 0:
            result = result * -1
        if -2**31 >= result or result >= 2**31-1:
            return 0
        return result