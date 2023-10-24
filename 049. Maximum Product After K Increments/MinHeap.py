from heapq import heapify, heappop, heappush


def maximumProduct(nums, k):
        
    # The most optimal solution will be to take the smallest number at any time and increment it by 1
    # So, we can use a minHeap to get the smallest number at any time
        
    # Convert "nums" list into a minHeap
    heapify(nums)
            
    # Now, we do the "k" operations
    while k > 0:
            
        # Take the smallest number
        top = heappop(nums)
            
        # Increment it by 1
        top += 1
            
        # Put it back in the nums
        heappush(nums, top)
            
        # Decrement operations
        k -= 1
            
    # Finally, return the product
    product = 1
    mod = 10**9 + 7
    while nums: product = (product * heappop(nums)) % mod
            
    return product

nums = [6,3,3,2]
k = 2

print("Output is ->", maximumProduct(nums,k))