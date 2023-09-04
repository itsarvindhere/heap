# PROBLEM STATEMENT

Alice and Bob take turns playing a game, with Alice starting first.

There are n stones in a pile. On each player's turn, they can remove a stone from the pile and receive points based on the stone's value. Alice and Bob may value the stones differently.

You are given two integer arrays of length n, aliceValues and bobValues. Each aliceValues[i] and bobValues[i] represents how Alice and Bob, respectively, value the ith stone.

The winner is the person with the most points after all the stones are chosen. If both players have the same amount of points, the game results in a draw. Both players will play optimally. Both players know the other's values.

Determine the result of the game, and:

 - If Alice wins, return 1.
 - If Bob wins, return -1.
 - If the game results in a draw, return 0.

# EXAMPLE

    Input: aliceValues = [2,4,3], bobValues = [1,6,7]
    Output: -1

Explanation:
Regardless of how Alice plays, Bob will be able to have more points than Alice.
For example, if Alice takes stone 1, Bob can take stone 2, and Alice takes stone 0, Alice will have 6 points to Bob's 7.
Bob wins.

# APPROACH

As the problem statement says, Alice and Bob both will play optimally and they both know what is the value of stone for other person.

Now, think about it. 

Initially, we may think that the best option is for each to choose the stone that gives them the maximum points, right?

But, will this strategy work for all the cases?

	Let's take an example => aliceValues = [1,5] and bobValues = [7,1]
	
	Let's go by the strategy of removing maximum valued stone.
	
	Since Alice plays first, she will choose the stone at index 1 with value "5"
	So, alice's points = 5
	
	In next move, Bob will remove the stone at index 0 with value "7"
	So, bob's points = 7
	
	So going by this strategy, Alice lost!
	
Now, think about some other strategy by which Alice may win or at least the game ends in a draw. 

There is a reason why this problem says "**Both players know the other's values.**"

I mean, if I am playing this game then my thinking would be to remove a stone such that not only I get some points, but it also removes the stone that my opposition might remove in next round.

And well, that's the most optimal strategy.

	This means, when choosing a stone to remove
	We should not just consider our profit
	But also consider the loss of the opposition
	
	We want to maximize these two values together
	We want to increase our profit and also decrease the loss of opposition
	And this sum of (profit + loss) should be maximum
	
	Coming back to the example -> [1,5] and [7,1]
	
	Alice should remove stone at index 0 initially because doing that mean - 
	
		Alice gets profit of 1 point
		Bob loses 7 points
		
		So, total 1 + 7 => 8
		
	And this is the maximum sum value in this list and so stone at index 0 must be removed first
	
	So, Alice removes the stone at index 0 and gets 1 point
	Now, bob removes stone at index 1 and gets 1 point as wel
	
	
	And so, the game ends in a draw, instead of Alice losing.

Hence, what we understood is that we need to order the stones by the sum of aliceValues[i] + bobValues[i] for each stone i.

And so, we will sort the stones accordingly.