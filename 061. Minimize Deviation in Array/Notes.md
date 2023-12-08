# PROBLEM STATEMENT

You are given an array nums of n positive integers.

You can perform two types of operations on any element of the array any number of times:

 - If the element is even, divide it by 2.
        
    - For example, if the array is [1,2,3,4], then you can do this operation on the last element, and the array will be [1,2,3,2].

 - If the element is odd, multiply it by 2.
        
    - For example, if the array is [1,2,3,4], then you can do this operation on the first element, and the array will be [2,2,3,4].

The deviation of the array is the maximum difference between any two elements in the array.

Return the minimum deviation the array can have after performing some number of operations.

# EXAMPLE

    Input: nums = [4,1,5,20,3]
    Output: 3

Explanation: You can transform the array after two operations to [4,2,5,5,3], then the deviation will be 5 - 2 = 3

# APPROACH

So basically, we are given that if we have an "odd" number, we can multiply it by 2. If we have an "even" number, we canb divide it by 2. And these are two operatons are can do on any number, any number of times.

First, you need to understand the concept of "deviation". As the problem statement says "deviation of the array is the maximum difference between any two elements in the array." And for any list, the maximum difference between any two elements is the "difference between maximum and minimum elements".

Now, if you take some examples, you will see that if we have an odd number, we can multiply it by 2 only once. And then, it will turn into an even number. So, basically, the multiplication operation can be done only once for any index. After that, it makes no sense to divide it by 2 and then again multiply by 2 as we will get the same number back.

So, based on this, what we can do is, we can use all of our "multiplication" operations once so that all the elements in the list are even numbers only.

	For example, if the input list is nums = [4,1,5,20,3]
	
	We can first convert all odd numbers to even by multiplying them by 2
	
	So, we will then get [4,2,10,20,6]
	
And now, all that we need to care about are the "division" operations. 

Now coming back to the deviation concept, since we have converted the list to all even numbers, now, both the maximum and minimum will be even numbers, right?

So, to get a smaller deviation, these two need to have a smaller difference.

And to get a smaller difference, we either need to "increase the minimum value" or "decrease the maximum value", right?

Now, since all elements are even only, the minimum and maximum will also be even. And for even numbers, we can only use division operation. In other words, we can only "reduce" a number, not "increase" it. And so, it means, the only option that we have is to "decrease the maximum value" in the list.

	So, coming back to the example -> 

	Our list was converted to [4,2,10,20,6]
	
	Now, the maximum value is 20
	And minimum value is 2
	
	The deviation of this list right now is 18
	
	Since "20" is even, we can take it and reduce it by dividing it by 2
	
	When we do that, the list becomes [4,2,10,10,6]
	
	And now, the maximum value is 10
	The minimum value is 2
	
	The deviation now becomes 10 - 2 => 8 which is smaller than previous deviation.
	
	Since "10" is still even, we can take it and reduce it by dividing it by 2
	
	When we do that, the list becomes [4,2,5,10,6]
	
	Now, maximum value is 10 and minimum is 2.
	
	So, deviation is still 8.
	
	Again, we can take "10' and divide it by 2
	
	When we do that, the list becomes [4,2,5,5,6]
	
	Now, maximum value is "6" and minimum is "2"
	
	And the deviation is "4" which is smaller than previous deviation.
	
	The greatest value is "6" and it is even. We can divide it by "2"
	
	The list becomes [4,2,5,5,3]
	
	Now, maximum value is "5" and minimum is "2"
	So, deviation is "3" which is smaller than previous deviation
	
Now comes the fun part. 

At this point, the list is [4,2,5,5,3] and now, the maximum value is "5". But, we can no longer reduce it by dividing it by 2 because it is an "odd" number at this point. And it makes no sense to multiply it by 2 because that will just increase the deviation since "5" will be converted to "10" and "10 - 2" will give us "8" which is higher than current deviation (3).

So, it means, when the maximum number in the list is an odd number, we know that there is no way to get a deviation smaller than the smallest we have got so far.

And so, for the list [4,1,5,20,3], output is "3".

Since we need to quickly get the maximum value in the list after we do the operation, the best way is to use a Max Heap.

 

