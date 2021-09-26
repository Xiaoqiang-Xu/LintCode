class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountainSequence(self, nums):
        # write your code here
        n = len(nums)
        if n == 1:
            return nums[0]
        if nums[0] > nums[1]:
            return nums[0]
        if nums[n - 1] > nums[n - 1]:
            return nums[n - 1]
        start, end = 0, n - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if nums[middle - 1] < nums[middle] and nums[middle] < nums[middle + 1]:
                start = middle
            elif nums[middle - 1] > nums[middle] and nums[middle] > nums[middle + 1]:
                end = middle
            else:
                return nums[middle]   
            
        
