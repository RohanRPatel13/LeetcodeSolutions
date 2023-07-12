class Solution(object):
    def getFolderNames(self, names):
        """
        :type names: List[str]
        :rtype: List[str]
        """
        last = collections.defaultdict(int)
        result = []
        for name in names:
            if name not in last:
                result.append(name)
                last[name] = 0
            else:
                last[name] += 1
                index = last[name]
                
                while True:
                    string = name + "(" + str(index) + ")"
                    if string not in last:
                        result.append(string)
                        last[string] = 0
                        break
                    else:
                        index += 1
        return result