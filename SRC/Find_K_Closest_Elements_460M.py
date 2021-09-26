class Solution:
    """
    @param A: an integer array
    @param target: An integer
    @param k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        # write your code here
        result = []
        n = len(A)
        start, end = 0, n - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if A[middle] < target:
                start = middle
            elif A[middle] == target:
                end = middle
            else:
                end = middle
        
        left, right = start, end
        while len(result) < k:
            if left < 0:
                result.append(A[right])
                right += 1
            elif right == n:
                result.append(A[left])
                left -= 1
            else:
                if abs(A[left] - target) <= abs(A[right] - target):
                    result.append(A[left])
                    left -= 1
                else:
                    result.append(A[right])
                    right += 1
    
        return result
