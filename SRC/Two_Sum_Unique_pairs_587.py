class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def twoSum6(self, nums, target):
        # write your code here
        # dont forget to do the boundary checking
        if not nums or len(nums) < 2:
            return 0

        count = 0
        hashset = set()
        visited = set()
        for i in nums:
            if target - i in hashset:
                if i not in visited:
                    count += 1
                    visited.add(i)
                    visited.add(target - i)
            hashset.add(i)        

        return count

