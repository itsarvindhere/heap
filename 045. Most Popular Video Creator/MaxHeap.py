from collections import defaultdict
from heapq import heappush


def mostPopularCreator(creators, ids, views):
        
        # Output list to return
        output = []
        
        # Length of the lists
        n = len(creators)
        
        # Dictionary to keep the view count for each creator
        totalViews = {}
        
        # Another dictionary to keep track of the videos with their ids and views
        # We will use a maxHeap to order the videos for a creator based on their views
        videos = defaultdict(list)
        
        # What is the highest total view count for any creator
        highestCount = 0
        
        # Loop to fill the dictionaries with the data
        for i in range(n): 
            
            # Get the view count for the "i" creator so far
            count = totalViews.get(creators[i], 0) + views[i]
            
            # Update the "highestCount" if required
            highestCount = max(highestCount, count)
            
            # Update the "totalViews" dictionary
            totalViews[creators[i]] = count
            
            # Update the "videos" dictionary
            heappush(videos[creators[i]], [-views[i], ids[i], ids[i]])
        
        # Now, we simply want to return the creator with total views equal to "highestCount"
        # And for that creator,we want to return the id of the video having the highest views
        # And there can be multiple creators with same number of total view count
        # So, in that case, we have to return all of them
        
        # Go over each creator
        for key in totalViews:
            
            # If the total views are same as "highestCount"
            # Then put the creator's name and the id of the video with highest views in output
            if totalViews[key] == highestCount: output.append([key, videos[key][0][2]])
            
        
        # Finally, return the output
        return output


creators = ["alice","bob","alice","chris"]
ids = ["one","two","three","four"]
views = [5,10,5,4]

print("Output -> ", mostPopularCreator(creators, ids, views))