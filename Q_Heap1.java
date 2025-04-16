// This question is designed to help you get a better understanding of basic heap operations.

// There are  types of query:

// " " - Add an element  to the heap.
// " " - Delete the element  from the heap.
// "" - Print the minimum of all the elements in the heap.
// NOTE: It is guaranteed that the element to be deleted will be there in the heap. Also, at any instant, only distinct elements will be in the heap.
public class Solution {

    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        TreeMap<Integer,Integer> arr=new TreeMap<>();
        for(int i=0;i<n;i++){
            int op=sc.nextInt();
            if(op==1){
                int a=sc.nextInt();
                arr.put(a, arr.getOrDefault(a, 0)+1);
            }
            else if(op==2){
                int element=sc.nextInt();
                if(arr.get(element)>1){
                    arr.put(element,arr.get(element)-1);
                } 
                else{
                    arr.remove(element);
                }
            }
            else {
                System.out.println(arr.firstKey());
            }
        } 
    }
}