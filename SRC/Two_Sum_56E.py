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
      
      
      
      
class Solution:
  # using two pointers method
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        # pay attention to the reference pass and value pass
        numbers1 = numbers[:]
        numbers1.sort()
        n = len(numbers)
        i, j = 0, n - 1
        while i < j:
            if numbers1[i] + numbers1[j] == target:
                pair = [numbers1[i], numbers1[j]]
                break
            elif numbers1[i] + numbers1[j] > target:
                j -=1
            else:
                i += 1
        result = []        
        for i in range(n):
            if numbers[i] == pair[0] or numbers[i] == pair[1]:
                result.append(i)
        result.sort()
        return result

      
      
