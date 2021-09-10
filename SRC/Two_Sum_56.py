class Solution:
  # using hashmap
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # write your code here
        um = dict()
        for i in range(len(numbers)):
            if numbers[i] in um:
                result = []
                result.append(um[numbers[i]])
                result.append(i)
                return result
            um[target - numbers[i]] = i
        return [0, 0]
