from collections import Counter
from functools import cmp_to_key


class Solution:
    
    # Custom compare function
    def compare(self, pair1, pair2):
        
        # If the frequency is different
        if pair1[0] != pair2[0]:
            # Then we simply sort by frequency
            # That is, the item with greater frquency 
            # appears after the item with lesser frequency 
            return pair1[0] - pair2[0]
        
        # If the frequency is same
        # Check the lexicographical order
        
        # The word that is lexicographically smaller
        # Should appear "after" the word that is lexicographically greater
        # That's why, we return "1" if word1 is lexicographically smaller than word2
        # "1" means place word1 after word2 in the sorted list
        if pair1[1] < pair2[1]: return 1
        
        # Otherwise, place the word1 before word2 if it is lexicographically equal to greater than word2
        return -1
    
    
    def topKFrequent(self, words, k: int):
        
        # Counter to have each word and its frequency
        freq = Counter(words)
        
        # List to keep each key value pair
        freqList = [(freq[key], key) for key in freq]
        
        freqList = sorted(freqList, key=cmp_to_key(self.compare))
        
        # Output list to return
        output = []
        
        while k > 0:
            output.append(freqList.pop()[1])
            k -= 1
        
        # Return the "k" most frequent words
        return output
    
s = Solution()

words = ["i","love","leetcode","i","love","coding"]
k = 2

print(s.topKFrequent(words,k))