class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        # write your code here
        n = len(A)
        start, end = 0, n - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if A[middle] > A[middle - 1] and A[middle] > A[middle + 1]:
                return middle
            elif A[middle] > A[middle - 1] and A[middle] < A[middle + 1]:
                start = middle
            elif A[middle] < A[middle - 1]:
                end = middle

        
