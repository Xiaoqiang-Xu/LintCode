import queue
class Stack:
    """
    @param: x: An integer
    @return: nothing
    """
    def __init__(self):
        self.queue1 = queue.Queue()
        self.queue2 = queue.Queue()


    def push(self, x):
        # write your code here
        self.queue1.put(x)  

    """
    @return: nothing
    """
    def pop(self):
        # write your code h ere
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        self.queue1.get()
        self.queue1, self.queue2 = self.queue2, self.queue1



    """
    @return: An integer
    """
    def top(self):
        # write your code here
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        temp = self.queue1.get()
        self.queue2.put(temp)
        self.queue1, self.queue2 = self.queue2, self.queue1

        return temp


    """
    @return: True if the stack is empty
    """
    def isEmpty(self):
        # write your code here
        if self.queue1.qsize() == 0:
            return True
        return False
