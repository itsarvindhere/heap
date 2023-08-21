from collections import Counter
def topKFrequent(nums, k):
    # Length of list
    n = len(nums)
        
    # We know that each element in list can occur at least "1" time and at most "length of list" times
    countList = [[] for i in range(n)]
        
    # Counter
    count = Counter(nums)
        
    # Now, we take each frequency and then update the list at index = "frequency - 1" (since 0-indexing)
    for key,val in count.items(): countList[val - 1].append(key)
            
    # Output List to return
    output = []
        
    # Now, we can fill our output list based on the data in countList
    for i in range(n - 1, -1, -1):
        for element in countList[i]:
            output.append(element)
                
            # Return if we have "k" most frequent elements
            if len(output) == k: return output

nums = [1,1,1,2,2,3]
k = 2
print("Output -> ", topKFrequent(nums,k))