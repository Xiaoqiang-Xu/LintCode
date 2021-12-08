class Solution:
    """
    @param A: An integer
    @return: a float number
    """
    def maxOfArray(self, A):
        # write your code here

        n = len(A)
        if n == 1:
            return A[0]
        
        result = A[0]
        for i in range(n):
            if A[i] > result:
                result = A[i]
        
        return result

      # can also use return max(A)
