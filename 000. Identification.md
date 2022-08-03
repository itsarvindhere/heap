-> How to identify if a problem requires the use of heap?

Just look for two keywords in the problem -
    1. k
    2. 'Smallest' or 'Largest'

If a problem has these two keywords, that question can be solved using a heap!

-> Which HEAP to choose for a problem??

There are two types of heaps -> Min Heap and Max Heap

    MaxHeap -> Maximum element on top of heap
    MinHeap -> Minimum element on top of heap

    1. Problem includes 'k' & 'Smallest' = MaxHeap
    2. Problem includes 'k' & 'Largest' = MinHeap

-> How using heap reduces complexity of a solution

Normally, heap related problems are sorting problems. e.g.

Given an array and find kth element etc etc...

So one way can be to sort the array and then find the element -> nlogn
If we use heap of size k, then the complexity becomes -> nlogk



----------------------------EXAMPLE------------------------

Suppose we want to find the kth smallest element in an array.

        arr = [7, 10, 4, 3, 20, 15]
        k = 3

Here, we want to find 3rd smallest element. 

Can we use heap in this problem? Yes we can. Because it includes the keywords 'k' and 'smallest'. So we can use a MaxHeap to solve it.

One way is to sort this array - [3,4,7,10,15,20] and then find the third smallest which is 7. So complexity is nlogn

To improve the complexity even better, we can use MaxHeap. Because in sorting, we only want 3rd smallest. After that number, it is just extra work to sort the rest of numbers.

---------------------- USING MAXHEAP ------------------

WE use MaxHeap so taht we can remove all the bigger elements from consideration.

        arr = [7, 10, 4, 3, 20, 15]
        k = 3

MaxHeap = 

         Push 7 to heap
            |     |
            |     |
            |     |
            |__7__| <- top
        
        Next we have 10. Since 10 > 7, 10 will be the new top
            |     |
            |     |
            |  10 | <- top
            |__7__|
        Next we have 4. Since 4 is less than 10 it will sit below 10. ALso 4 is less than 7 so it sits below 7

            |     |
            |  10 | <- top
            |  7  |
            |__4__|
        Next we have 3. Again, since 3 is less than 10, 7 and 4. It will sit at the bottom. 

            |  10 | <- top
            |  7  | 
            |  4  |
            |__3__|
    Here, our maxHeap size exceeds k = 3. Size is now 4. This means that the element at the top of heap will never qualify for the kth smallest. It will never come in the first k smallest elements in array. So we can reject it safely. Hence, we pop 10. 

            |     |
            |  7  | <- top
            |  4  |
            |__3__| 

    Next we have 20

            | 20  | <- top
            |  7  | 
            |  4  |
            |__3__| 

    Similar to 10, 20 also does not qualify because size of heap > k now, so we pop() 20.

            |     |
            |  7  | <- top
            |  4  |
            |__3__|
    
    Finally, we push 15. 

            |  15 | <- top
            |  7  | 
            |  4  |
            |__3__|

    Since size of heap is again > k, the top most element is popped. So 15 is popped. And our array ends. 

    At the end, our heap looks like - 

            |     |
            |  7  |  <- top
            |  4  |
            |__3__|

And the kth smallest element is the top element in this heap = 7. This is the required answer.

Hence, using a MaxHeap, the complexity becomes nlogk. 
        
         







