class Solution:
    """
    @param nums: a rotated sorted array
    @return: the minimum number in the array
    """
    def findMin(self, nums):
        # write your code here
        n = len(nums)
        if n == 1:
            return nums[0]
        start, end = 0, n - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if nums[middle] > nums[end]:
                start = middle
            if nums[middle] < nums[end]:
                end = middle

        return min(nums[start], nums[end])
            

        
