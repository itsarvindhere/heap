A scenic location is represented by its name and attractiveness score, where name is a unique string among all locations and score is an integer. Locations can be ranked from the best to the worst. The higher the score, the better the location. If the scores of two locations are equal, then the location with the lexicographically smaller name is better.

You are building a system that tracks the ranking of locations with the system initially starting with no locations. It supports:

 - Adding scenic locations, one at a time.
 - Querying the ith best location of all locations already added, where i is the number of times the system has been queried (including the current query).
  
     - For example, when the system is queried for the 4th time, it returns the 4th best location of all locations already added.

Note that the test data are generated so that at any time, the number of queries does not exceed the number of locations added to the system.

Implement the SORTracker class:

 - SORTracker() Initializes the tracker system.
 - void add(string name, int score) Adds a scenic location with name and score to the system.
 - string get() Queries and returns the ith best location, where i is the number of times this method has been invoked (including this invocation).

# EXAMPLE

Input
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]

Output
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

Explanation
SORTracker tracker = new SORTracker(); // Initialize the tracker system.
tracker.add("bradford", 2); // Add location with name="bradford" and score=2 to the system.
tracker.add("branford", 3); // Add location with name="branford" and score=3 to the system.
tracker.get();              // The sorted locations, from best to worst, are: branford, bradford.
                            // Note that branford precedes bradford due to its higher score (3 > 2).
                            // This is the 1st time get() is called, so return the best location: "branford".
tracker.add("alps", 2);     // Add location with name="alps" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford.
                            // Note that alps precedes bradford even though they have the same score (2).
                            // This is because "alps" is lexicographically smaller than "bradford".
                            // Return the 2nd best location "alps", as it is the 2nd time get() is called.
tracker.add("orland", 2);   // Add location with name="orland" and score=2 to the system.
tracker.get();              // Sorted locations: branford, alps, bradford, orland.
                            // Return "bradford", as it is the 3rd time get() is called.
tracker.add("orlando", 3);  // Add location with name="orlando" and score=3 to the system.
tracker.get();              // Sorted locations: branford, orlando, alps, bradford, orland.
                            // Return "bradford".
tracker.add("alpine", 2);   // Add location with name="alpine" and score=2 to the system.
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "bradford".
tracker.get();              // Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                            // Return "orland".

# **USING A SORTED LIST**
The most basic approach to this problem would be to maintain a list and then whenever "add" is called, we push to this list and then after pushing, we Sort the list so that the items are always in sorted order.

Then, whenever "get" is called, since our list is always sorted, we can easily return the "ith" largest value so far.

The issue is that "At most 4 * 104 calls in total will be made to add and get." So, for each "add" call, since we are sorting the whole list, this is not an efficient approach. And so, for large test cases with a lot of "add" calls, we will get TLE.

But still, we need our items in a Sorted order. So, what if we have some sort of data structure that takes an item and automatically sorts it, without us having to do it manually. And it does that is an efficient manner.

Well, in Python, there is a third party library named "Sorted Containers" which provides us one such data structure named "SortedList". As the name suggests, this is a list that always maintains its order, no matter how many items we add or remove from it. And it has the worst case time complexity of O(LogN) for addition and deletion operations.

So, we can replace our normal list with a Sorted List and then our solution will be accepted.

But ofcourse, this question is asked in an interview, I don't think the interviewer will be happy with this approach since we are basically using a third party library that handles all the ordering automatically for us.

# **USING 2 HEAPS**
This one is a better approach for interview purpose.

It is not difficult to guess that we can use a Heap in this problem since this problem particularly talks about getting the "ith" largest element at any time which is something that a Heap is most commonly used for.

One way could be to have just one "Max Heap" which will order elements from maximum to minimum and then, whenever "get" is called, we will manually remove all the elements above the "ith" largest element, return the ith largest element, and then put back all the elements in the heap again. But, again, that will give TLE because just imagine a test case with a lot of "get" calls.

And so, a better approach is using two heaps. More precisely, one MaxHeap and one MinHeap.

I hope you have done problems where we return the "Kth" largest or "Kth" smallest elements in a list. And if you have, you know that if we want the "Kth" Largest element in a list, we can use a "Min Heap". We simply maintain the size of this heap to be at most "k" and if the size exceeds, we remove the elements from the top. So, at the end, we just have the "k" largest elements, with the one on the top of Min Heap being the "Kth" largest. 

And that's the same idea that we can use in this problem. It is just that "K" here is not fixed. It will change with each "get" call. This means, we cannot simply discard the elements from the top of Min Heap here once Min Heap size exceeds some certain size. Because in future, those elements might be the ones that we need to return in the get() call.

So, that's why we will use two heaps so that is the MinHeap size exceeds certain value, we will remove the extra elements from top of minHeap and put them in the second heap. 

And this second heap will be a Max Heap. Why?

Because, just think of this situation when minHeap has lets say "i" elements and this is the "ith" get() call. In that case, we will simply return the name of city on top of the MinHeap because it is currently the kth best city. Now, in the next call, it might not be the kth best. And one candidate for the next best city is the one on top of the Max Heap (if maxHeap is not empty). Because, since it is a maxHeap, the top city will be the best among all the cities in the maxHeap. And so, it is the best candidate to be the next best among all that we have traversed so far.

So, that's why, while in add() call we removed the extras from top of MinHeap and put them in maxHeap, in the get() call, we will take the top of maxHeap and put it back in the minHeap.

And that's the whole idea of using two Heaps in this problem.

Don't get confused by the "MinWrapper" and "MaxWrapper" classes. These are simply used here to override the logic to compare two elements when we put them in the Heap. Since, when two elements have same "score", we want to compare them based on their names.

You can check out this answer on stackoverflow - https://stackoverflow.com/a/59956131

Basically, we are overriding the logic for the "less than" comparison operator. 

For Min Heap, if we have data of two cities, we want the city with a lesser score to be above the city with a larger score. That's why, for the "MinWrapper", we returned "self.score < other.score" if scores are different. But, if scores are same, we then compare the names. Because, the city with a lexicographically smaller name will have more score than city with a lexicographically larger name as per the problem. But, since it is a minHeap, we always want the cities with a lower score on top and cities with a larger score on the bottom. That's why, in "MinWrapper", if the scores are same, we returned "self.name > other.name". 

And the opposite is done for "MaxWrapper" class.
