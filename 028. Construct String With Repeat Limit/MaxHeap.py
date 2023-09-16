from collections import Counter
from heapq import heappop, heappush
def repeatLimitedString(s: str, repeatLimit: int) -> str:
        
        # First, we want to know how many times each character appears in the string "s"
        freq = Counter(s)
        
        # We can create a maxHeap that will give us the greatest character at any time
        maxHeap = []
        
        for key in freq: heappush(maxHeap, [-ord(key), key])
        
        # Output string to return
        output = []
        
        # What was the previous character
        prevCharacter = ''
        
        while len(output) != len(s):
            
            # Top of heap
            greatestCharacter = heappop(maxHeap)[1]
            
            # If previous character is not the same as the greatest character at this point
            if prevCharacter != greatestCharacter:
                
                # How many times we can use this character in a row
                repeatedCount = 0
                
                # Now, we can put at most "repeatLimit" characters in output
                while repeatedCount < repeatLimit and freq[greatestCharacter] > 0:
                    output.append(greatestCharacter)
                    freq[greatestCharacter] -= 1
                    repeatedCount += 1
                    
                # Update the previous character
                prevCharacter = greatestCharacter
                
                # If the frequency of greatestCharacter is already 0
                # No need to push it back to the heap
                # Otherwise, push it back
                if freq[greatestCharacter] > 0: heappush(maxHeap, [-ord(greatestCharacter), greatestCharacter])
            
            # If previous character is the same as character at "i" index in charList
            else:
                # We cannot use it again at this point
                # So, we have to use the second greatest character at this time, if it exists
                
                # We can only use a character if its frequency is not already 0
                while maxHeap and freq[maxHeap[0][1]] == 0: heappop(maxHeap)

                # If second greatest does not exist, break
                if not maxHeap: break
                    
                # Get the second greatest character
                secondGreatest = heappop(maxHeap)[1]
                
                # We will only put one instance of this second greatest character in the output
                # Because we want as many greater characters as possible in the beginning of the output string
                output.append(secondGreatest)
                
                # Update the previous character
                prevCharacter = secondGreatest
                
                # Reduce the frequency in the dictionary
                freq[secondGreatest] -= 1
                
                # If the frequency of secondGreatest is already 0
                # No need to push it back to the heap
                # Otherwise, push it back
                if freq[secondGreatest] > 0: heappush(maxHeap, [-ord(secondGreatest), secondGreatest])
                
                # And don't forget to put the first greatest character back into the heap
                heappush(maxHeap, [-ord(greatestCharacter), greatestCharacter])
        
        # Return the output string
        return "".join(output)


s = "aababab"
repeatLimit = 2

print("Output -> ", repeatLimitedString(s, repeatLimit))