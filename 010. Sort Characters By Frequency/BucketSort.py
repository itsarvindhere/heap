def frequencySort(s: str) -> str:
        
        # Length of string
        n = len(s)
        
        # Keep track of frequencies of characters
        freq = {}
        
        # First we want frequency of each character in the string
        for c in s: freq[c] = freq.get(c,0) + 1
            
        # A list to keep each character and its frequency as a pair
        # In a string of length "n", a character can appear at most "n" times
        # So, we can create a list of "n" length
        # Where each index represents the frequency
        # Since indices start from 0, i = 0 actually refers to frequency of "1"
        # And at each index, we can have a list of characters with that frequency
        # Since the indices are already in sorted order, we don't have to sort manually
        freqList = [[] for i in range(n)]
        
        for key in freq: freqList[freq[key] - 1].append(key)
        
        # And now, we can start populating the final output list
        output = []
        
        # Loop backwards since we want from highest frequency to lowest
        for i in range(n - 1, -1, -1):
            for c in freqList[i]: output.append(c * (i + 1))
        
            
        # Return the output
        return "".join(output)


s = "cacaca"

print("Output -> ",frequencySort(s))