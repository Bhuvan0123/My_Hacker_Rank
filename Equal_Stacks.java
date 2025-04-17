// You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

// Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.
public static int equalStacks(List<Integer> h1, List<Integer> h2, List<Integer> h3) {
    int s1=h1.stream().mapToInt(x->x.intValue()).sum();
    int s2=h2.stream().mapToInt(x->x.intValue()).sum();
    int s3=h3.stream().mapToInt(x->x.intValue()).sum();
    while(s1!=s2 || s2!=s3){
        if(s1>s2 || s1>s3){
            s1-=h1.remove(0);
        }
        if(s2>s1 || s2>s3){
            s2-=h2.remove(0);
        }
        if(s3>s1 || s3>s2){
            s3-=h3.remove(0);
        }
    }
    return s1;
}