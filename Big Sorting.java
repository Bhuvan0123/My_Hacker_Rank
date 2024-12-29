
// Consider an array of numeric strings where each string is a positive number with anywhere from  to  digits. Sort the array's elements in non-decreasing, or ascending order of their integer values and return the sorted array.

public static List<String> bigSorting(List<String> unsorted) {
        Collections.sort(unsorted,new Comparator<String>() {
            @Override
            public int compare(String s1,String s2){
                int l1=s1.length();
                int l2=s2.length();
                if(l1!=l2){
                    return l1-l2;
                }
                BigInteger i1=new BigInteger(s1);
                BigInteger i2=new BigInteger(s2);
                return i1.compareTo(i2);
            }
        });
        return unsorted;
        
    }
