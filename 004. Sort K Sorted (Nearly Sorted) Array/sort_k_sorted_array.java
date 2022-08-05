import java.util.PriorityQueue;
import java.util.Scanner;

/* PROBLEM STATEMENT

  We are given a 'k' sorted array or 'nearly' sorted array
  We have to sort this nearly sorted array.
  'k' sorted array means that any value in the array can be up to k distance from its expected position.
  e.g. arr = [6,5,3,2,8,10,9], k = 3
  
  If we sort it, it becomes = [2,3,5,6,8,9,10]
  As we can see, 6 is at index = 0 in unsorted array and at index 3 in sorted array. So, its actual position is k distance away from its current position.
  
  Same with other elements. They will also be <= 3 distance away from their actual position (k distance on left side or k distance on right side)
  
  e.g. take 2. Current position in arr = index 3
  Actual position in the sorted array = index = 0
  k = 3 - 0 = 3 which is <= 3
  
  take 5. Current position in arr = index 1
  actual position in sorted arr = index 2
  Difference in positions = 1 which is <= 3
  
  So, this is a nearly sorted array or a k sorted array where k = 3
  We can obviously use a sorting algorithm like merge sort to sort this array in nlogn complexity. But in the problem, since we are given 'k', that means we can do even better. We can sort in nlogk using heap. 
 */


/*
    How to use Heap to solve this problem

    We are given k so we can make use of this value.

    arr = [6,5,3,2,8,10,9]

    Lets take index = 0.

    WE know that the element that should be at index = 0 can be found up to a distance = k from current index = 0. 

    i.e., it can be either 
        index = 0 + 1 = index 1 = 5
        index = 0 + 2 = index 2 = 3
        index = 0 + 3 = index 3 = 2
    
        It cannot be any element after index = 3 because all the other elements lie outside distance = 3 from index 0. 

        Hence, at one time, we are only considering k elements (3 elements)

        And this is something we can use in a heap. size of heap = 3.

        Now, we need to decide what type of heap we need here. Minheap or maxheap??

        If we see, what we are doing with 4 elements is that we want the smallest to come at the top because we know taht from a heap we can only get the topmost element at a time. That means, we need a MinHeap which has the smallest element on top. 

        arr = [6,5,3,2,8,10,9], k = 3

        Push 6 to heap, size = 1 <= k
                        |     |
                        |     |
                        |     |
                        |__6__| <- top
      
        Push 5 to heap, size = 2 <= k
                        |     |
                        |     |
                        |  5  | <- top
                        |__6__| 

        Push 3 to heap, size = 3 <= k
                        |     |
                        |  3  | <- top
                        |  5  | 
                        |__6__| 

        Push 2 to heap

                        |  2  | <- top
                        |  3  | 
                        |  5  | 
                        |__6__| 
        
        Here, size > k. Which means we need to pop the top most element now. So, pop 2 and push it in some result array. 
        Result arr = [2]

        Push 8 to heap

                        |  3  | <- top
                        |  5  | 
                        |  6  | 
                        |__8__| 

        Again, the size of heap exceeded k = 3 so pop the topmost element = 3. Result arr = [2,3]

        Push 10 to the heap

                        |  5  | <- top
                        |  6  | 
                        |  8  | 
                        |__10_| 
        Pop the top element since size > k. Pop 5 and push it to result arr. Result arr = [2,3,5]


        Push 9 to the heap

                        |  6  | <- top
                        |  8  | 
                        |  9  | 
                        |__10_| 

        Pop top element since size > k. Pop 6 and push to result arr. Result arr = [2,3,5,6]

        And finally, our loop ends because we have pushed the last element in the array to heap. So now, all we do is keep popping the element from heap and push to the array since the elements are already in sorted order top to bottom as this is a minheap so smallest element is always at top.

        Finally, result arr = [2,3,5,6,8,9,10] = SORTED!!

 */



 public class sort_k_sorted_array {

    public static int[] kSortedArray(int[] arr, int k) {
      PriorityQueue<Integer> minHeap = new PriorityQueue<>();
      int[] result = new int[arr.length];
      int index = 0;

      for(int i = 0; i < arr.length; i++){
        minHeap.add(arr[i]);
        if(minHeap.size() > k){
          result[index++] = minHeap.remove();
        }
      }

      while(minHeap.size() > 0){
        result[index++] = minHeap.remove();
      }

      return result;

    }
    public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of elements in the array");

        int n = sc.nextInt();

        int[] arr = new int[n];

        System.out.println("Enter the elements of the array");

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }

        System.out.println("Enter the value of k");

        int k = sc.nextInt();

        System.out.println("*****************************");
        System.out.print("Array is:  ");
        for(int i = 0; i < n; i++){
            System.out.print(arr[i] + " ");
        }

        System.out.println("");
        System.out.print("k is:  ");
        System.out.println(k);

        System.out.println("*****************************");

        int[] resultArr = kSortedArray(arr,k);

        System.out.println("k sorted array after Sorting is : ");
        for(int i = 0; i < resultArr.length; i++){
            System.out.print(resultArr[i] + " ");
        }

        sc.close();
    }
    
 }