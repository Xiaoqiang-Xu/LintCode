class Solution:
    """
    @param A: an integer rotated sorted array
    @param target: an integer to be searched
    @return: an integer
    """
    def search(self, A, target):
        # write your code here
        n = len(A)
        if not A:
            return -1

        start, end = 0, n - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if A[middle] > A[end]:
                if A[start] <= target <= A[middle]:
                    end = middle
                    # for other cases, we assign start = middle
                else:
                    start = middle
            else:
                if A[middle] <= target <= A[end]:
                    start = middle
                    # for other cases, we assign end = middle
                else:
                    end = middle
        
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

