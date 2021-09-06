
class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        if target == "":
            return 0

        elif len(target) > len(source):
            return -1
        elif len(target) == len(source):
            if target == source:
                return 0
            else:
                return -1
        elif len(target) < len(source):
            m = len(target)
            n = len(source)
            indicator = -1
            for i in range(n - m +1):
                if source[i:i+m] == target:
                    indicator = i
                    break
            return indicator 
