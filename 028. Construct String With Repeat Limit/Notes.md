# PROBLEM STATEMENT

You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.

Return the lexicographically largest repeatLimitedString possible.

A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.

# EXAMPLE

    Input: s = "cczazcc", repeatLimit = 3
    Output: "zzcccac"

Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
The letter 'a' appears at most 1 time in a row.
The letter 'c' appears at most 3 times in a row.
The letter 'z' appears at most 2 times in a row.
Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.

# APPROACH

We want the "Lexicographically largest repeatLimitedString possible".

What does that mean?

It means, we want the put the greatest characters in the string in the beginning, followed by the smaller ones. But, we are also given the limit which indicates how many characters we can put in a row.

	So, if we have as string as "abcdzzzzzz" and limit = 3
	
	It means we cannot have an output string that starts with "zzzzzz" or "zzzzz" or "zzzz"
	because we can repeat "z" only "3" times in a row.
	
	Since we can only repeat it "3" times in a row, the best way would be - 
	
	First use at most "3" z characters -> output = "zzz"
	
	Since we cannot use "z" again, use one second greatest character
	Here, second greatest is "d" so we put it in output
	
	output = "zzzd"
	
	And now, as you can see, we can again use multiple "z" together.
	
	output  ="zzzdzzz"
	
	And that's the whole idea.
	
Since we want the greatest characters to be in the beginning, if we reach the limit and we still have a particular character to use that is the greatest at that time, we will put one second greatest character in between so that we can again use the greatest character at most "limit" number of times.

And to keep track of the greatest characters, we have three different options. We can either sort the characters that the string has, or we can use a maxHeap which will give us the greatest and second greatest character at any time, or we can use a simple list of length "26" to keep track of the characters and their frequencies.