class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        ch = 'a'
        decoder = {}
        for i in range(1, len(key)+1):
            string = key[i-1:i]
            if string not in decoder and string != " ":
                decoder[string] = ch
                ch = chr(ord(ch) + 1)
        
        result = ""
        for i in range(1, len(message)+1):
            string = message[i-1:i]
            if string == " ":
                result = result + " "
            else:
                result = result + decoder[string]
        return result

