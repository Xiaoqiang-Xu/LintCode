class Solution:
    """
    @param k: An integer
    @param nums: An integer array
    @return: kth smallest element
    """
    # O(nlogn)
    def kthSmallest(self, k, nums):
        # write your code here
        n = len(nums)
        if n < k:
            return
        nums.sort()
        return nums[k - 1]
