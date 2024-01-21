# PROBLEM STATEMENT

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

# EXAMPLE

    Input: lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]

    Explanation: The linked-lists are:
        [
        1->4->5,
        1->3->4,
        2->6
        ]

    merging them into one sorted list:
    1->1->2->3->4->4->5->6

# **1. THE EASY WAY - NOT THE BEST FOR INTERVIEWS**

This approach, I think, is pretty easy to come up with.

Basically, we will put every node's value in a minHeap so that it ordered them all from smallest to largest.

Then, we will create a new linked list out of the values in the minHeap and return that.

# **2. THE BETTER WAY**
If you think about it, what exactly we are doing in the above approach is that for every single node in every single linked list, we are creating a new node and then attaching it to the output list. This is not the most space efficient way to solve this problem.

What if we can simply reuse the nodes in the input linked lists instead of having to create new ones?

Well, for that, you might think that we can simply push the node's value and also the node itself in the minHeap because as we know, in Python, if a tuple is pushed in a minHeap, the minHeap will automatically order the elements based on the first value of the tuple.

So, we might try doing something like - 
	
		heappush(minheap, (lst.val, lst))
		
But, as you will see, this will not work. This will throw an error which says - 

	TypeError: '<' not supported between instances of 'ListNode' and 'ListNode'
	
As this error message suggests, there is no way to compare two instances of the ListNode class. So, Python cannot understand how to tell which instance to be placed first in the minHeap and which one to place later.

The solution is that we have to manually define the logic for the less than "<" operator for the ListNode class. And we can do that by doing - 

	ListNode.__lt__ = lambda self, other: self.val < other.val
	
Here, we are saying that if a less than operator is used between two instances of a "ListNode" class, then compare then based on their values.

And now, we can write the following line without any error - 

		heappush(minheap, (lst.val, lst))
		
Now, the minHeap has all the nodes ordered by their values.  So, all that's left is now to construct the final linked list using these values. 

So, everything seems to be working fine, right?

Well, there is one issue.

For some test cases, when we construct the final Linked List, we will get the error saying "Error - Found cycle in the ListNode".

For example, if we have a test case as - [[-2,-2],[-3]]

	Let's say we simply do heappush(minheap, (lst.val, lst))
	
	For simplicity, lets call the first node with value -2 as node "A"
	Let's call the second node with value -2 as node "B"
	and the third node with value -3 as node "C"
	
	So, we start with the first linked list [-2,-2]
	
	First, we push the node "A" to the minHeap which has value -2 and next node is "B"
	Then, we push the node "B" to the minHeap which has a value -2 and next node is "Null"
	Finally, we push the node "C" in the minHeap which has a value -3 and next node is "Null"

So far, it is fine. There is no error so far.

Now, we start constructing the final linked list. 

we take a dummy node. And we take a pointer that points to this dummy node initially.

So the top of minHeap has the node "C" since it has the lowest value -3.

So, we attach the node -3 with this dummy node. Now, pointer points to this node with value -3.

Next, we have the node "B" with value -2 and next node as "Null".

So, we attach this node to node that pointer points to. And now, pointer is updated to point to this node "A".

Finally, we have the node "A" with value -2 and next node as node "B".

Note that right now, the pointer points to the Node "B" which we just attached. And now, to this, we are attaching the node "A" which in turn has node "B" as its next node.

What does that mean? It means, we have a cycle here as -

	node C -> node B -> node A -> node B

Ideally, it should be 

	node C -> node B -> Node A -> Null
	
So, what can we do? Well, the simplest way to solve this issue is to make sure that before we attach a node to the final linked list, we make sure that it doesn't have any node after it. In other words, we attach a node to a linked list by separating it from its linked list. 

For that, before we attach it to the linked list, we will set its "next" pointer's value as Null (None in Python).

And well, that's the whole logic.

