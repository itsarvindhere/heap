from sortedcontainers import SortedList
class MedianFinder:

    def __init__(self):
        self.sortedList = SortedList()
        

    def addNum(self, num: int) -> None:
        self.sortedList.add(num)
        

    def findMedian(self) -> float:
        # If the size of the list is odd
        if len(self.sortedList) % 2 != 0:
            # Return the middle element
            mid = len(self.sortedList) // 2
            return self.sortedList[mid]
        
        # If the size of the list is even
        else:
            mid = len(self.sortedList) // 2
            return (self.sortedList[mid - 1] + self.sortedList[mid]) / 2