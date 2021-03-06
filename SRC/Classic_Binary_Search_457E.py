class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        start, end = 0, n - 1
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                start = middle + 1
            else: 
                end = middle - 1
        return -1

    
    # template
    class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def findPosition(self, nums, target):
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        start, end = 0, n - 1
        while start + 1 < end:
            middle = (start + end) // 2
            if nums[middle] == target:
                end = middle
            elif nums[middle] < target:
                start = middle
            else: 
                end = middle
        
        if nums[start] == target:
            return start 
        if nums[end] == target:
            return end
        return -1
