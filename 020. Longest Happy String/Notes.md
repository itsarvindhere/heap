# PROBLEM STATEMENT

A string s is called happy if it satisfies the following conditions:

- s only contains the letters 'a', 'b', and 'c'.
- s does not contain any of "aaa", "bbb", or "ccc" as a substring.
- s contains at most a occurrences of the letter 'a'.
- s contains at most b occurrences of the letter 'b'.
- s contains at most c occurrences of the letter 'c'.
  
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

# EXAMPLE

    Input: a = 1, b = 1, c = 7
    Output: "ccaccbcc"
    Explanation: "ccbccacc" would also be a correct answer.

# APPROACH

https://leetcode.com/problems/reorganize-string/

Here is my solution for that - https://leetcode.com/problems/maximum-total-importance-of-roads/discuss/3966617/python-simple-sorting-solution


Anyways, in this problem, we have to generate a string, instead of validating or reorganizing an existing one.

Based on the rules, the most optimal way to generate will be to always take the character with the maximum availability twice so that we can ensure that we won't have the same character thrice. We can do that by putting other characters between the character with the maximum availability so that we can reduce the chances of getting the same three characters.

	For example, a = 1, b = 3, c = 7
	
	Here, since "c" has the maximum availability, we will take it first
	
	So, we take 2 c's and string becomes "cc"
	
	Updated values => a = 1, b = 3, c = 5
	
	Again, "c" has the maximum availability but we cannot take "c" again
	Otherwise we will have a "ccc" pattern which we don't want
	
	So, we will now go for the second greatest value that is "b"
	But, we will only take one occurance of it 
	
	String becomes "ccb"
	
	Updated values => a = 1, b = 2, c = 5
	
	Now, we can take "c" twice again
	String becomes "ccbcc"
	
	Updated values => a = 1, b = 2, c = 3
	
	Again, we take "b" only once since we cannot take "c" at this point
	String becomes "ccbccb"
	
	Updated values => a = 1, b = 1, c = 3
	
	Again, we take "c" twice
	String becomes "ccbccbcc"
	Updated values => a = 1, b = 1, c = 1
	
	And now, since all values are available only 1 time,
	we can simply have "ccbccbccabc"
	
	And that's the final output
	
So with this example, it is easier to understand why we are only putting one occurance of the second greatest value and two occurances of the first greatest value. That's because we want to generate the longest possible valid string. So, we want to use the maximum occurances of greatest value but also want to make sure the character is not repeated more than twice in a row.

So, we have to keep track of the characters with the first greatest and the second greatest values at any time.

## **1. USING A MAXHEAP**

We can use a maxHeap to keep track of the first and second greatest characters and their values. Since it is a maxHeap, it will always have the maximum value on top. And as we update the values and push them back to the heap, the heap will take care of the ordering of values.

## **2. WITHOUT USING A MAXHEAP**
Since we only have three values a,b and c, using a MaxHeap just to get the first and second greatest value is kind of an overkill.

We can simply use a dictionary to keep track of the available occurances and two simple variables to keep track of first and second greatest values.

A simple for loop will give us the first and second greatest values at any time and this for loop will run in constant time as well.
