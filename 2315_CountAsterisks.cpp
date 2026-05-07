class Solution {
public:
    int countAsterisks(string s) {
        bool open = false;
        bool closed = false;
        int total = 0;
        int temp = 0;

        for(int i = 0; i < s.length(); i++){
            
            if (s[i] == '*'){
                temp += 1;
            }

            if (s[i] == '|'){
                
                

                if (!open){
                    total+=temp;
                    temp = 0;
                    open = true;
                    continue;
                }

                if (open && !closed){
                    temp = 0;
                    open = false;
                    continue;
                }
                
            }
            if (i == s.length()-1){
                total+=temp;
            }
        }
        return total;
    }
};
