# PROBLEM STATEMENT

You are given two string arrays creators and ids, and an integer array views, all of length n. The ith video on a platform was created by creator[i], has an id of ids[i], and has views[i] views.

The popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator with the highest popularity and the id of their most viewed video.

 - If multiple creators have the highest popularity, find all of them.
 - If multiple videos have the highest view count for a creator, find the lexicographically smallest id.

Return a 2D array of strings answer where answer[i] = [creatori, idi] means that creatori has the highest popularity and idi is the id of their most popular video. The answer can be returned in any order.

# EXAMPLE

    Input: creators = ["alice","bob","alice","chris"], ids = ["one","two","three","four"], views = [5,10,5,4]
    Output: [["alice","one"],["bob","two"]]

Explanation:
The popularity of alice is 5 + 5 = 10.
The popularity of bob is 10.
The popularity of chris is 4.
alice and bob are the most popular creators.
For bob, the video with the highest view count is "two".
For alice, the videos with the highest view count are "one" and "three". Since "one" is lexicographically smaller than "three", it is included in the answer.

# **1. USING DICTIONARY + MAX HEAP - O(NLogN)**
In this approach, we will use two dictionaries. One will have the data about the total view count for each creator, and the other will have the data about the "videos" and "ids". 

If a creator has got the most views, we quickly want to fetch the video with the highest videos. So, for that reason, we will use a maxHeap to do so. Each value in the maxHeap will be a triplet -> [video views, id, id]. 

We use a triplet so that the second value can be used for tie-breaker. If two videos have same views, we want to give priority to the one with a smaller id. That's why, the second value pushed is an id.

And finally, all that we have to do is to pick all those creators that have got the highest views and put their video with highest views in the output list along with the id.

# **2. USING JUST ONE DICTIONARY - O(N)**

If you think a bit, there is no need to keep track of all the videos of a creator. We just want to know that one video which has the highest views for a creator. That's it. It means, there is no need to use a maxHeap at all.

We just want to keep this one data which is the highest views on a video, and its id.

And also, instead of two dictionaries, we can use just one.

This single dictionary will have all the required data -> [video with most views, id of the video, total views for this creator]