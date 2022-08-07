
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * Given an array, find the kth smallest element from this array
 * Since we have to find 'kth' 'smallest', we use MaxHeap to find. In java, we can create a MaxHeap using a PriorityQueue and Comparator.reverseOrder()
 */

public class Kth_smallest_element {

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

        System.out.print("kth smallest element is: " + kthSmallest(arr, k));

        sc.close();
    }
}
