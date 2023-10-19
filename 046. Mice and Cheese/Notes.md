# PROBLEM STATEMENT

There are two mice and n different types of cheese, each type of cheese should be eaten by exactly one mouse.

A point of the cheese with index i (0-indexed) is:

 - reward1[i] if the first mouse eats it.
 - reward2[i] if the second mouse eats it.

You are given a positive integer array reward1, a positive integer array reward2, and a non-negative integer k.

Return the maximum points the mice can achieve if the first mouse eats exactly k types of cheese.

# EXAMPLE

    Input: reward1 = [1,1,3,4], reward2 = [4,4,1,1], k = 2
    Output: 15

Explanation: In this example, the first mouse eats the 2nd (0-indexed) and the 3rd types of cheese, and the second mouse eats the 0th and the 1st types of cheese.
The total points are 4 + 4 + 3 + 4 = 15.
It can be proven that 15 is the maximum total points that the mice can achieve.

# APPROACH

We are given that the first mouse will eat "k" types of cheese. This means, whatever cheese is left, the second mouse will eat all of that.

And since we want to maximize the points, we not only want the first mouse to get most points by eating "k" types of cheese, but we also want that the second mouse gets the maximum points by eating the rest.

	This means, If we have - 
	
		reward1 = [1,4,4,6,4]
		reward2 = [6,5,3,6,1]
		k = 1
		
	Then even though the maximum reward that first mouse can get is "6", we cannot let him eat this cheese.
	
	Why? Because let's say first mouse eats the cheese with "6" points.

	now, the second mouse can eat all the cheese left -> 6 + 5 + 3 + 1 => 16
	
	So, total points = 22
	
	But, that's not the maximum we can get.
	
	If the first mouse eats the last cheese, he gets "4" points.

	And now, second mouse can eat all the cheese left -> 6 + 5 + 3 + 6 =>20
	
	So, total points = 24
	
	And 24 is the maximum that we can get!
	
So, we cannot simply take the maximum from one list. We also have to consider the values in the other list.

The reason why feeding cheese with "6" points to first mouse is not optimal is because since the same cheese has "6" points for second mouse as well, the second mouse loses "6" points that it could've gained if it had eaten this cheese. 

But at the same time, when we feed the first mouse the cheese with "4" points, then the second mouse loses only "1" point that it would've received by eating the same cheese. So, the difference is big here between what the first mouse gets and what the second mouse loses.

And that's the whole point. We want to maximize this difference such that the first mouse gets the most and the second mouse loses the least.

And so, we want to choose the cheese based on this order only. And that's the idea of the two solutions.