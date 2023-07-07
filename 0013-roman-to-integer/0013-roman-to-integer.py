class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        values = {"I":1, "IV":4, "V":5, "IX":9, "X":10, "XL":40, "L":50, "XC":90, "C":100, "CD":400, "D":500, "CM":900, "M":1000}
        i = 0
        while i in range(len(s)):
            sub = s[i:i+1]
            check = s[i:i+2]
            if check in values and len(check) == 2:
                sub = check
                i += 1
            result += values[sub]
            i += 1
        return result
