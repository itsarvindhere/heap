from collections import defaultdict
from heapq import heappop, heappush
class Twitter:

    def __init__(self):
        
        # For each user, we will maintain a dictionary to keep track of followings
        # So, "key" will be the "userId" and the value will be all the usersIds
        self.followings = defaultdict(set)
        
        # Another Dictionary to keep track of the news feed for each user
        # Key will be the "userId" and the value will be a Max Heap 
        # Max Heap is used to order the posts from most recent to least recent
        self.newsFeed = defaultdict(list)
        
        # A simple integer that we can use as the "timestamp" for each tweet
        # So that based on this we can order each tweet
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        
        # When a new Tweet gets posted, all the users that follow the "userId"
        # And also the "userId" themselves, will get this tweet in their newsFeed
        
        # First, update the time
        self.time += 1
        
        # Add it to the newsFeed of the "userId" 
        heappush(self.newsFeed[userId], [-self.time, tweetId, userId])
        
        # All the followers of "userId" should also get this tweetId in their newsFeed
        for user in self.newsFeed:
            
            # If this user follows "userID"
            # Then, we will add this "tweetId" in the newsFeed of that user
            if userId in self.followings[user]:
                heappush(self.newsFeed[user], [-self.time, tweetId, userId])
        

    def getNewsFeed(self, userId: int):
        
        # List of tweetIds that we have to return
        mostRecentTweets = []
        
        # New Max Heap
        newMaxHeap = []
        
        while len(mostRecentTweets) < 10 and self.newsFeed[userId]:
            
            top = heappop(self.newsFeed[userId])
            
            
            # LAZY DELETION
            # If the user that made the "top" tweet is not being followed by "userId" anymore
            # Then, we won't show it in the news feed and it should also not go into the new Max heap
            # This is more efficient than removing the tweets when a user unfollows someone
            
            
            # Otherwise, we can put it in the mostRecentTweets list amnd the newMaxHeap
            # Also, if the tweet was made by the same user as "userId" then also we need to consider this tweet
            if top[2] == userId or top[2] in self.followings[userId]:
                
                mostRecentTweets.append(top[1])
                
                heappush(newMaxHeap, top)
            
        # Put the remaining data in the newMaxHeap as well
        while self.newsFeed[userId]:
            
            # Ignore the tweets from users that are not being followed by "userId"
            top = heappop(self.newsFeed[userId])
            if top[2] == userId or top[2] in self.followings[userId]: heappush(newMaxHeap, top)
        
        # Now, the "newsFeed" of "userId" should be the "newMaxHeap"
        self.newsFeed[userId] = newMaxHeap
        
        # Return the most recent tweets
        return mostRecentTweets
        

    def follow(self, followerId: int, followeeId: int) -> None:
        
        # If the "followerId" is not already following "followeeId"
        if followeeId not in self.followings[followerId]:
            
            # Update the "followings" dictionary
            self.followings[followerId].add(followeeId)

            # Now, all the tweets made by "followeeId" will appear in newsFeed of "followerId"
            for data in self.newsFeed[followeeId]:

                # If this tweet was made by "followeeId"
                if data[2] == followeeId:
                    # Put this tweet in the newsfeed of "followerId"
                    heappush(self.newsFeed[followerId],data)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        # Update the "followings" dictionary
        if followeeId in self.followings[followerId]: self.followings[followerId].remove(followeeId)