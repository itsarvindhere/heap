# PROBLEM STATEMENT

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

# EXAMPLE

    Input: words = ["i","love","leetcode","i","love","coding"], k = 2
    Output: ["i","love"]

Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

# APPROACH

The Sorting approach is pretty straightforward since in Python we can use the cmp_to_key method to use a custom compare function based on which sorting of items happens.

But, I did not know how we can do the same thing with a Heap in Python. 

Credits to this post for making it clear -> https://leetcode.com/problems/top-k-frequent-words/discuss/538903/Python-O(N-log(k))

Basically, to override the logic for the less than "<" operator, there is the __lt__ method in Python.

Under the hood, the heap will use the less than operator to compare two items and place them accordingly.

So, if we want to have a custom logic for the heap to order items, then we can override the __lt__ method inside our custom Wrapper class. And then, instead of pushing the values in the heap, we will wrap those values with this Wrapper class and then put the objects of this class in the heap.

In this way, when heap uses the "<" operator under the hood to compare, it will use the logic we had in the __lt__ method of that Wrapper class.

In the code below, the __lt__ method returns a boolean.

	False means "self" is not less than "other"
	True means "self" is less than "other"
	And since we are using a minHeap, it will place smaller values on top of the greater ones
	
So, if the frequency of "self" is greater than frequency of "other", we will return False which means "self" is not less than "other".
So, minHeap it will place "self" below "other". 

But if frequencies are the same, then we will check if self.word is lexicographically greater than other.word. If yes, then we return True. It means, in this case, self is less than other so "self" is placed on top of "other" in the minHeap.

It means, in case of same frequencies, the lexicographically smaller word is placed below the lexicographically greater one in the minHeap