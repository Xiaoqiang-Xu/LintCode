class Solution:
    """
    @param s: input string
    @return: a string as the longest palindromic substring
    """
    def longestPalindrome(self, s):
        # write your code here
        if not s:
            return ''
        
        longest = ''
        for middle in range(len(s)):
            sub = self.find_palindrome_from(s, middle, middle)
            if len(sub) > len(longest):
                longest = sub
            sub = self.find_palindrome_from(s, middle, middle + 1)
            if len(sub) > len(longest):
                longest = sub
        return longest 
        
    def find_palindrome_from(self, string, left, right):
        while left >= 0 and right < len(string):
            if string[left] != string[right]:
                break
            left -= 1
            right += 1
        # pay attention to the string start and end point
        return string[left + 1 : right]
