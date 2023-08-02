def findRelativeRanks(score):
        # Length of the list
        n = len(score)
        
        # Before sorting, convert each value into a pair (value, original index)
        sortedList = [(score[i], i) for i in range(n)]
        
        # Sort
        sortedList.sort(reverse = True)
        
        # Populate correct ranks
        for i in range(n):
            if i == 0:
                score[sortedList[i][1]] = "Gold Medal"
            elif i == 1:
                score[sortedList[i][1]] = "Silver Medal"
            elif i == 2:
                score[sortedList[i][1]] = "Bronze Medal"
            else:
                score[sortedList[i][1]] = str(i + 1)
                
        # Return the required output list
        return score


score = [10,3,8,9,4]
print("Output ->", findRelativeRanks(score))