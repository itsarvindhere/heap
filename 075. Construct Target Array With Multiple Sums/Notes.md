# PROBLEM STATEMENT

You are given an array target of n integers. From a starting array arr consisting of n 1's, you may perform the following procedure :

 - let x be the sum of all elements currently in your array.
 - choose index i, such that 0 <= i < n and set the value of arr at index i to x.
 - You may repeat this procedure as many times as needed.

Return true if it is possible to construct the target array from arr, otherwise, return false.

# EXAMPLE

    Input: target = [9,3,5]
    Output: true

Explanation: Start with arr = [1, 1, 1] 
[1, 1, 1], sum = 3 choose index 1
[1, 3, 1], sum = 5 choose index 2
[1, 3, 5], sum = 9 choose index 0
[9, 3, 5] Done

# APPROACH

So, we are given an input array and then asked if we can recreate that array if we start from a same sized array having all 1s.

	For example, if we have target = [9,3,5]
	
	Then, here is how we will receate it from [1,1,1]
	
	[1, 1, 1], sum = 3 choose index 1 and replace it with "3"
	[1, 3, 1], sum = 5 choose index 2 and replace it with "5"
	[1, 3, 5], sum = 9 choose index 0 and replace it with "9"
	[9, 3, 5] Done

Now, the issue with this flow is that, at any time, how will you decide which index to replace? If we had done [3,1,1] in second step above, then we would've never reached [9,3,5].

But, if we can generate [9,3,5] from [1,1,1], that means we can surely generate [1,1,1] from [9,3,5] by doing the steps in reverse, right? And that would be an easier approach because we do not have to worry about replacements. We know that at each index, we need a value "1" at the end.

So, how will we start? Note that in above approach, whatever index we replace, that index will get the largest element among all others. And that makes sense because tha element is the sum of all the elements. So ofcourse it is going to be larger than other elements. We can use this logic in reverse now.

	We start from the given target array [9,3,5]
	
	What is its sum? It is 17
	And what is the largest element? It is "9"
	
	This means, there must've been a previous step
	where the array was [x,3,5] 
	and x + 3 + 5 = 9
	
	Annd that's why we replaced "x" with "9" in next step to get [9,3,5]
	
	Now we want to do the opposite. 
	
	What does the largest element currently means?
	It means total sum was equal to this largest element 
	in the previous state of this array (which we are trying to recreate)
	
	So, to reach that state, we can reduce this largest element by the sum of other elements.
	
	That is, 9 - ( 3 + 5 ) => 9 - 8 => 1
	
	So, we want to replace "9" by "1" and so, we get [1,3,5]
	
	And now, we repeat this process.
	
	We now get the largest element currently, which is "5"
	
	And total sum of [1,3,5] is 9
	
	Since "5" is largest, it means it was the sum in the previous state of this array.
	
	So, we reduce it by the sum of other elements. That is
	
	5 - (1 + 3) => 5 - 4 => 1
	
	Now, the list becomes [1,3,1]
	
	And finally, "3" is largest and we do 3 - (1 + 1) => 3 - 2 => 1
	
	And we get [1,1,1]
	
	So, we were able to get to [1,1,1] from [9,3,5] hence we can return True.
	
As we saw, in each step, we wanted to get the largest element among all. We can do that quickly using a Max Heap. We also want to keep track of the total sum of the list at each stage because we will be updating it in each stage as it gets smaller and smaller.

So, it seems that the approach is pretty straightforward right? Well, there is one caveat with this solution. It will give TLE for some test cases.
Let's take a small test case to understand the issue.

	Let's say we have [3,20]
	
	If we go by the above approach, this is how the difference stages will look like - 
	
	Stage 1 => [3,20]
	Stage 2 => [3,17]
	Stage 3 => [3,14]
	Stage 4 => [3,11]
	Stage 5 => [3,8]
	Stage 6 => [3,5]
	Stage 7 => [3,2]
	Stage 8 => [1,2]
	Stage 9 => [1,1]
   
Did you notice something? From Stage 1 to Stage 7, the element that we replaced was at the index 1. And in each stage, all we did was reduced it by the remaining sum of the list. And from stage 1 to stage 7, this remaining sum never changed. It was always "3". While in this example, it does not seem like that big of a deal, imagine what would happen if there was a test case like this -

				[3,99999998]
				
In this case, we would keep decreasing the second number by "3" till it becomes less than "3". Do you think what can we do instead?

Well, we can instead do

	99999998 % 3
	
And that will give us the same result.

So, at any stage, if "x" is the largest element in the list, and "y" is the remaining sum of the list (except x), then, the value by which we must replace "x" with is - 

	x % y

And that's the biggest optimization you can add to this approach. The rest is simply handling the edge cases.

So, let's talk about the edge cases now.

	What if we have [1,20]?

	In this case, x % y will be 20 % 1 => 0
	
	So, does it mean we have to push "0" in place of "20" to get [1,0]?
	
	Well, no! Because the smallest value we want is "1". Since we are trying to reach to [1,1]
	
	If, at any stage, the remaining sum is "1", then it is definitely possible to get an array with all 1s.
	
	That's one thing to check.
	
Now, let's talk about another edge case.

	What if we have [2,4]
	
	Here, largest element = 4 and remaining sum = 2
	
	In this case x % y will be 4 % 2 => 0
	
	So, should we push "0" in place of "4" to get [2,0]?
	
	No! It is simply not possible to reach [1,1]
	
	And this is the case with any test case where the remaining sum is > 1
	and 
	largest element % remaining sum is 0
	
	That's second thing to check.
	
Let's talk about another edge case.

	What if we have [1,1,1,2]
	
	Here, the largest element = 2 and remaining sum = 3
	
	So, does it mean we have to push 2 % 3 => 2 ?
	
	Well, that doesn't make sense right? We are replacing 2 with 2
	
	Well, think about it. If we have [1,1,1,2]
	
	Then, since its largest element is "2", the previous state must've total sum of "2"
	
	But, how is total sum of "2" even possible for a list of size "4"?
	
	Because the smallest value at any index can be "1" as we want to reach [1,1,1,1]
	
	The reason is that at any case, the "largest element" can never is <= remaining sum.
	
	If we had [1,1,1,3] then also it would've been impossible because 3 <= 3
	But, if we had [1,1,1,4] then it would've been possible because 4 > 3
	
	And that's yet another thing to check for.

Finally, we have something we can check at the very beginning. And that's the length of the list.

	What if we had [1]
	
	In this case, largest element = 1 and remaining sum = 0
	
	So, if we tried to do 1 % 0, it will throw an error.
	
	But we know that [1] is already a valid list. So we can straight away return True.
	
	But for all other cases where there is only one element and it is not 1, we return False.
	
And well, that's the whole idea.