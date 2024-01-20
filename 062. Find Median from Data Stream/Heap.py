class MedianFinder:

    def __init__(self):
        
        # We will maintain items in these two heaps such that
        # If the ordered list is [a,b,c,d]
        # Then one heap can have [a,b] and other can have [c,d]
        # So basically, we will maintain balance between the two in terms of their sizes
        # But, since we know that there can be odd number of elements as well
        # It means, if we have [a,b,c,d,e]
        # Then, one heap will have one extra element than other
        # And so, we will allow that.
        # But, we cannot allow one heap to have more than one elements than the other
        # In other words, the difference in their lengths can be at most 1
        
        # Also, the maximum element of maxHeap cannot be greater than the minimum element of the minHeap
        # For example, if the ordered list is [a,b,c,d,e]
        # The maxHeap cannot have e in it if the minHeap has d in it
        # Because all that we want to do is divide this ordered list between these two heaps
        # Such that maxHeap has the left part (smaller elements) and minHeap has the right part (bigger elements)
        
        # Max Heap
        self.maxHeap = []
        
        # Min Heap
        self.minHeap = []
        

    def addNum(self, num: int) -> None:
        
        # We will always push the element in maxHeap first
        heappush(self.maxHeap, -num)
        
        # If the minHeap is not empty and top of maxHeap is greater than top of minHeap
        # Then, we want to push the top of maxHeap into the minHeap
        # Because we want the maxHeap to have all the elements <= elements in minHeap
        if self.minHeap and -self.maxHeap[0] > self.minHeap[0]: heappush(self.minHeap, -heappop(self.maxHeap))
            
        # If the difference in lengths is greater than 1
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            
            # If maxHeap has more elements, put the top into the minHeap
            if len(self.maxHeap) > len(self.minHeap): heappush(self.minHeap, -heappop(self.maxHeap))
                
            # If minHeap has more elements, put the top into the maxHeap
            else: heappush(self.maxHeap, -heappop(self.minHeap))
        

    def findMedian(self) -> float:
        
        # Total Elements inserted so far
        n =  len(self.maxHeap) + len(self.minHeap)

        # If the number of elements are odd
        # Then we need to return the top of the maxHeap or minHeap, depending on which one has an extra element
        if n % 2 != 0:
            return -self.maxHeap[0] if len(self.maxHeap) > len(self.minHeap) else self.minHeap[0]
        
        # If the number of elements are even, we will simply return the median by taking the top elements from both heaps
        else: 
            return (-self.maxHeap[0] + self.minHeap[0]) / 2