# PROBLEM STATEMENT

You are given an integer array heights representing the heights of buildings, some bricks, and some ladders.

You start your journey from building 0 and move to the next building by possibly using bricks or ladders.

While moving from building i to building i+1 (0-indexed),

 - If the current building's height is greater than or equal to the next building's height, you do not need a ladder or bricks.
 - If the current building's height is less than the next building's height, you can either use one ladder or (h[i+1] - h[i]) bricks.

Return the furthest building index (0-indexed) you can reach if you use the given ladders and bricks optimally.

# EXAMPLE

    Input: heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
    Output: 4

Explanation: Starting at building 0, you can follow these steps:
- Go to building 1 without using ladders nor bricks since 4 >= 2.
- Go to building 2 using 5 bricks. You must use either bricks or ladders because 2 < 7.
- Go to building 3 without using ladders nor bricks since 7 >= 6.
- Go to building 4 using your only ladder. You must use either bricks or ladders because 6 < 9.
It is impossible to go beyond building 4 because you do not have any more bricks or ladders.

# APPROACH

The most difficult thing to understand is how to choose when to use a ladder and when to use bricks to make a jump.

Because, if you try to use bricks first and then ladders then some test cases will not pass. Similarly, if you try to use ladders first and then bricks, then also some test cases will fail.

One thing that's not so hard to grasp is that ladders are quite valuable. Because just with 1 ladder, we can make a jump of any height. But, to make that same jump with bricks, we need at least that much amount of bricks. So, the optimal way would be to first try to make use of the bricks we can and if we don't have enough bricks, then think of some other way.

Let's take an example to understand how we will choose bricks vs ladders.

	heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
	
	b0 to b1, the height difference is 12 - 4 => 8
	
	So, we can either use 8 bricks or 1 ladder to make this jump
	Since we already decided to use bricks first, let's use 8 bricks here.
	
	Now, bricks left = 2 and ladders = 2
	
	Next, from b1 to b2, we don't require anything since 12 >= 2
	
	From b2 to b3, height difference is 7 - 2 => 5
	
	So, we need either 5 bricks or 1 ladder. 

	We don't have 5 bricks available so should we use a ladder here?
	
	Now, think about the first jump that we did. There, we used 8 bricks.
	
	But here, we require only 5. 
	
	So, wouldn't it be better to use a ladder instead of 8 bricks in the first jump?
	And that's the whole idea!
	
	In that way, we will still have 10 bricks left with us when we want to jump from b2 to b3.
	And we can simply use "5" bricks for this jump, leaving us with 5 bricks and 1 ladder.
	
	From b3 to b4, nothing required since 7  >= 3
	
	From b4 to b5, the height difference is 18 - 3 => 15
	
	So, we either need 15 bricks or 1 ladder.
	
	We only have 5 bricks here and in any of the previous jumps we did with bricks,
	we did not use 15 or more bricks there.
	
	So, the only option we have is to use a ladder here.
	
	Now, bricks remaining = 5 and ladder = 0
	
	From b5 to b6, height difference is 20 - 18 => 2
	
	Since we have only bricks left, we use 2 bricks.
	
	Now, bricks remaining = 3 and ladder = 0
	
	From b6 to b7, nothing is required since 20 >= 3
	
	From b7 to b8, height difference is 19 - 3 => 16
	
	We don't have enough bricks and ladders are already 0
	
	So, we cannot make this jump at all.
	
And so, the maximum building that we were able to reach was the building 7. Hence, we return "7".

So as we can see, when we cannot make a jump using bricks available, we want to check what is the maximum brick count that we used for any previous jump. And if we used more bricks for that previous jump than what we require in current jump, then we can make that previous jump using a ladder instead (if we have ladders available). And in this way, we will have enough bricks to make the current jump.

So basically, we are using ladders only for the big jumps.