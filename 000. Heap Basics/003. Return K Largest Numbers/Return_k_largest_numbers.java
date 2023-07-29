import java.util.PriorityQueue;
import java.util.Scanner;

/**
 * We are given an array and we have to return another array which 
 * has k largest numbers in it
 * e.g. arr = [7, 10, 4, 3, 20, 15] and k = 3
 * SO, returned arr = [20, 15, 10] <- 3 largest elements in array
 */

public class Return_k_largest_numbers {

    public static int[] kLargestElements(int[] arr, int k) {
        PriorityQueue<Integer> minHeap  = new PriorityQueue<Integer>();

        for(int i = 0; i < arr.length; i++){
            minHeap.add(arr[i]);

            if(minHeap.size() > k){
                minHeap.remove();
            }
        }

        int[] result = new int[k];
        int i = 0;

        while(minHeap.size() > 0){
            result[i++] = minHeap.remove();
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

        int[] resultArr = kLargestElements(arr,k);

        System.out.println("k largest elements are : ");
        for(int i = 0; i < resultArr.length; i++){
            System.out.print(resultArr[i] + " ");
        }

        sc.close();
    }
}
