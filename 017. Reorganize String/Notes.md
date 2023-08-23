# PROBLEM STATEMENT

Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.

# EXAMPLE

    Input: s = "aab"
    Output: "aba"


# APPROACH


The approach is quite simple.

We want to make sure no two adjacent characters are the same. The most optimal way is to consider those characters first that are occuring the most in the original string. In this way, we can put other characters between them so that no two characters are the same.

For example, if we have "aab", then in the output, we have to consider "a" as the first character, and then put "b" as second and "a" as third. 

To understand it even better, let's take a bigger example.

	s = "aaaabbbcc"
	
	Here, frequency of these characters is - 
	
	a => 4, b => 3 and c => 2
	
	output = []

	Since "a" has the most frequency at this point, 
	the most optimal approach is to take it in our output
	if the previous character is not the same
	
	At this point, output is empty to we can put "a" in it.
	
	output = ["a"]
	
	Updated frequencies are - a => 3, b => 3 and c => 2
	
	Here, again, "a" is having maximum frequency.
	
	But, we cannot take it because previous character in output is "a" only
	
	So, we have to take the character with the second maximum frequency, that is "b".
	
	output = ["a", "b"]
	
	Updated frequencies are - a => 3, b => 2 and c => 2
	
	Again, we take "a" 
	
	output = ["a", "b", "a"]
	
	Updated frequencies are - a => 2, b => 2 and c => 2
	
	Now, we take "b" since previous character was "a" so we cannot take "a" here
	
	output = ["a", "b", "a", "b"]
	
	Updated frequencies are - a => 2, b => 1 and c => 2
	
	Again, we take "a" 
	
	output = ["a", "b", "a", "b", "a"]
	
	Updated frequencies are - a => 1, b => 1 and c => 2
	
	Now, we take "c" since it is having the maximum frequency at this point
	
	output = ["a", "b", "a", "b", "a", "c"]
	
	Updated frequencies are - a => 1, b => 1 and c => 1
	
	Now, we can pick "a" again since previous character was "c"
	
	output = ["a", "b", "a", "b", "a", "c", "a"]
	
	Updated frequencies are - a => 0, b => 1 and c => 1
	
	We now pick "b"
	
	output = ["a", "b", "a", "b", "a", "c", "a", "b"]
	
	Updated frequencies are - a => 0, b => 0 and c => 1
	
	And finally, we pick "c"
	
	output = ["a", "b", "a", "b", "a", "c", "a", "b", "c"]
	
	Updated frequencies are - a => 0, b => 0 and c => 0
	
	
So, the final output is "ababacabc". There are multiple solutions possible so "ababacacb" is also a valid solution.
	
If you examine closely, after each step, we are picking the character with the maximum frequency at that point. And in case that character was picked before, we will pick the character with second maximum frequency at that point. 

So, we can use a data structure here that will give us the character with the maximum frequency at any time so that in each step, we don't have to manually order the characters by their frequencies. 

And well, we can use a heap for that. We will use a maxHeap here because we want the maximum frequency at any time or the second maximum.