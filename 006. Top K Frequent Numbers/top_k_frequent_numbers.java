import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Scanner;

/*
 
    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    e.g. nums = [1,1,1,2,2,3], k = 2

    We need to output two most frequent appearing numbers in this array. As we can see, those are [1,2] so the solution for this case if [1,2]

    nums = [1], k = 1

    So result = [1]

    In the K Closest Numbers, we put numbers in heap based on their absolute difference. Here, we need to put numbers in the heap based on their frequency. 

    We want elements with max frequencies. That means, we need to discard elements with least frequencies. Hence, we will use a MinHeap for this because in MinHeap, minimum stays at top and Max at the bottom.

    When it comes to frequencies, one thing that comes to mind is a Map because using a map, we can set key value pairs where key is the element and value is its frequency in the array.

    e.g. [1,1,1,3,4,2,2]

    Its map will be like 

    1 -> 3
    3 -> 1
    4 -> 1
    2 -> 2


    So now, all that we need to do is in our minHeap, we need to put the keys of this map and they will be ordered based on their frequency.
*/


public class top_k_frequent_numbers {

    static int[] topKFrequentNumbers(int[] arr, int k) {
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int element : arr) {
            if(freq.get(element) == null){
                freq.put(element, 1);
            } else{
                int prev = freq.get(element);
                freq.put(element, prev + 1);
            }
        }

        // minheap with elements ordered based on their frequency with min frequency on top and max on bottom
        PriorityQueue<Integer> minHeap = new PriorityQueue<>((a,b) -> freq.get(a) - freq.get(b));

        freq.forEach((key,value) -> {
            minHeap.add(key);
            if(minHeap.size() > k) {
                minHeap.remove();
            }
        });

        int[] result = new int[k];
        int index = k - 1;

        while(minHeap.size() > 0){
            result[index--] = minHeap.remove();
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
    
            System.out.println();
            System.out.print("k is:  ");
            System.out.println(k);
            System.out.println("*****************************");
    
            int[] resultArr = topKFrequentNumbers(arr,k);
    
            System.out.println("Top " + k + " most frequent elements in the array are: ");
            for(int i = 0; i < resultArr.length; i++){
                System.out.print(resultArr[i] + " ");
            }
            sc.close();
    }
}
