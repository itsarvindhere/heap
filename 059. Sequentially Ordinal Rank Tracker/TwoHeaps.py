from heapq import heappop, heappush

# To Implement Custom Ordering for elements in the MinHeap
class MinWrapper:
    def __init__(self, score, name):
        self.score = score
        self.name = name
    
    # Overriding the "lt" (less than) comparison operator's logic
    def __lt__(self, other):

        # If the scores are different
        if self.score != other.score:
            return self.score < other.score


        # If the scores are the same
        # The city with a lexicographically larger name should be placed above the one with a lexicographically smaller name
        return self.name > other.name

# To Implement Custom Ordering for elements in the MaxHeap
class MaxWrapper:
    def __init__(self, score, name):
        self.score = score
        self.name = name
    
    # Overriding the "lt" (less than) comparison operator's logic
    def __lt__(self, other):

        # If the scores are different
        if self.score != other.score:
            return self.score > other.score


        # If the scores are the same
        # The city with a lexicographically smaller name should be placed above the one with a lexicographically larger name
        return self.name < other.name


class SORTracker:

    def __init__(self):
        
        # To keep track of how many times the "get" method has been invoked
        self.i = 0
        
        # Max Heap
        self.maxHeap = []
        
        # Min Heap
        self.minHeap = []
        

    def add(self, name: str, score: int) -> None:
        
        # Push the data to the Minheap
        heappush(self.minHeap, MinWrapper(score,name))
        
        # If the length of the minHeap exceeds "i + 1"
        # Pop the extra elements from the top of minHeap and put them in maxheap
        while len(self.minHeap) > self.i + 1:
            top = heappop(self.minHeap)
            heappush(self.maxHeap, MaxWrapper(top.score, top.name))
        

    def get(self) -> str:
        
        # Increment the count ( The number of times get() is called)
        self.i += 1
        
        # The minHeap has the "ith" best city on top
        bestLocation = self.minHeap[0].name
        
        # If the maxHeap is not empty, take the element on top of maxHeap
        # And put it into minHeap
        # We always want to maintain the size of minHeap as "i + 1" at any point
        if self.maxHeap:
            top = heappop(self.maxHeap)
            heappush(self.minHeap, MinWrapper(top.score, top.name))

        # Return the ith best city
        return bestLocation