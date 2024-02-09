class DinnerPlates:

    def __init__(self, capacity: int):
        
        # A list with each index having a stack
        self.stacks = []
        
        # Capacity
        self.capacity = capacity
        

    def push(self, val: int) -> None:
        
        # Push the "val" in leftmost stack with size < capacity
        
        # Index of leftmost stack with size < capacity
        leftmostStackIndex = -1
        for i in range(len(self.stacks)):
            if len(self.stacks[i]) < self.capacity: 
                leftmostStackIndex = i
                break

        # If there are no stacks or there is no leftmost stack with size < capacity
        if not self.stacks or leftmostStackIndex == -1:
            
            # Add a new stack and put the value in that stack
            newStack = [val]
            self.stacks.append(newStack)
            
        # Otherwise, push the value into the leftmost stack with size < capacity
        else: self.stacks[leftmostStackIndex].append(val)

    def pop(self) -> int:
        
        # Remove all the stacks on right side that are empty
        while self.stacks and not self.stacks[-1]: self.stacks.pop()
        
        # If there are no stacks, return -1
        if not self.stacks: return -1
        
        # Otherwise, return the value on top of the rightmost non empty stack
        val = self.stacks[-1].pop()
        
        # If the rightmost non empty stack is empty, pop it as well
        if not self.stacks[-1]: self.stacks.pop()

        # Return the value
        return val
        
    def popAtStack(self, index: int) -> int:
        
        # If the stack at "index" does not exist
        # Or, it is empty
        # Return -1
        if index > len(self.stacks) or not self.stacks[index]: return -1
        
        # Otherwise, Remove the value from the stacks at "index"
        val = self.stacks[index].pop()
        
        # Return the value
        return val