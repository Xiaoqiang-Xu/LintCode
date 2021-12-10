class MyQueue:
    
    def __init__(self):
        # do intialization if necessary
        self.stack1 = []
        self.stack2 = []


    """
    @param: element: An integer
    @return: nothing
    """
    def push(self, element):
        # write your code here
        self.stack1.append(element)

    """
    @return: An integer
    """
    def pop(self):
        # write your code here
        if len(self.stack2) == 0:
            self.move()
        return self.stack2.pop()
 
    """
    @return: An integer
    """
    def top(self):
        # write your code here
        if len(self.stack2) == 0:
            self.move()
        return self.stack2[-1]

    def move(self):
        while len(self.stack1) > 0:
            self.stack2.append(self.stack1.pop())

# a_list[-1] will return last element of a certain list.
# a_list.pop() means deleting the last element and return it
# the insertion is easy, the pop() is kind of heavy. It can be reversed (insertion heavy, pop() easy).
