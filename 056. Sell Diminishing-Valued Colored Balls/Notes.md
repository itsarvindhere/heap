# PROBLEM STATEMENT

You have an inventory of different colored balls, and there is a customer that wants orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number of balls of that color you currently have in your inventory. For example, if you own 6 yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of balls of the ith color that you initially own. You are also given an integer orders, which represents the total number of balls that the customer wants. You can sell the balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. As the answer may be too large, return it modulo 10^9 + 7.

# EXAMPLE

    Input: inventory = [2,5], orders = 4
    Output: 14

Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).

The maximum total value is 2 + 5 + 4 + 3 = 14

# **1. HEAP APPROACH - TLE**

This is probably the simplest solution one can write for this problem.

Since we want our profit to be maximum, the ideal way would be to sell those balls first that are available in the maximum quantity. So, at any time, we should know what ball is available in maximum quantity and we should sell that. 

Here, we can use a Max Heap which can give us this information about which colored ball has the maximum quantity at any time. So, we can sell one such ball and our profit will increment by "quantity" and orders will reduce by 1.

But, the issue with this approach is that it is not efficient for large test cases. Suppose we have inventory as [1000000000] and orders are 1000000000.

In this case, our "while" loop will run "1000000000" times and in each iteration, we will take the greatest, which always remains the same ball, reduce its quanitity by 1, push it back to heap, update orders and update profit. This just take too much time and hence we get TLE.

# **2. BETTER HEAP APPROACH - TLE**

One thing we saw in above approach was that, even if we were picking same colored ball in multiple iterations, we were just reducing the quantity by 1 in each iteration.

If we know that we have to sell the "i" ball for the next "x" orders, why not just take "x" balls and sell them? Makes sense, right?

So, we can improve this code further.

Let's say we have 
		
		inventory = [5,2]
		
		So, just for the sake of understanding
		"red" balls are 5
		"blue" balls are 2
		
		We see that since 5 - 2 = 3
		
		For the next (3 + 1) => 4 orders,
		we can sell "red" colored ball
		
		So, 
		in order 1, we sell one red ball so profit = 5
		Now, "red" balls are 4
		in order 2, we sell one red ball so profit = 5 + 4
		Now, "red" balls are 3
		in order 3, we sell one red ball so profit = 5 + 4 + 3
		Now, "red" balls are 2
		in order 4, we sell one red ball so profit = 5 + 4 + 3 + 2
		Now, "red" balls are 1
		
		And now, if next order comes, we cannot sell "red" ball
		Because now, we have "1" red ball and "2" blue balls
		So, we should sell a blue ball instead so that profit increases by 2
		
And that's the optimization we can add to our Heap Approach. We will now get not just the greatest value at any time, but also the second greatest.

So that we can quickly sell certain number of balls of a color instead of selling one by one in each iteration.

But, even this approach will fail. 

	Because, just think of a test case like [1000000000,1000000000]

In this case, since difference between first and second greatest is 0, it means, we can only sell 1 ball in each iteration
	
And this basically repeats the situation we had in initial approach.


# **3. SORTING APPROACH - ACCEPTED**
And now, we come to the Accepted solution. 

I was not able to come up with this code but thanks to this YouTube video for giving an idea of this approach - https://www.youtube.com/watch?v=vl915tFlhJM

The code might seem a bit overwhelming at first but believe me, when you get the main idea, you'll understand it very easily.

We first sort the input list in Decreasing order so that values are ordered from highest to lowest. 

Let's draw a graph to understand it better.

Suppose, input is [2,6,7,1] and orders = 12

After sorting, input = [7,6,2,1]

![image](https://assets.leetcode.com/users/images/0e4f79d7-3f37-491d-a579-af1436760cef_1699980040.2093432.png)

Let's also color these balls so we have 7 red, 6 blue, 2 yellow and 1 green ball.

Now, we start from first value which is "7". The value after it is "6". The difference between the two is "1". So it means, we can be sure that for the next "1" order(s), we can sell "red" ball only. Makes sense, right?

Okay. So, we sell "1" red ball and so, now orders = 11 and profit = 7

Now, our graph looks like this - 

![image](https://assets.leetcode.com/users/images/f4367209-57f7-45c2-8ed4-4ef7d244686b_1699980253.3282816.png)

So, we have "6" blue balls. And since next value is "2", the difference is "6 - 2" => 4

It means for the next "4" orders, we can sell the blue balls.

But now comes the fun part. Since there are same number of "red" balls as the "blue" balls. It means, we can also sell "4" red balls in the next "4" orders after the next "4" orders. 

In other words, we can sell "8" total balls in next "8" orders among which "4" will be red balls and "4" will be "blue" balls. 

And since we still have "11" orders to complete, it means we can indeed sell all the "8" balls. 

So now, orders become "2" but what about profit? How to calculate it now?

See, we have "2" different colored balls that we can sell right now.
And from each color, we take "4" balls.

So, for one color, let's say "blue", profit from selling "4" balls is -> 6 + 5 + 4 + 3 =? 18
So it means, for "2" different colored balls, total profit will be "2 * 18" => 36

But, how to calculate this summation "6 + 5 + 4 + 3" quickly since it can get pretty huge for big test cases?

And here, we can use the formule for the "Sum of N Natural Numbers".

	For calculating the Sum from "1" to "N" we can do  (N * (N + 1)) / 2
	
	But in our case, we need sum of 3 + 4 + 5 + 6
	
	So, First we can calculate the sum 1 + 2 + 3 + 4 + 5 + 6
	And then, we can calculate the sum 1 + 2
	
	And if we subtract the two, we will get 3 + 4 + 5 + 6
	
	Makes sense?
	
And that's how we can quickly find the sum as well.

So, now, orders left = 3, profit = old profit (7) + 36 => 43

And the graph now looks like this - 

![image](https://assets.leetcode.com/users/images/7346a8bd-5b7e-4945-aa8a-8bddd1cd26a4_1699980697.122881.png)

So now, you should be getting an idea of how we are selling balls efficiently, right?

In next iteration, we have value = 2. And different between current and next is "2 - 1" => 1

So, for next 1 order(s), we can sell "1" yellow ball.

And this also means, we can sell "1" red and "1" blue ball as well since those are also available in same quantity as the yellow ball.

And luckily in this test case, orders remaining are also "3" so we can sell each one of these balls.

Profit will be 2 + 2 + 2 => 6 and now, all orders are done.

And so, Maximum profit = 43 + 6 => 49

---------------------------------------------------------------------------

Now, the above test case did not have any edge cases.

But in maximum test cases, there will be a situation when we have more balls available to sell than the orders. And in that case, it might become complicated to choose balls to sell and then to calculate the profit.

Let's take the same test case with different orders count.

Suppose, inventory = [7,4,2,1] and orders = 6

![image](https://assets.leetcode.com/users/images/c6c13973-4feb-4bc0-b256-f76bd309d41c_1699981677.7803187.png)

Again, initially, first value is "7" and next is "4" so for the next "7 - 4" => 3 orders, we can sell the Red ball.

Now, orders = 3 and profit = 7 + 6 + 5 => 18

![image](https://assets.leetcode.com/users/images/b1b142bc-5568-4b4f-96bb-41780adec785_1699981758.6528196.png)

In next iteration, the value is "4". Next value is "2" so for the next "4 - 2" => 2 orders, we can sell the "Blue ball". And since the "Red" ball is also having same quantity, we can also sell "2" Red balls at this point.

So, total balls available to sell are "4". But, the orders remaining are only "3".

Now this is the case that is a bit complicated.

We cannot sell "2" balls each from the "2" available colors. 

But, how many maximum balls we can sell from each color? We can definitely sell "1" ball each. That is, 1 "red" and 1 "blue" ball.

This means, We can still use the "Sum of N natural numbers" formula here at least when we are selling "x" amount of balls for each color.

For "1" blue ball, profit is "4". So, for 1 blue and 1 red => 2 balls, the profit is "8"

Hence, overall profit = old profit + 8 => 18 + 8 => 26

So, at this point, we now have "3" red balls and "3" blue balls.

But, we still have "1" order left to fulfil. And here, we can either select "1" red or "1" blue ball. Doesn't matter which one you choose, because after this order, we are done.

Let's say we chose "1" red ball. So, profit = old profit + 3 => 26 + 3 => 29

And we are done!

So, it means, when we have less orders than the available balls to sell, we have two steps.

	First, find how many balls to sell from each available color => orders // available colors
	Second, find how many extra balls to sell to finish the orders => orders %  number of different colors we can choose
	
	So for example, in above case
	
	We have "2" available colors -> Red and Blue
	And orders are "3"
	
	So, how many balls to sell from each color -> 3 // 2 => 1
	And how many extra balls to sell to finish the orders -> 3 % 2 => 1
	
And then, we can get the combined profit and add it to the overall profit.

And that's the whole approach. PHEW!