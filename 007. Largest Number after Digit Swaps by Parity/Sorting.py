def largestInteger( num: int) -> int:

        # Number to list
        numList = []
        
        while num > 0:
            remainder = num % 10
            num = num // 10
            numList.append(remainder)
            
        numList.reverse()
        
        # List for even numbers
        evenList = [num for num in numList if num % 2 == 0]
        
        # List for odd numbers
        oddList = [num for num in numList if num % 2 != 0]
        
        # Sort evenList and oddList in decreasing order
        # We are sorting in decreasing order since we want the largest values to appear first
        # So, if even and odd lists are sorted in decreasing order
        # We can be sure that at any time, the value we are picking is the largest even or largest odd at that time
        evenList.sort(reverse=True)
        oddList.sort(reverse=True)
        
        evenPointer, oddPointer = 0,0
        
        # Final Number to return
        finalOutput = 0
        
        for num in numList:
            # If we have an even number
            if num % 2 == 0:
                # Then take the highest even number available at this point for finalOutput
                finalOutput  = finalOutput * 10 + evenList[evenPointer]
                evenPointer += 1
            # If we have an odd number
            else:
                # Then take the highest odd number available at this point for finalOutput
                finalOutput  = finalOutput * 10 + oddList[oddPointer]
                oddPointer += 1  
        
        return finalOutput

num = 65875
print("Output ->", largestInteger(num))