#include <vector>
class Solution {
public:
    bool rotateString(string s, string goal) {
        if (s.length() != goal.length()){
            return false;
        }
        if (s == goal){
            return true;
        }
        
        for (int i = 0; i < s.length(); i++){
            char front = s[0];
            s = s.erase(0, 1);
            s += front;
            if (s == goal){
            return true;
            }
        }
        return false;
    }
};
