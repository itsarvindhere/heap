import java.util.PriorityQueue;
import java.util.Scanner;

/* 
    There are given N ropes of different lengths, we need to connect these ropes into one rope. 

    The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.

    e.g. arr = [1,2,3,4,5]

    Here, we have 5 ropes and we have to connect the ropes in such a way that the cost is minimum.


    e.g. if we connect ropes of length 4 and length 5, we will have a rope of length 9. So, the cost to connect ropes of length 4 and length 5 is 9.  

    So now, we have four ropes left -> 1, 2, 3, 9
    cost so far = 9

    If we connect rope of length 9 to length 2, we get a new rope of length = 11. Cost to connect these two ropes is also 11. 

    So cost so far = 9 + 11 => 20

    So, now we have three ropes -> 1, 3, 11

    Let's say we now connect ropes 11 and 3

    So cost to connect these two ropes = 14
    And so, this cost is added to the cost so far => 20 + 14 => 34

    Finally, we have two ropes left => 1 and 34

    We connect both and finally we get a rope of length 35.

    Cost to connect these two = 35

    So Final cost = prev cost + 35 => 34 + 35 => 69

    -------------------------------------------------------

    Now, there can be multiple ways to connect ropes so we want to minimize this final cost.
    
    If we observer, if we connect two ropes of large lengths, the cost will also be large. So if we start from the bigger ropes initially, our cost finally will be more. 


    e.g. in above example, let us start from the smaller lengths.

    arr = [1,2,3,4,5]

    1. Connect 1 and 2 -> new Rope of length 3 is formed. Cost = 3
    2. Connect 3 and 3 -> new Rope of length 6 is formed. Cost = 6
    3. Connect 4 and 5 (since 6 is bigger than both) -> new Rope of length 9 is formed. Cost = 9
    4. Finally, connect 6 and 9 -> new Rope of length 15 is formed. Cost = 15.

    Total cost = 3 + 6 + 9 + 15 => 33

    As we can see, 33 is much lesser than 69. 

    And this is the minimum cost to connect ropes.

    Hence our strategy will be to connect the smaller sized ropes first. So at any time, the two ropes that we take to connect should be the smallest.

    So that means, we want k smallest lengths at any time. Where k = 2.  SInce at any time we want two minimum numbers, that means, we want a Minheap because then we can combine the two topmost lengths and they will always be the smallest lengths at any time.

    First, we will put all the lengths in the heap. That ensures that we have minimum at top and max at bottom.

    Then, we keep adding topmost two lengths by removing them from heap and putting back their sum. We also add this sum to existing cost.

    We do this until our heap has only one length left i.e., the final rope length. 
 */



public class Minimum_cost_to_connect_ropes {

    static int minimumCost(int[] arr) {
        int cost = 0;
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();

        for (int length : arr) {
            minHeap.add(length);
        }

        while(minHeap.size() > 1){
            // Remove the two smallest lengths at any time
            int l1 = minHeap.remove();
            int l2 = minHeap.remove();

            // Add the length of new rope formed by combination of the above two lengths to the heap
            minHeap.add(l1 + l2);

            // Add the cost to the existing cost
            cost += l1 + l2;
        }

        return cost;
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
    
            int result = minimumCost(arr);
    
            System.out.println("Minimum Cost to Connect Ropes is -> " + result);

            sc.close();
    }
}
