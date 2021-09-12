class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        n = len(S)
        if n < 3:
            return("Error")
        
        S.sort()
        count = 0
        for k in range(2, n):
            i = 0
            j = k -1
            while i < j:
                if S[i] + S[j] <= S[k]:
                    i += 1
                else:
                    count = count + j - i
                    j -= 1
            
        return count
