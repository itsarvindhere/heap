from heapq import heappop, heappush


def largestInteger( num: int) -> int:

        # Number to list
        numList = []
        
        while num > 0:
            remainder = num % 10
            num = num // 10
            numList.append(remainder)
            
        numList.reverse()
        
        # MaxHeap for evenList
        maxHeapEven = []
        
        # MaxHeap for oddList
        maxHeapOdd = []
        
        # Populate the heaps
        for num in numList:
            if num % 2 == 0: heappush(maxHeapEven, -num)
            else: heappush(maxHeapOdd, -num)

        # Final Number to return
        finalOutput = 0
        
        for num in numList:
            # If we have an even number
            if num % 2 == 0:
                # Then take the highest even number available at this point for finalOutput
                finalOutput  = finalOutput * 10 + (-heappop(maxHeapEven))
            # If we have an odd number
            else:
                # Then take the highest odd number available at this point for finalOutput
                finalOutput  = finalOutput * 10 + (-heappop(maxHeapOdd))
        
        return finalOutput

num = 65875
print("Output ->", largestInteger(num))