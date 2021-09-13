class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def twoSumClosest(self, nums, target):
        # write your code here
        n = len(nums)
        if n <= 1:
            return target
        nums.sort()
        import math
        diff = max(abs(target - nums[0] -nums[1]), abs(target - nums[n - 1] -nums[n -2]))
        i, j = 0, n - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return 0
            elif nums[i] + nums[j] > target:
                if nums[i] + nums[j] - target < diff:
                    diff = nums[i] + nums[j] - target
                j -= 1
            else:
                if target - nums[i] - nums[j] < diff:
                    diff = target - nums[i] - nums[j]
                i += 1
        return diff
#   -4 -1 1 2
                




            
