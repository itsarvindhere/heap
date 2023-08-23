from collections import Counter
from heapq import heappop, heappush


def reorganizeString(s: str) -> str:
        
        #  Output to return
        output = []
        
        
        # Frequency of characters
        freq = Counter(s)
        
        # MaxHeap that will give us the character with maximum frequency at any time
        # Because the most optimal approach is to take a character that appears the most number of times
        # This will ensure that at the end, we are not grouping same characters together
        maxHeap = []
        for key in freq: heappush(maxHeap, [-freq[key], key])
            
        # While our maxHeap is not empty
        while maxHeap:
            
            # Take the character on top of the heap since it currently has the maximum frequency
            top = heappop(maxHeap)
            
            # If character at top of heap is not same as previous character
            # Or, if the output is empty, then we will consider the character on top
            if not output or output[-1] != top[1]:
                
                # Put the character in the output list
                output.append(top[1])
                
                # Reduce its frequency
                top[0] *= -1
                top[0] -= 1
                
                # If the frequency is not 0, we can push it back to heap with the updated frequency
                if top[0] > 0: heappush(maxHeap, [-top[0], top[1]])
            
            # If character on top of heap is same as previous character
            else:
                # If there are no more characters to choose in place of current character
                # Then it is not possible
                if not maxHeap: return ""
                
                # Otherwise, we can take the character that is currently on top of the heap
                newTop = heappop(maxHeap)
                
                # And do the same thing as we did in the above step
                output.append(newTop[1])
                
                newTop[0] *= -1
                newTop[0] -= 1
                
                if newTop[0] > 0: heappush(maxHeap, [-newTop[0], newTop[1]])
                    
                    
                # Finally, also push back the character that was initially on top which we did not consider
                # Since it might be considered later
                heappush(maxHeap, top)
        
        return "".join(output)


s = "aaaabbbcc"

print("Output -> ", reorganizeString(s))