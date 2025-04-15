# Jesse loves cookies and wants the sweetness of some cookies to be greater than value . To do this, two cookies with the least sweetness are repeatedly mixed. This creates a special combined cookie with:

# sweetness  Least sweet cookie   2nd least sweet cookie).

# This occurs until all the cookies have a sweetness .

# Given the sweetness of a number of cookies, determine the minimum number of operations required. If it is not possible, return .
public static int cookies(int k, List<Integer> A) {
        if(A.size()==0){
            return -1;
        }
        if(A.size()==1){
            return (A.get(0)<k)?-1:0;
        }
        Queue<Integer> queue=new PriorityQueue<>(A);
        int res=0;
        while(queue.peek()<k){
            if(queue.size()<2){
                return -1;
            }
            int a=queue.poll();
            int b=queue.poll();
            queue.add(a+(2*b));
            res++;
        }
        return res;
    }