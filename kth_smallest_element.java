
import java.util.Comparator;
import java.util.PriorityQueue;

/**
 * Given an array, find the kth smallest element from this array
 * Since we have to find 'kth' 'smallest', we use MaxHeap to find. In java, we can create a MaxHeap using a PriorityQueue and Comparator.reverseOrder()
 */

public class kth_smallest_element {

    public static int kthSmallest(int[] arr, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());

        for(int i = 0; i < arr.length; i++){
            maxHeap.add(arr[i]);
            if(maxHeap.size() > k){
                maxHeap.remove();
            }
        }

        return maxHeap.peek();
    }
    public static void main(String[] args) {
        int[] arr  = {7, 10, 4, 3, 20, 15};
        System.out.print("kth smallest element is: " + kthSmallest(arr, 3));
    }
}