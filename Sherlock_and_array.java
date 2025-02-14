# Watson gives Sherlock an array of integers. His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.
public static String balancedSums(List<Integer> arr) {
        int n=arr.size();
        int sum=0;
        for(int i=0;i<n;i++){
            sum+=arr.get(i);
        }
        int left=0;
        for(int i=0;i<n;i++){
            int right=sum-left-arr.get(i);
            if(right==left){
                return "YES";
            }
            left+=arr.get(i);
        }
        return "NO";

    }