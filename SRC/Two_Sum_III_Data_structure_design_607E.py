class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def __init__(self):
        self.map = {}

    def add(self, number):
        # write your code here
        if number in self.map:
            self.map[number] += 1
        else:
            self.map[number] = 1
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for num in self.map:
            if value - num in self.map and \
               (value - num != num or self.map[num] > 1):
               return True
        return False       
