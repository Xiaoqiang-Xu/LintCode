class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: an integer
    """
    def twoSum2(self, nums, target):
        # write your code here
        n = len(nums)
        if n <= 1:
            return 0
        
        nums.sort()
        count = 0
        i, j = 0, n - 1
        while i < j:
            if nums[i] + nums[j] <= target:
                i += 1
            else:
                count = count + j - i
                j -= 1
    
        return count

