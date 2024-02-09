# PROBLEM STATEMENT

You have an infinite number of stacks arranged in a row and numbered (left to right) from 0, each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

 - DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks capacity.
 - void push(int val) Pushes the given integer val into the leftmost stack with a size less than capacity.
 - int pop() Returns the value at the top of the rightmost non-empty stack and removes it from that stack, and returns -1 if all the stacks are empty.
 - int popAtStack(int index) Returns the value at the top of the stack with the given index index and removes it from that stack or returns -1 if the stack with that given index is empty.
  
# EXAMPLE

    Input
    ["DinnerPlates", "push", "push", "push", "push", "push", "popAtStack", "push", "push", "popAtStack", "popAtStack", "pop", "pop", "pop", "pop", "pop"]
    [[2], [1], [2], [3], [4], [5], [0], [20], [21], [0], [2], [], [], [], [], []]

    Output
    [null, null, null, null, null, null, 2, null, null, 20, 21, 5, 4, 3, 1, -1]


# **1. BRUTE FORCE APPROACH**

The Brute Force solution is pretty simple. We just need to manage a list of all the stacks, and a variable capacity which denotes the maximum capacity of a stack.

Now, when "push" is called, we will iterate over the entire list of stacks, and find the leftmost stack with size < capacity. If we can find such a stack, then we will push the "val" in it. Otherwise, it means we have to push the value in a new stack.

When we pop the value form the rightmost stack, and after popping, the rightmost stack becomes empty, we will remove it from the list.

And when we have to pop a value from the stack at any index "i", we first check if that index is a valid index or not. If not, then we can return -1. Otherwise, we pop the element from the stack at index "i" and return that element.

The issue with this approach is the loop in the "push()" method. For every push() call, we are iterating over the entire list of stacks to find the leftmost stack. In worst case, we will be iterating over the entire list, only to find that there is no existing stack in which we can push or, it is the last stack. This is not an optimal approach and hence, we will get TLE.


# **2. HEAP APPROACH**

So, from Brute Force approach, we can understand that we need a way in which we can get the leftmost valid stack quickly when push() is called. We can use a data structure that keeps all the candidate stacks in it, and then gives us the stack with the smallest index at any time. And well, we can use a MIN HEAP for that.

So, as we push a new value using push(), we check if we have a candidate on top of the heap. If no, it means we have to push a new stack. Otherwise, we will push the value in that candidate stack and if it becomes full, we will remove it from the heap. Because note that this heap only keeps those stacks in it that are candidates for the "push()" method.

Similarly, when we pop() an element from a stack, we do not want to push it to the heap without checking. Why? Because if you do this, you will end up having duplicate values in the heap which is not something we want to do. Just think of this in this way -> If our heap has a stack with index "1" having 3 elements in it (max capacity is 4) and we pop an element from this stack, it now has "2" elements. So, if we now again push the index "1" to the heap, the heap will now have duplicate values.

We only want to push something to the heap if it is not already there. And the quickest way to ensure that is to only push a stack's index in the heap, if it was full before we popped an element from it. Because since it was full, it means it was not already in the stack. So after popping, it now has one less element to reach the max capacity so now it is a candidate.

That's why, in both pop() and popAtStack(), before we push to the heap, we are checking if - 

	len(self.stacks[-1]) == self.capacity - 1
	
That is, after popping, does this stack has one less element to reach max capacity? If yes, then push it to the heap. Otherwise, it means it is already present in the heap.

And well, that's the whole approach.