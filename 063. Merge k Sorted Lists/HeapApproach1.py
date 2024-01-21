def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        # A Min Heap to order the nodes by their values from smallest to largest
        minHeap = []
        
        # Go over each linked list
        for lst in lists:
            
            # Take each node and put its value in the minHeap
            while lst:
                heappush(minHeap, lst.val)
                lst = lst.next
                
        # Dummy Node
        dummy = ListNode()
        
        # Pointer to the dummy node
        pointer = dummy
        
        # While the minHeap is not empty
        while minHeap:
            
            # New Node
            newNode = ListNode()
            newNode.val = heappop(minHeap)
            
            # Point to this new node
            pointer.next = newNode
            
            # Update the pointer
            pointer = pointer.next

        # Return the output list
        return dummy.next