# PROBLEM STATEMENT

You have a water dispenser that can dispense cold, warm, and hot water. Every second, you can either fill up 2 cups with different types of water, or 1 cup of any type of water.

You are given a 0-indexed integer array amount of length 3 where amount[0], amount[1], and amount[2] denote the number of cold, warm, and hot water cups you need to fill respectively. Return the minimum number of seconds needed to fill up all the cups.

# EXAMPLE

    Input: amount = [5,4,4]
    Output: 7

Explanation: One way to fill up the cups is:
Second 1: Fill up a cold cup, and a hot cup.
Second 2: Fill up a cold cup, and a warm cup.
Second 3: Fill up a cold cup, and a warm cup.
Second 4: Fill up a warm cup, and a hot cup.
Second 5: Fill up a cold cup, and a hot cup.
Second 6: Fill up a cold cup, and a warm cup.
Second 7: Fill up a hot cup.

# APPROACH

After analysing the examples, what we can see is that in each second, the best approach is to reudce the two greatest values if both are not 0 yet. 

If we don't have two non-zero values, then obviously we can only fill one cup in a second.

But, if we think more, then there is also a one liner solution possible. You can check the comments in that solution to understand easily.

