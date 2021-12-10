class Solution:
    """
    @param n: an integer
    @return: an ineger f(n)
    """
    def fibonacci(self, n):
        # write your code here
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            curr_left = 1
            curr_left_left = 0
            for i in range(3,  n + 1):
                current = curr_left + curr_left_left
                curr_left_left = curr_left
                curr_left = current
        
        return current
