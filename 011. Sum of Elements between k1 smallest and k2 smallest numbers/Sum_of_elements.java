import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.Scanner;

/*
 
    Given an array and two integers k1 and k2. We have to find the sum of all the elements between k1th and k2th smallest elements of the array. 


    It is a variation of kth smallest element problem. There, we had only one value. Here we hae k1 and k2. And also it is given than K1 > K2. 

    That means, size of heap will be not more than K2. And since we want smallest elements, that means we want to remove all the bigger ones. Hence, we use maxHeap so that bigger elements are on top and they are removed. 


    Finally, since we do not include K1th or K2th element in our final Sum, we can simply set size of heap as K2 - 1 instead of K2 so that K2th element is not included in heap as well.

    And until size of heap becomes K1 i.e., heap has the k1th smallest element on top, we keep adding the elements by removing them from top of heap.



*/


public class Sum_of_elements {

    public static long sumBetweenTwoKth(long A[], long N, long K1, long K2)
    {
        PriorityQueue<Long> maxHeap = new PriorityQueue<Long>(Comparator.reverseOrder());
        long sum = 0;
        
        for(int i = 0; i < N; i++){
            maxHeap.add(A[i]);
            
            // Since we don't include the K2th element itself in the sum so we can simply set heap size as (K2 - 1) so that we can start fetching the top element directly and adding it to sum variable
            if(maxHeap.size() > (K2 - 1)){
                maxHeap.remove();
            }
        }
        
        // Since K1 will always be smaller than K2, that means unless the size of Heap becomes K1, keep removing the elements from the top and add to the sum. In the end, we will have sum of all the elements between K1th and K2th smallest elements
        while(maxHeap.size() > K1){
            sum += maxHeap.remove();
        }
        
        return sum;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

            System.out.println("Enter the number of elements in the array");
        
            int n = sc.nextInt();
        
            long[] arr = new long[n];
        
            System.out.println("Enter the elements of the array");
    
            for(int i = 0; i < n; i++){
                arr[i] = sc.nextLong();
            }
    

            System.out.println("Enter the value of k1");
    
            long k1 = sc.nextLong();

            System.out.println("Enter the value of k2");
    
            long k2 = sc.nextLong();
    
            System.out.println("*****************************");
            System.out.print("Array is:  ");
            for(int i = 0; i < n; i++){
                System.out.print(arr[i] + " ");
            }
            System.out.println();
            System.out.println("K1 is:  " + k1);
            System.out.println("K2 is:  " + k2);

            System.out.println("*****************************");
    
            long result = sumBetweenTwoKth(arr, n, k1, k2 );
    
            System.out.println("Sum of Elements between k1th and k2th smallest element is -> " + result);

            sc.close();
    }
}
