from heapq import heappop, heappush


def frequencySort(s: str) -> str:
        
        # Keep track of frequencies of characters
        freq = {}
        
        # First we want frequency of each character in the string
        for c in s: freq[c] = freq.get(c,0) + 1
            
        # We can use a maxHeap here such that as we push elements, 
        # they are arranged automatically by their frequency from max to min
        maxHeap = []
        for key in freq:  heappush(maxHeap, (-freq[key], key))
        
        # Final List 
        output = []
        while maxHeap: 
            pair = heappop(maxHeap)
            output.append(pair[1] * -pair[0])
            
        # Return the output
        return "".join(output)


s = "cacaca"

print("Output -> ",frequencySort(s))