class Solution:
    """
    @param str: An array of char
    @param left: a left offset
    @param right: a right offset
    @return: return a rotate string
    """
    def RotateString2(self, str, left, right):
        # write your code here
        if str == '':
            return ''
        else:
            n = len(str)
            if left == right:
                return str
            elif left > right:
                total_off = left - right
                modulus = total_off % n
                result = str[modulus: n] + str[0: modulus]
                return result
            else:
                total_off = right - left
                modulus = total_off % n
                result = str[n - modulus : ] + str[: n - modulus]
                return result


