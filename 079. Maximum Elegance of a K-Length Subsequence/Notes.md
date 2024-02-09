# PROBLEM STATEMENT

You are given a 0-indexed 2D integer array items of length n and an integer k.

items[i] = [profiti, categoryi], where profiti and categoryi denote the profit and category of the ith item respectively.

Let's define the elegance of a subsequence of items as total_profit + distinct_categories2, where total_profit is the sum of all profits in the subsequence, and distinct_categories is the number of distinct categories from all the categories in the selected subsequence.

Your task is to find the maximum elegance from all subsequences of size k in items.

Return an integer denoting the maximum elegance of a subsequence of items with size exactly k.

Note: A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the remaining elements' relative order.

# EXAMPLE

    Input: items = [[3,2],[5,1],[10,1]], k = 2
    Output: 17

Explanation: In this example, we have to select a subsequence of size 2.
We can select items[0] = [3,2] and items[2] = [10,1].
The total profit in this subsequence is 3 + 10 = 13, and the subsequence contains 2 distinct categories [2,1].
Hence, the elegance is 13 + 22 = 17, and we can show that it is the maximum achievable elegance. 

# APPROACH

The elegance of a subsequence is given as - 

	total_profit + distinct_categories^2
	
This means, for the maximum elegance, we need to maximize not just the profit, but also the distinct categories. Ofcourse it is not always possible that both are maximized at the same time so we want to balance them such that the elegance value we get is the maximum.

When we have such problems, we can try to maximize one part first, and then try to work on the other part. Here, we will do the same. We can try to maximize the total_profit first. And that is pretty simple. We just need to sort the items by their "profit" values in decreasing order, and then pick the first "k" items for our subsequence. That will be the "k" length subsequence with highest "total_profit".

Now that our profit is maximized, we want to increase the "distinct_categories" in our subsequence. 

Let's take an example to understand how that will be done.

	Suppose, we have items = [[3,2],[5,1],[10,1]], k = 2
	
	When we sort items in decreasing order of their profit, we get - 
	
		items = [[10,1], [5,1], [3,2]]
		
	So, the "k" length subsequence with highest total_profit is [[10,1],[5,1]]
	
	And for this, elegance is (10+5) * 1 => 16
	
	Now, how can we increase this elegance further?
	
	We have already maximized "total_profit".
	
	So, the other term we can play around with is "distinct_categories"
	
	Currently, the distinct_categories is "1"
	
	But, what if, we can remove one item and replace it with an item with a different category?
	
	That will increase the distinct_categories count to "2"
	
	We have [3,2] and we can replace either [10,1] or [5,1]
	
	We can replace some item because [3,2] has a category "2" 
	which is not already present in the current subsequence.
	
	It means, addin this item will increase the distinct_categories.
	
	Now, which one to replace among [10,1] and [5,1]?
	
	Ofcourse it is the one that has a lower profit value because remember that,
	we want to balance "total_profit" and "distinct_categories"
	
	So, we replace and the new subsequence we get is [[10,1],[3,2]]
	The new elegance is (10 + 3) + (2*2) => 17
	
	And this is higher than previous elegance value.
	
	So, the maximum elegance possible is "17".
	
And this is the idea.

# **1. USING A MIN HEAP**

We first get the "k" length subsequence with the highest total_profit value. When we create that subsequence, if current item has a category that is already present in the subsequence, we also add that item to a minHeap which keeps all the candidates which can be replaced by other items in the range [k,n-1]. This minHeap will order them by their profit values from smallest to largest. So at any time, the item we will replace will always be the one having the smallest profit.

As we saw in above example, we could replace an item with [3,2] only because the category "2" is not already present in the subsequence. And that's the logic we also use in the code. We only do this replacement if the current item's category is not already present. And to keep track of this, we can use a Set. If current item's category is not present already, it means adding this new item will increase the distincts_count value and might also increase the elegance (not always the case).

So, we will update the elegance accordingly.

# **2. WITHOUT USING A MIN HEAP**
Since we have already sorted the items by profit in decreasing order, it means, when we get the candidates that can be replaced, they will also be in a sorted order based on their profit values from highest to lowest. So, there is no need to use a Heap. Instead, we can use a simple list and at any time, the item that we should replace will always be at the end of this list.