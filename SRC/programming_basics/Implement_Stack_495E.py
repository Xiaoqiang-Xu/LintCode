class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.list1 = []


    def push(self, x):
        # write your code here
        self.list1.append(x)

    """
    @return: nothing
    """
    def pop(self):
        # write your code here
        if len(self.list1) > 0:
            self.list1.pop(-1)
        return None

    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.list1) > 0:
            return self.list1[-1]
        return None

    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        if len(self.list1) == 0:
            return True
        return False
# it is easy to use list in Python to realize stack.
