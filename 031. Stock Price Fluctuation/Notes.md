# PROBLEM STATEMENT

You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

Design an algorithm that:

 - updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
 - Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
 - Finds the maximum price the stock has been based on the current records.
 - Finds the minimum price the stock has been based on the current records.
  
Implement the StockPrice class:

 - StockPrice() Initializes the object with no price records.
 - void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
 - int current() Returns the latest price of the stock.
 - int maximum() Returns the maximum price of the stock.
 - int minimum() Returns the minimum price of the stock.

# EXAMPLE

Input
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]

Output
[null, null, null, 5, 10, null, 5, null, 2]

Explanation
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // Timestamps are [1] with corresponding prices [10].
stockPrice.update(2, 5);  // Timestamps are [1,2] with corresponding prices [10,5].
stockPrice.current();     // return 5, the latest timestamp is 2 with the price being 5.
stockPrice.maximum();     // return 10, the maximum price is 10 at timestamp 1.
stockPrice.update(1, 3);  // The previous timestamp 1 had the wrong price, so it is updated to 3.
                          // Timestamps are [1,2] with corresponding prices [3,5].
stockPrice.maximum();     // return 5, the maximum price is 5 after the correction.
stockPrice.update(4, 2);  // Timestamps are [1,2,4] with corresponding prices [3,5,2].
stockPrice.minimum();     // return 2, the minimum price is 2 at timestamp 4.

# APPROACH

One thing that is pretty straightforward to understand is that we would need a dictionary or a hashmap in this problem so that we can easily keep track of at any timestamp, what was the price of the stock. 

So that's one part. 

And it is also quite easy to keep track of what is the latest timestamp. 

But, what's not easy to figure out is how to efficiently keep track of the prices of the stock so far and get the maximum and minimum out of those prices efficiently. 

We cannot use a simple variable "maximum" and update its value accordingly. Because, what if this is no longer the maximum? Then, what will be the next maximum? 

We want a way through which we order the prices in such a way that we can easily get the maximum price so far. But, in case that price is no longer maximum because we have changed the price on that particular timestamp, we can then easily get the next maximum value. And that's something a MAX HEAP can do.

Similarly, for the "minimum" price we can use a MIN HEAP to keep track of minimum prices of the stock.


	Let's say that we have our data so far as following - 
	
		{1 : 10, 2 : 5, 3: 7}
		
	So, it means at timestamp 1, price was 10
	At timestamp 2, price was 5
	and at timestamp 3, price was 7
	
	Now, our maxHeap will have values like this - [(10,1), (7,3), (5,2)] (Ignore the negative symbol for now)
	And, our minHeap will have values like this - [(5,2), (7,3), (10,1)]
	
	On every "update" method call, we will push the new pair in both the heaps.
	
	Let's say we run update(1,9)
	
	It means, at timestamp 1, update the price to be "9"
	
	So, dictionary becomes {1 : 9, 2 : 5, 3: 7}
	
	And we push the pairs in both the heaps.
	
	Now, our maxHeap will have values like this - [(10,1), (9,1) (7,3), (5,2)]
	And, our minHeap will have values like this - [(5,2), (7,3), (9,1), (10,1)]
	
	Notice how we did not remove the old values in this update call.
	
	Now, the next time maximum() is called, we will not immediately return the top value.
	Because we know that the top may have some data that is already been updated.
	
	So, we will first check against the dictionary whether the data on top of valid at that point or not.
	
	Here, in the maxHeap, top data is (10,1) which says that at timestamp 1, the value was 10
	
	But if we see the dictionary, it says at timestamp 1, the value was 9
	
	hence, the data in maxHeap is not valid now. So we will pop it and move to the next maximum data.
	
	Next, we have the pair (9,1) which says that at timestamp 1, the value was 9.
	
	And it is correct as per the dictionary too. So, it means, we found the maximum value that we have to return here.
	
	So, we will return "9".
	
And this same logic applies to the minHeap too when we want the minimum price of the stock so far.
 