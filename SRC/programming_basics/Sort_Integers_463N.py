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
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if A[j] < A[min_index]:
                    min_index = j
            A[i], A[min_index] = A[min_index], A[i]
        
        return A

# using the selection sort O(n^2)



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
        
        for i in range(n):
            indicator = 0
            for j in range(0, n - i - 1):
                if A[j] > A[j + 1]:
                    A[j], A[j + 1] = A[j + 1], A[j]
                    indicator = 1
            if indicator == 0:
                return A

        return A
    # using the bubble sort with some optimization (after ith pass, the last i element are already sorted. We 
    # can also stop the algorithm when we detect that no swap is happening)

       
