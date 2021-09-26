class Solution:
    """
    @param reader: An instance of ArrayReader.
    @param target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
        # write your code here
        start, end = 0, 1
        if reader.get(start) == target:
            return 0
        while reader.get(end) < target:
            end = end * 2
        
        return self.binarySearch(reader, end // 2, end, target)

    def binarySearch(self, reader, start, end, target):
        while start + 1 < end:
            middle = (start + end) // 2
            if reader.get(middle) < target:
                start = middle
            elif reader.get(middle) == target:
                end = middle
            else:
                end = middle
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        return -1
