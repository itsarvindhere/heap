from collections import Counter
from heapq import heappop, heappush


class Wrapper:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
    
    # Overriding the "lt" comparison operator's logic
    # So that heap orders elements as per the problem statement
    def __lt__(self, other):
        
        # If the frequencies are different
        # Then take the greater frequency before the smaller one
        if self.freq != other.freq:
            return self.freq < other.freq
        
        
        # If the frequencies are the same
        # Then take the lexicographically smaller word after the lexicographically greater word
        return self.word > other.word

class Solution:
    def topKFrequent(self, words, k: int):
        
        # Counter to have each word and its frequency
        freq = Counter(words)
        
        # Min Heap to get the k most frequent words
        minHeap = []
        
        # Go over each key in the the freq counter
        for key in freq:
            # Use the wrapper class to wrap the word and its frequency
            w = Wrapper(key, freq[key])
            
            # Push this wrapper class in the heap
            heappush(minHeap, w)
            
            # If heap size exceeds k, pop
            if len(minHeap) > k: heappop(minHeap)
                
        # Output to return
        output = []
        while minHeap:output.append(heappop(minHeap).word)
        
        output.reverse()

        # Return the "k" most frequent words
        return output
    
s = Solution()

words = ["i","love","leetcode","i","love","coding"]
k = 2

print(s.topKFrequent(words,k))