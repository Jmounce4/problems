class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {

    
        
        for(int i = 0; i < nums.size(); i++){
            if (nums[i] == target){
                return i;
            }
            if (i == 0){
                if (target < nums[i]){
                    return i;
                }
                continue;
            }
            
            if(nums[i-1] < target && nums[i] > target){
                return i;
            }

        }
        return nums.size();
    }
};
