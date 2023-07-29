import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Scanner;

/*

    Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

    Here again, we first find frequency of elements using a Hashmap and then use a minheap since we want the elements in increasing order of frequencies. That means, minimum frequency element first. So, top of heap should have least frequency and bottom should have max frequency element.
 
 */


 public class Frequency_Sort {

    static int[] frequencySort(int[] nums) {
        int[] result = new int[nums.length];

        HashMap<Integer, Integer> freq = new HashMap<>();

        for(int element: nums){
            freq.put(element, freq.getOrDefault(element, 0) + 1);
        }
        
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b) -> {
            
            int freq1 = freq.get(a);
            int freq2 = freq.get(b);
            
            if(freq1 == freq2){
                return b - a; //If frequency is same, give the bigger number priority i.e., sort those numbers in decreasing order
            }
            
            return freq1 - freq2;
        
        });

        for(int element: nums){
            minHeap.add(element);
        }

        for(int i = 0; i < nums.length; i++){
            result[i] = minHeap.remove();
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
    
            System.out.println("*****************************");
            System.out.print("Array is:  ");
            for(int i = 0; i < n; i++){
                System.out.print(arr[i] + " ");
            }
            System.out.println("*****************************");
    
            int[] resultArr = frequencySort(arr);
    
            System.out.println("Elements Sorted based on frequency -> ");
            for(int i = 0; i < resultArr.length; i++){
                System.out.print(resultArr[i] + " ");
            }
            sc.close();
    }
}