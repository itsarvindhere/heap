# PROBLEM STATEMENT

Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.

# EXAMPLE

    Input: s = "cccaaa"
    Output: "aaaccc"

Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.

Note that "cacaca" is incorrect, as the same characters must be together.

# APPROACH

The approach is the same in all three solutions.

We first want the frequency of every character in the input string.

And once we have that data, we have three different solutions to use. We can either create a list with each element being a pair -> (frequency,character) and then sort that list in decreasing order.

In this way, the characters will be arranged from left to right in the order of their frequency from max to min. And then we just need to populate the final list.

We can also use a heap such that instead of creating a list first and then sorting it, we can keep adding pairs to the heap and the heap takes care of ordering automatically.

And finally, we have the Bucket sort approach.

See, since we have a string of length "n", it makes sense that a character can at most occur "n" times in the string. So, we have this range of 1 to n of the frequencies for the characters. And we can use bucket sort here. We will have a list of length "n" where each index represents the frequency. And at each index, we have a bucket that groups characters with same frequency together.

Since the indices are already sorted, there is no need to manually sort the list.