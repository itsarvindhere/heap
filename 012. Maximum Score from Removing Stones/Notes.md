# PROBLEM STATEMENT

You are playing a solitaire game with three piles of stones of sizes a​​​​​​, b,​​​​​​ and c​​​​​​ respectively. Each turn you choose two different non-empty piles, take one stone from each, and add 1 point to your score. The game stops when there are fewer than two non-empty piles (meaning there are no more available moves).

Given three integers a​​​​​, b,​​​​​ and c​​​​​, return the maximum score you can get.

# EXAMPLE

    Input: a = 2, b = 4, c = 6
    Output: 6

Explanation: The starting state is (2, 4, 6). One optimal set of moves is:
- Take from 1st and 3rd piles, state is now (1, 4, 5)
- Take from 1st and 3rd piles, state is now (0, 4, 4)
- Take from 2nd and 3rd piles, state is now (0, 3, 3)
- Take from 2nd and 3rd piles, state is now (0, 2, 2)
- Take from 2nd and 3rd piles, state is now (0, 1, 1)
- Take from 2nd and 3rd piles, state is now (0, 0, 0)
There are fewer than two non-empty piles, so the game ends. Total: 6 points.

# APPROACH

This is a greedy problem because we have to maximize our score by optimally choosing the two piles to decrement the values from.

The most optimal approach would be to choose the two piles with most number of stones in each iteration.

So, we need a way to keep track of those two piles in each iteration.

The first way is using extra space.

We will use a Max Heap that we can use to get the two greatest values at any time. And as we decrement the values, this maxHeap will take care of the ordering as well.

But, if you think about it, there is no need to use a maxHeap because we have only 3 values to play aroun with. And we can easily keep track of what is the first greatest and the second greatest.

And this solution uses that same logic. We will first make sure "a" is the first greatest value, "b" is the second greatest value and "c" is the third greatest value. And we will maintain this order going forward. So, in each iteration, after we are done decrementing "a" and "b", we will then update the "a", "b" and "c" based on which is the first, second and third greatest.

And we know that when the second greatest value becomes 0, it means there are less than 2 non-empty piles left with us so we can exit the loop.

