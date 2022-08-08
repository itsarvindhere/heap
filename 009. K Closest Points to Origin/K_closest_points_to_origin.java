import java.util.PriorityQueue;
import java.util.Scanner;

/*
    Given an array of points. points[i] = [xi, yi] and it represents a point on the X-Y plane. 

    Also given is an integer, k. 

    We need to return k closest points to the origin [0,0]

    NOTE - The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

    ------------------------------------------------------

    e.g. points = [[1,3], [-2,2]] and k = 1

    That means we need to return the closest point to origin. 

    1. For first point -> x1 = 1, y1 = 3
    2. For second point -> x1 = -2, y1 = 2

    And since we want to find distance from origin, x2 = 0, y2 = 0

    So, for the first point, 
            distance = √(1 - 0)2 + (3 - 0)2)
                     = √1 + 9
                     = √10
    Similarly, for the second point , 

            distance = √(-2 - 0)2 + (2 - 0)2)
                        = √4 + 4
                        = √8

    From these two distances, √8 is the smaller one. That means, point 2 is more closer to the origin than point 1. Hence, we return point 2 -> [-2,2]

    ------------------------------------------------------

    e.g. points = [[3,3],[5,-1],[-2,4]], k = 2

    Now we want two points closer to origin, not just one. 

    Again, we do the same thing.

    For point [3,3], distance from origin = √18
    For point [5,-1], distance from origin = √26
    For point [-2,4], distance from origin = √20

    Here, 2 closest points are [3,3] and [-2,4]
    
    ------------------------------------------------------

    So basically, we need to discard all the points that are further away from origin. i.e., for which the Euclidean distance is greater. Hence, we want a MaxHeap which has max distance on top and least on the bottom

    We can also avoid finding the Square root because since we are calculating distance from origin which is [0,0], in the end, the distance is simply x^2 + y^2. This will reduce the time taken by our program while computing bigger test cases. 

    ------------------------------------------------------

    e.g. points = [[3,3],[5,-1],[-2,4]], k = 2

    This time, we find distance without square root

    For point [3,3], distance from origin = 18
    For point [5,-1], distance from origin = 26
    For point [-2,4], distance from origin = 20

    Still, the closest points are the same. So, when comparing distance from origin, we can simply compare x^2 + y^2 for the two points and that's it.

    Here, 2 closest points are [3,3] and [-2,4]
    
    ------------------------------------------------------
 */


public class K_closest_points_to_origin {

    static int compare(int[] a, int[] b){
        double distance1 = (a[0] * a[0]) + (a[1] * a[1]);
        double distance2 = (b[0] * b[0]) + (b[1] * b[1]);
        
        return distance1 < distance2 ? 1 : -1;
    }

    static int[][] kClosest(int[][] points, int k) {
        //MaxHeap
        PriorityQueue<int[]> maxHeap = new PriorityQueue<>((a,b) -> compare(a,b));
        
        for(int i = 0; i < points.length; i++){
            maxHeap.add(points[i]);
            
            if(maxHeap.size() > k){
                maxHeap.remove();
            }
        }
        
        int[][] result = new int[k][2];
        int index = 0;
        
        while(maxHeap.size() > 0){
           result[index++] = maxHeap.remove();
        }
        
        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Enter the number of points in the points array");
    
        int n = sc.nextInt();
        
    
        int[][] points = new int[n][2];
    
        System.out.println("Enter the elements of the array");

        for(int i = 0; i < n; i++){
            for(int j = 0; j < 2; j++){
                points[i][j] = sc.nextInt();
            }
        }

        System.out.println("Enter the value of k");
        int k = sc.nextInt();

        System.out.println("*****************************");
        System.out.print("Array is:  ");
        for(int[] x : points){
            for(int y : x){
                System.out.print(y + "   ");
            }
            System.out.println();
        }
        System.out.println();
        System.out.println("k is : " + k);
        System.out.println("*****************************");

        int[][] resultArr = kClosest(points, k);

        System.out.println(k + " closest points to the Origin are -> ");
        for(int[] x : resultArr){
            for(int y : x){
                System.out.print(y + "   ");
            }
            System.out.println();
        }
        sc.close();
    }
}
