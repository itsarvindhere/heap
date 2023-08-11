def frequencySort(s: str) -> str:
        
        # Keep track of frequencies of characters
        freq = {}
        
        # First we want frequency of each character in the string
        for c in s: freq[c] = freq.get(c,0) + 1
            
        # A list to keep each character and its frequency as a pair
        freqList = []
        for key in freq: freqList.append((freq[key], key))
        
        # Sort the list in decreasing order
        freqList.sort(reverse=True)
        
        # Final List 
        output = []
        for pair in freqList: output.append(pair[0] * pair[1])
            
        # Return the output
        return "".join(output)


s = "cacaca"

print("Output -> ",frequencySort(s))