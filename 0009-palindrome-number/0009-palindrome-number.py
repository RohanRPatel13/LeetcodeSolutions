class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            string = str(x)
            string = string[::-1]
            inversed = int(string)
            if inversed == x:
                return True
            else:
                return False