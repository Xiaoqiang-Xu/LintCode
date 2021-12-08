class Solution:
    """
    @param num1: An integer
    @param num2: An integer
    @param num3: An integer
    @return: an interger
    """
    def maxOfThreeNumbers(self, num1, num2, num3):
        # write your code here

        result = num1
        if num2 > result:
            result = num2
        
        if num3  > result:
            result = num3
        
        return result
