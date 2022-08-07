import java.util.PriorityQueue;
import java.util.Scanner;

/*
  
  Given an array e.g. [5,6,7,8,9]
  Also given is a Value X. e.g. X = 7
  And finally, value K is also given. e.g. K = 3

  We have to find K closest elements to X in the array.

  In other words, we have to find 3 numbers from above array that are closest to 7. e.g., in the above array, the 3 numbers closest to 7 are -> [6,7,8]

  How can we solve this? 

  One way is to find absolute difference of every element with the given element X. e.g. if we substract each element with X = 7

  arr                 = [5,6,7,8,9]
  absolute difference = [2,1,0,1,2]

  And now, we know that the less the differnce  = the closest the element to X

  If we sort this absolute difference -> [0,1,1,2,2]
   arr                                -> [7,6,8,5,9]

  so, from this we can see that [7,6,8] are the closest 3 numbers to 7 because they have the least absolute difference.
  
  Hence, we are sorting elements based on their absolute difference with the element X. <-  THIS IS IMPORTANT TO CONSIDER!!

  So in the heap, we have to place items based on their absolute difference, not based on the number itself.
  
  WHICH HEAP WILL BE USED HERE??

  What we want is discard all the elements for which absolute difference is high and keep only those for which absolute difference is the least. That means, least absolute different at the bottom and high at top of heap. That means we have to use a Max Heap for this problem.
  
  So, the comparator for the PriorityQueue will compare elements based on their absolute differences.

  There may be problems on Leetcode of GFG where it is also said that do not include the element X itself if that is in the array too. In that case, before putting the element into heap also check if element != X. 

  Also, it might be said that if the absolute difference is same for two elements, give the priority to the greatest element / smallest element of the two. Make changes to comparator method accordingly.
 
 */

public class K_closest_elements {

        public static int compare(int a, int b, int x) {
            int abs1 = Math.abs(b - x);
            int abs2 = Math.abs(a - x);

            // If two elements have same absolute difference
            if(abs1 == abs2){
                
                return b - a;     // <-   if question says return smaller number if same absolute difference
                // return a - b;     <-  if question says return bigger number if same absolute difference

            }
            
            return abs1 - abs2;
        }
        
        public static int[] kClosestElements(int[] arr, int k, int x) {
            PriorityQueue<Integer> maxHeap = new PriorityQueue<>((a,b) -> compare(a,b,x));
            int[] result = new int[k];

            for(int i = 0; i < arr.length; i++){
                maxHeap.add(arr[i]);
                if(maxHeap.size() > k){
                    maxHeap.remove();
                }
            }

            int index = 0; //We can also take this index = k - 1 if we want to output numbers in reverse order
            while(maxHeap.size() > 0){
                result[index++] = maxHeap.remove();  //If we have to output in reverse order, here we need to do result[index--] = maxHeap.remove(); 
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

            System.out.println("Enter the value of x");
    
            int x = sc.nextInt();
    
            System.out.println("*****************************");
            System.out.print("Array is:  ");
            for(int i = 0; i < n; i++){
                System.out.print(arr[i] + " ");
            }
    
            System.out.println();
            System.out.print("k is:  ");
            System.out.println(k);

            System.out.println();
            System.out.print("x is:  ");
            System.out.println(x);
    
            System.out.println("*****************************");
    
            int[] resultArr = kClosestElements(arr,k,x);
    
            System.out.println(k + " closest elements to " + x + " in the array are: ");
            for(int i = 0; i < resultArr.length; i++){
                System.out.print(resultArr[i] + " ");
            }
    
            sc.close();

        }
}
