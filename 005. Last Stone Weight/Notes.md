# PROBLEM STATMENT

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

 - If x == y, both stones are destroyed, and
 - If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.

At the end of the game, there is at most one stone left.

Return the weight of the last remaining stone. If there are no stones left, return 0.

# EXAMPLE

    Input: stones = [2,7,4,1,8,1]
    Output: 1

Explanation: 
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.


# **1. BRUTE FORCE APPROACH**

In the Brute Force approach, we first sort the input list so that we know the last two stones are the ones we need to consider first.

But then, if the two stones are different, we have to push a new stone of weight (firstHeaviest - secondHeaviest) to the list.

And now, since we want to make sure the list remains in sorted order, we have to again manually sort the list after we push a new weight.

So as you can see, this is not optimal to keep sorting the list again and again as we push a new weight.

I mean, yes, we do want to make sure the list is in sorted order, but do you think we always want to sort the whole list again?

	Take this example [1,1,1,1,1,1,1,1,1,1,10,20]
	
	Initially, when this list is sorted, we will take 10 and 20. 
	
	So list becomes [1,1,1,1,1,1,1,1,1,1]
	
	Then, since these two are not same, we now have to push a new weight (20 - 10) into this list.
	
	So, we push it and list becomes [1,1,1,1,1,1,1,1,1,1,10]
	
	But now, is there any need to sort the whole list again? There is absolutely no need. 
	
	But still, for similar cases, our Brute Force approach will again sort the whole list and this will just increase the running time.
	
	You may argue that it is not always necessary that when we push, the element is already at correct place. Yes, you're right.
	
	Suppose, we had  [1,1,1,1,1,1,1,1,4,8,10]
	
	In this case, when we take the last two stones, since they are not same, we have to push (10 - 8) into the list.
	
	So list becomes [1,1,1,1,1,1,1,1,4,2]
	
	And now, we see that again, there is no need to sort the whole list.
	
	We just want to sort this small portion [4,2] because the previous part is already sorted.

So, that's the issue in the Brute Force approach, even though it is accepted. It is accepted only because the constraints are quite small since list size can be up to 30 only.

# **2. HEAP APPROACH**
So, how can we optimize this approach? 

Is there any data structure that can automatically rearrange the element in a specific order (increasing or decreasing), as we give a new element to it? And we want that it does the sorting in an efficient manner.

Yes. That data structure is a HEAP.

So, instead of sorting the list again and again, we will maintain a MaxHeap. Max Heap means the element on the top at any time is the maximum.

In Python, the default heap implementation is Min-Heap. So to convert it to a MaxHeap, we can multiply each element by -1.

And well, the rest of the code is exactly the same as the Brute Force approach. 