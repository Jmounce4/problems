class Solution {
    public boolean isPalindrome(String s) {
        String str = s.replace(" ", "").toLowerCase();
        str = str.replaceAll("[^a-zA-Z0-9]", "");
        if (str.length()<=1){
            return true;
        }
        Boolean result = true;
        int strSize = str.length()-1;
        for(int i = 0; i<strSize; i++, strSize--){
        char startChar = str.charAt(i);
        char endChar = str.charAt(strSize);
        if (startChar != endChar){
            result = false;
        }

        }
        

        

        return result;
    }
}
