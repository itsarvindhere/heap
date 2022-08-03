

import java.util.PriorityQueue;

/*
 *  Since we want to find 'kth' 'largest' element, we have to use MinHeap here.
 *  In Java, we can have a minHeap using a PriorityQueue.
 */

public class kth_largest_element {
    public static int kthLargest(int[] arr, int k) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for(int i = 0; i < arr.length; i++){
            minHeap.add(arr[i]);
            if(minHeap.size() > k){
                minHeap.remove();
            }
        }

        return minHeap.peek();
    }
    public static void main(String[] args) {
        int[] arr  = {7, 10, 4, 3, 20, 15};
        System.out.print("kth largest element is: " + kthLargest(arr, 3));
    }
}
