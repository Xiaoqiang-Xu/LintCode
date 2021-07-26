class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        if nums == []:
            return 0
        elif max(nums) < k:
            return len(nums)
        elif min(nums) > k:
            return 0
        else:
            n = len(nums)
            left, mid, right = 0, 0, n - 1
            while mid <= right:
                if nums[mid] < k:
                    nums[left], nums[mid] = nums[mid], nums[left]
                    left += 1
                    mid += 1
                elif nums[mid] == k:
                    mid += 1
                else:
                    nums[mid], nums[right] = nums[right], nums[mid]
                    right -= 1
        for i in range(0, n):
            if nums[i] >= k:
                return i

