def repeatLimitedString(s: str, repeatLimit: int) -> str:
        
        # Output string to return
        output = []
        
        # It is given that the input string will have lowercase alphabets only
        # So basically, the maximum number of unique characters a string can have is 26
        # So, instead of having a frequency map and then creating a list or heap out of it,
        # We can create a list of length 26 where each index represents the character and value represents the frequency
        # And since the indices are already in sorted order, there is no need to explicitly sort the list
        freq = [0] * 26
        for c in s: freq[ord(c) - ord('a')] += 1
        
        #  Now, we can begin with our main logic
        
        # Previous character
        previousCharacter = ''
        
        # Index of the greatest character at any time
        # Initialize it as the last index in the "freq" list
        i = 25
            
        while len(output) != len(s):
            
            # Make sure "i" points to a character that has a non-zero frequency
            while i >= 0 and freq[i] == 0: i -= 1
            
            # Greatest character at this time
            greatestCharacter = chr(i + ord('a'))
            
            # If the previous character was not the same as current character
            if previousCharacter != greatestCharacter:
                
                # How many times we can use this character in a row
                repeatedCount = 0
                
                # Now, we can put at most "repeatLimit" characters in output
                while repeatedCount < repeatLimit and freq[i] > 0:
                    output.append(greatestCharacter)
                    freq[i] -= 1
                    repeatedCount += 1
                    
                # Update the previous character
                previousCharacter = greatestCharacter
            
            # If the previous character was the same as current character
            else:
                
                # We cannot use the current character in output at this point
                # So, we have to put the second greatest character in the output
                j = i - 1
                
                # Make sure secondGreatest character has a non-zero frequency
                while j >= 0 and freq[j] == 0: j -= 1
                    
                # If there is no secondGreatest character available, break
                if j < 0: break
                    
                # Otherwise, use the character at index "j" in "freq" once
                secondGreatest = chr(j + ord('a'))
                
                output.append(secondGreatest)
                
                # Update the frequency
                freq[j] -= 1
                
                # Update the previous character
                previousCharacter = secondGreatest
                
        # Return the output string
        return "".join(output)   


s = "aababab"
repeatLimit = 2

print("Output -> ", repeatLimitedString(s, repeatLimit))