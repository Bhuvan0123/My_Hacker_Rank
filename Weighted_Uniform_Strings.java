// Given a string, , let  be the set of weights for all possible uniform contiguous substrings of string . There will be  queries to answer where each query consists of a single integer. Create a return array where for each query, the value is Yes if . Otherwise, append No.

// Note: The  symbol denotes that  is an element of set .
public static List<String> weightedUniformStrings(String s, List<Integer> queries) {
    List<String> retList = new ArrayList<>();
    List<Integer> sumList = new ArrayList<>();
    String regex = "([a-z])\\1*";
    Pattern p = Pattern.compile(regex);
    Matcher m = p.matcher(s);
    while(m.find()){
        String sub = m.group();
        char curr = sub.charAt(0);
        int count = sub.length();
        for(int i=0;i<count;i++){
            sumList.add(((int)curr-97+1)*(i+1));
        }
        s=s.replace(sub,"");
    }
    
    for(int i=0;i<queries.size();i++){
        if(sumList.contains(queries.get(i))){
            retList.add("Yes");
        }else{
            retList.add("No");
        }
    }
    return retList;

}