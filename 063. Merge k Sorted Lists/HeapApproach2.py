def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # Defining the less than comparator's logic for the ListNode class
        # This is done so that we can directly push a linked list int a Heap
        ListNode.__lt__ = lambda self, other: self.val < other.val

        # A Min Heap to order the nodes by their values from smallest to largest
        minHeap = []
        
        # Go over each linked list
        for lst in lists:
            
            # Put each linked list in the minHeap
            # Since the test case can have empty linked lists as well, skip them
            while lst: 
                
                # Push the current node in the minHeap
                heappush(minHeap, (lst.val, lst))
                
                # Move to the node afer the "lst" node
                lst = lst.next
                
        # Dummy Node
        dummy = ListNode()
        
        # Pointer to the dummy node
        pointer = dummy
        
        # While the minHeap is not empty
        while minHeap:
            
            # The node on top of the minHeap
            top = heappop(minHeap)[1]
            
            # Make sure it has no node after it
            top.next = None
            
            # Point the pointer to the node on top of the minHeap
            pointer.next = top
            
            # Update the pointer
            pointer = pointer.next

        # Return the output list
        return dummy.next