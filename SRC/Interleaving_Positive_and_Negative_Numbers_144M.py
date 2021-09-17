class Solution:
    """
    @param: A: An integer array.
    @return: nothing
    """
    def rerange(self, A):
        # write your code here
        n = len(A)
        if n <= 1:
            return A
        
        # number of positive and negative elements
        pos_num = 0
        neg_num = 0
        for i in A:
            if i > 0:
                pos_num += 1
            else:
                neg_num += 1
        
        # partition    
        i = 0
        flag = 0
        if pos_num >= neg_num:
            flag = 1
        for j in range(n):
            if flag == 1:
                if A[j] > 0:
                    A[i], A[j] = A[j], A[i]
                    i += 1
            else:
                if A[j] < 0:
                    A[i], A[j] = A[j], A[i]
                    i += 1
        
        # swap using two pointer method
        boundary = neg_num
        if flag == 1:
            boundary = pos_num
        k = 1
        for j in range(boundary, n):
            A[k], A[j] = A[j], A[k]
            k += 2

        return A




