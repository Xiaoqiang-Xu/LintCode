class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # write your code here
        n = len(numbers)
        results = []
        for i in range(0, n - 2):
            inner_set = set()
            cur_sum = - numbers[i]
            for j in range(i + 1, n):
                if cur_sum - numbers[j] in inner_set:
                    triplet = [numbers[i], numbers[j], cur_sum - numbers[j]]
                    triplet.sort()
                    if triplet not in results:
                        results.append(triplet)
                inner_set.add(numbers[j])
        return results
