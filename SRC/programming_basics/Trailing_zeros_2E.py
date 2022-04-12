class Solution:
    """
    @param n: A long integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailing_zeros(self, n: int) -> int:
        # write your code here
        num = 0
        i = 5
        while n >= i:
            num += n // i
            i = i * 5
        
        return num

