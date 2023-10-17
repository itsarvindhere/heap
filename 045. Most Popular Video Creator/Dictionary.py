def mostPopularCreator(creators, ids, views):
        # Output list to return
        output = []
        
        # Length of the lists
        n = len(creators)
        
        # Dictionary to keep data for each creator
        # Each value will be a triplet -> [views, id, totalViews]
        data = {}
        
        # What is the highest total view count for any creator
        highestCount = 0
        
        # Loop to fill the dictionaries with the data
        for i in range(n): 
            
            # Update the "data" dictionary
            # If there is no entry yet for this creator, we just push the current one
            if creators[i] not in data: 
                
                data[creators[i]] = [views[i], ids[i], views[i]]
                
                # Update the highestCount
                highestCount = max(highestCount, views[i])
            
            # Otherwise
            else:
                
                # Update the total count so far for this creator
                data[creators[i]][2] += views[i]
                
                # Update the highestCount
                highestCount = max(highestCount, data[creators[i]][2])
                
                # On what conditions we can replace the current entry with the "i" video?
                
                # 1. Is the view count of current entry less than the current video?
                condition1 = data[creators[i]][0] < views[i]
                
                # 2. Is the view count of current entry same as current video but, the id is greater?
                condition2 = data[creators[i]][0] == views[i] and data[creators[i]][1] > ids[i]
                
                # If any of the two conuditions are true, we can replace
                if condition1 or condition2: 
                    data[creators[i]][0] = views[i]
                    data[creators[i]][1] = ids[i]

        # Now, we simply want to return the creator with total views equal to "highestCount"
        # And for that creator,we want to return the id of the video having the highest views
        # And there can be multiple creators with same number of total view count
        # So, in that case, we have to return all of them
        
        # Go over each creator
        for key in data:
            
            # If the total views are same as "highestCount"
            # Then put the creator's name and the id of the video with highest views in output
            if data[key][2] == highestCount: output.append([key, data[key][1]])
            
        # Finally, return the output
        return output


creators = ["alice","bob","alice","chris"]
ids = ["one","two","three","four"]
views = [5,10,5,4]

print("Output -> ", mostPopularCreator(creators, ids, views))