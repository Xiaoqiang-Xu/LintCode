class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        ordinal = 0
        n = len(nums)

        for i in range(n):
            if nums[i] != 0:
                nums[ordinal], nums[i] = nums[i], nums[ordinal]
                ordinal += 1
        return nums

