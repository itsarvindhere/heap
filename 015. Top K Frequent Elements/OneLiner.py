from collections import Counter
def topKFrequent(nums, k):
    return [key for key,_ in Counter(nums).most_common(k)]

nums = [1,1,1,2,2,3]
k = 2
print("Output -> ", topKFrequent(nums,k))