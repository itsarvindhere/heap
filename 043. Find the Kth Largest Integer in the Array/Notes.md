# PROBLEM STATMENT

You are given an array of strings nums and an integer k. Each string in nums represents an integer without leading zeros.

Return the string that represents the kth largest integer in nums.

Note: Duplicate numbers should be counted distinctly. For example, if nums is ["1","2","2"], "2" is the first largest integer, "2" is the second-largest integer, and "1" is the third-largest integer.

# EXAMPLE

    Input: nums = ["3","6","7","10"], k = 4
    Output: "3"

Explanation:
The numbers in nums sorted in non-decreasing order are ["3","6","7","10"].
The 4th largest integer in nums is "3"

# APPROACH

The Heap and Sorting approaches are pretty simple. We just need to convert each element into an integer and then it becomes easier to sort them.

But, an interviewer expects a better solution.

We should be able to write a custom comparator method which does not rely on converting each string into an integer. 

In Python, we can use a method named "cmp_to_key(func)" from functools which lets us use our custom compare function as a key to sort elements.

And so, now, the main logic is in this custom compare function.

A comparator will take two arguments which are basically two elements that will be compared against each other to see which one is greater or smaller or whether they are both equal.

    If both are equal, this method returns 0
    If first is greater than second, this method returns 1
    If first is smaller than second, this method return -1

Since we are dealing with strings, the easiest way to compare two number strings is to check their lengths.

Ofcouse "10" is greater than "9" because length of "10" is 2 whereas length of "9" is 1. But, if you directly do "10" > "9" in python it will return False because it checks the first digit of both and in "10", it is "1", whereas in "9" it is "9". And since "9" > "1", it says that "9" is greater than "10".

That's why, we cannot directly check against two strings using less than or equal to operators.

Now, it is also possible that both have same lengths.

That is, if we have "10" and "19" then both have same length so now, we have to think of some other way to compare them.

We can loop over both from left to right and compare each digit. The place where both differ will decide which one is greater.

    At index 0, both "10" and "19" have digit "1"
    So, we move forward

    At index 1, "10" has "0" whereas "19" has "9"

    And since "0" is smaller than "9" it means, 

    "10" is smaller than "19"

And so, that's the main logic of our custom comparator.