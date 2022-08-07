

import java.util.PriorityQueue;
import java.util.Scanner;

/*
 *  Since we want to find 'kth' 'largest' element, we have to use MinHeap here.
 *  In Java, we can have a minHeap using a PriorityQueue.
 */

public class Kth_largest_element {
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

        System.out.print("kth largest element is: " + kthLargest(arr, k));

        sc.close();
    }
}
