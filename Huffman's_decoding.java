// Huffman coding assigns variable length codewords to fixed length input characters based on their frequencies. More frequent characters are assigned shorter codewords and less frequent characters are assigned longer codewords. All edges along the path to a character contain a code digit. If they are on the left side of the tree, they will be a 0 (zero). If on the right, they'll be a 1 (one). Only the leaves will contain a letter and its frequency count. All other nodes will contain a null instead of a character, and the count of the frequency of all of it and its descendant characters.

// For instance, consider the string ABRACADABRA. There are a total of  characters in the string. This number should match the count in the ultimately determined root of the tree. Our frequencies are  and . The two smallest frequencies are for  and , both equal to , so we'll create a tree with them. The root node will contain the sum of the counts of its descendants, in this case . The left node will be the first character encountered, , and the right will contain . Next we have  items with a character count of : the tree we just created, the character  and the character . The tree came first, so it will go on the left of our new root node.  will go on the right. Repeat until the tree is complete, then fill in the 's and 's for the edges.
void decode(String s, Node root) {
    String res="";
    Node curr=root;
    for(int i=0;i<s.length();i++){
        if(s.charAt(i)=='0'){
            curr=curr.left;
        }
        else{
            curr=curr.right;
        }
        res+=curr.data;
        if(curr.left==null && curr.right==null){
            curr=root;
        }
    }
    System.out.print(res.replace("\0", ""));
}
