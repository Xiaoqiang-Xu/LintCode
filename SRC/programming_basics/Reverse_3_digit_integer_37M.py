class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here

        return number % 10 * 100 +  ((number // 10) % 10) * 10  + number // 100  
      
      # get the hundreds digit, tens digit, and single digit
      # multiply them by 1, 10 and 100, then sum up
