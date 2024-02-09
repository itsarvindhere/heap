class DinnerPlates:

    def __init__(self, capacity: int):
        
        # A list with each index having a stack
        self.stacks = []
        
        # Capacity
        self.capacity = capacity
    
        # When we "push", we need to get the leftstack stack with size < capacity
        # In Brute Force Approach, we have to loop over the entire list of stacks to get that
        # Instead, we can use a Min Heap to order the non-full stacks by their indices from left to right
        # So that at any time, we can pick the leftmost stack quickly
        self.leftmostStacks = []
        

    def push(self, val: int) -> None:
        
        # Push the "val" in leftmost stack with size < capacity
        # Remove all the stacks on top of the "leftmostStacks" heap that are invalid
        while self.leftmostStacks and self.leftmostStacks[0] >= len(self.stacks): heappop(self.leftmostStacks)

        # If there is no leftmost stack with size < capacity
        if not self.leftmostStacks:
            
            # Add a new stack and put the value in that stack
            newStack = [val]
            self.stacks.append(newStack)
            
            # If the stack has less elements than capacity, then add its index to the leftmostStack heap
            if self.capacity > 1: heappush(self.leftmostStacks, len(self.stacks) - 1)
            
        # Otherwise, push the value into the leftmost stack with size < capacity
        else: 
            idx = self.leftmostStacks[0]
            self.stacks[idx].append(val)
            
            # If after pushing, the stack becomes full, remove it from the heap
            if len(self.stacks[idx]) == self.capacity: heappop(self.leftmostStacks)
                
        
    def pop(self) -> int:
        
        # Remove all the stacks on right side that are empty
        while self.stacks and not self.stacks[-1]: self.stacks.pop()
        
        # If there are no stacks, return -1
        if not self.stacks: return -1
        
        # Otherwise, return the value on top of the rightmost non empty stack
        val = self.stacks[-1].pop()
        
        # If the rightmost non empty stack is empty, pop it as well
        if not self.stacks[-1]: self.stacks.pop()
            
        # Otherwise, if its capacity is "max capacity - 1", then it is a new candidate for leftmost stack
        # Hence, push it into the heap
        elif len(self.stacks[-1]) == self.capacity - 1: heappush(self.leftmostStacks, len(self.stacks) - 1)

        # Return the value
        return val
        
    def popAtStack(self, index: int) -> int:
        
        # If the stack at "index" does not exist
        # Or, it is empty
        # Return -1
        if index > len(self.stacks) or not self.stacks[index]: return -1
        
        # Otherwise, Remove the value from the stacks at "index"
        val = self.stacks[index].pop()
        
        # Put this stack in the heap if it has (capacity - 1) elements
        if len(self.stacks[index]) == self.capacity - 1: heappush(self.leftmostStacks, index)
        
        # Return the value
        return val