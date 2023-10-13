from collections import defaultdict
from heapq import heappop, heappush
class NumberContainers:

    def __init__(self):
        
        # A dictionary where each key is the "number"
        # And each value is a minHeap 
        # The minHeap will order the indices from smallest to largest
        self.indices = defaultdict(list)
        
        # Another dictionary where each "key" is an index
        # And value is the "number"
        # So this dictionary will always give us the latest number at any index
        self.currentValues = {}
        

    def change(self, index: int, number: int) -> None:
        
        # At "index", we want the value as "number"
        # So, update it in the currentValues first
        self.currentValues[index] = number
        
        # And now, for this number, we can put this index in the "indices" dictionary
        heappush(self.indices[number], index)
        

    def find(self, number: int) -> int:
        
        # If no index is filled with "number" return -1
        if number not in self.indices: return -1
        
        # if the number is present, we want the smallest index
        # But note that it is possible that we have already updated the number
        # at the current smallest index in minHeap
        # So, we also have to remove all those indices now
		
		# So here, we can make use of our "currentValues" dictionary
		# We want that at both places, we have the "number" at a particular index
		# If not, we will remove that index from the minHeap of the "number"
        while self.indices[number] and self.currentValues[self.indices[number][0]] != number: heappop(self.indices[number])
            
        # At this point, if the minHeap is empty, it means no index currently is filled with "number"
        if not self.indices[number]: return -1
        
        # Otherwise, just return the smallest index
        return self.indices[number][0]