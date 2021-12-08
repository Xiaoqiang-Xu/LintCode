class Solution:
    """
    @param A: an integer array
    @return: nothing
    """
    def sortIntegers(self, A):
        # write your code here

        n = len(A)

        if n <= 1:
            return A
        
        temp = A[0]
        result = []
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if A[j] < A[min_index]:
                    min_index = j
            A[i], A[min_index] = A[min_index], A[i]
        
        return A
# using the selection sort O(n^2)
