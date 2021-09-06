class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        if s == "":
            return 0
        
        n = len(s)
        map = {}
        count = 0
        for i in range(n):
            if s[i] in map:
                count += 2
                map.pop(s[i])
            else:
                map[s[i]] = 1
        if map != {}:
            count += 1
        
        return count
