class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # write your code here

        n = len(s)
        if n == 0:
            return True
        else:
            start, end = 0, n - 1
            while start < end:
                while start < end and not s[start].isalnum():
                    start += 1
                while start < end and not s[end].isalnum():
                    end -=1
                if s[start].upper() != s[end].upper():
                    return False
                    break
                else:
                    start += 1
                    end -= 1
            return True
