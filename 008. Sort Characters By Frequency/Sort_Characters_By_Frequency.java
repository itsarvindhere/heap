import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Scanner;

/*
 Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

 Return the sorted string. If there are multiple answers, return any of them.

 Since it is given to sort in decreasing order, it means top should have max frequency character in string. That means, we need to use MaxHeap here. 
  
 */


public class Sort_Characters_By_Frequency {

    static String frequencySort(String s) {
        String result = "";

        HashMap<Character, Integer> freq = new HashMap<>();
    
        for(int i = 0; i < s.length(); i++){
            freq.put(s.charAt(i), freq.getOrDefault(s.charAt(i), 0) + 1);
        }
        
        PriorityQueue<Character> maxHeap = new PriorityQueue<>((a,b) ->  freq.get(b) - freq.get(a));

        freq.forEach((key,value) -> maxHeap.add(key));

        while(maxHeap.size() > 0) {
            Character c = maxHeap.remove();
            result += new String(new char[freq.get(c)]).replace('\0', c);
        }

        return result;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

            System.out.println("Enter the String");
        
            String s = sc.nextLine();  
            String frequencySortedString = frequencySort(s);
    
            System.out.println("String sorted based on frequency (decreasing order) -> " + frequencySortedString);

            sc.close();
    }
}
