You are given a 0-indexed m * n integer matrix values, representing the values of m * n different items in m different shops. Each shop has n items where the jth item in the ith shop has a value of values[i][j]. Additionally, the items in the ith shop are sorted in non-increasing order of value. That is, values[i][j] >= values[i][j + 1] for all 0 <= j < n - 1.

On each day, you would like to buy a single item from one of the shops. Specifically, On the dth day you can:

 - Pick any shop i.
 - Buy the rightmost available item j for the price of values[i][j] * d. That is, find the greatest index j such that item j was never bought before, and buy it for the price of values[i][j] * d.

Note that all items are pairwise different. For example, if you have bought item 0 from shop 1, you can still buy item 0 from any other shop.

Return the maximum amount of money that can be spent on buying all m * n products.

# EXAMPLE

    Input: values = [[10,8,6,4,2],[9,7,5,3,2]]
    Output: 386

Explanation: On the first day, we buy product 4 from shop 0 for a price of values[0][4] * 1 = 2.
On the second day, we buy product 4 from shop 1 for a price of values[1][4] * 2 = 4.
On the third day, we buy product 3 from shop 1 for a price of values[1][3] * 3 = 9.
On the fourth day, we buy product 3 from shop 0 for a price of values[0][3] * 4 = 16.
On the fifth day, we buy product 2 from shop 1 for a price of values[1][2] * 5 = 25.
On the sixth day, we buy product 2 from shop 0 for a price of values[0][2] * 6 = 36.
On the seventh day, we buy product 1 from shop 1 for a price of values[1][1] * 7 = 49.
On the eighth day, we buy product 1 from shop 0 for a price of values[0][1] * 8 = 64
On the ninth day, we buy product 0 from shop 1 for a price of values[1][0] * 9 = 81.
On the tenth day, we buy product 0 from shop 0 for a price of values[0][0] * 10 = 100.
Hence, our total spending is equal to 386.

It can be shown that 386 is the maximum amount of money that can be spent buying all m * n products.

# **1. BRUTE FORCE APPROACH**
Looking at the contraints, it is not hard to figure out that the Brute Force approach will work.

It is given that at any day, we can buy one item among all the rightmost items in the shops. Also, we want to maximize our spending. So, it makes sense to buy the items with a higher price at later than the items with a lower price.

	For example, if at day 1, we can buy one item among three whos prices are -> 1,2,3
	
	Then, if we buy item with value "3" at this day, its price will be 3 * 1 => 3
	But, if we don't buy it on day 1 and instead buy it on day 2, the price will be 3 * 2 => 6
	Even better is when we buy it on the day 3 because in that case, the price will be 3 * 3 => 9

And that's the whole idea. At any day, among all the rightmost items in shops, we want the item with the lowest value.

In this way, we will buy the items with a higher value at the end where we will also spend more money.

# **2. SORTING APPROACH**

If you read the problem statement carefully, it clearly says that - 

	The items in the ith shop are sorted in non-increasing order of value. 
	That is, values[i][j] >= values[i][j + 1] for all 0 <= j < n - 1.
	
Always remember that there is always a reason if the problem already has provided the data in some sorted order.  

We know that at any day, we want the "smallest" item value among all the rightmost items.
We also know that for each shop, items are sorted in Decreasing order.

Doesn't it mean that the rightmost value in a shop is always the smallest value at any time for that shop?

So if you think about it, all that we are doing is simply buying items with values in this order -> lowest to highest

There is absolutely no need to worry about the "rightmost" thing because even if it was not explicitly mentioned in the problem, we would've always picked an item optimally among the rightmost items in the shops.

And so, we can simply take all the items, sort them by their value from lowest to highest, and then simply buy them in that same order.

# **3. MIN HEAP APPROACH**

This is just the same idea but using a Min Heap. So, instead of first getting all the items and then sorting them, we can have a Min heap that automatically orders them as we put items in it.