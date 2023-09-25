from heapq import heappop, heappush
class StockPrice:

    def __init__(self):
        # To keep track of the timestamp and the price
        self.data = {}
        
        # What is the latest timestmap
        self.latestTimestamp = 0 
        
        # To keep the prices in maximum to minimum order
        # So that we can get the maximum price at any time
        # We can use a maxHeap
        self.maxPrices = []
        
        # To keep the prices in minimum to maximum order
        # So that we can get the minimum price at any time
        # We can use a minHeap
        self.minPrices = []
        
        

    def update(self, timestamp: int, price: int) -> None:
        # Update the price at the timestamp
        self.data[timestamp] = price
        
        # Update the timestamp
        self.latestTimestamp = max(self.latestTimestamp, timestamp)
        
        # Put the price in the heaps along with the timestamp
        heappush(self.maxPrices, (-price, timestamp))
        heappush(self.minPrices, (price, timestamp))
        

    def current(self) -> int:
        
        # Return the price at the latest timestamp
        return self.data[self.latestTimestamp]
        
    def maximum(self) -> int:
        
        # Remove all the data from top that is no longer valid
        # That is, if we updated the price at the timestamp but in the heap, 
        # we still have data with the old price on the top
        while -self.maxPrices[0][0] != self.data[self.maxPrices[0][1]]: heappop(self.maxPrices)
        
        return -self.maxPrices[0][0]
        
        

    def minimum(self) -> int:
        
        # Remove all the data from top that is no longer valid
        # That is, if we updated the price at the timestamp but in the heap, 
        # we still have data with the old price on the top
        while self.minPrices[0][0] != self.data[self.minPrices[0][1]]: heappop(self.minPrices)
        
        return self.minPrices[0][0]
