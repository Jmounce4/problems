/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package leetcodesolutions;

/**
 *
 * @author Julian
 */
public class TwoSum {
        public int[] twoSum(int[] nums, int target) {
        int a;
        int b;
        int sum;
        int[] result = new int[2];
        boolean edit = false;
        for(int i = 0; i <= nums.length; i++){
            if(edit == true){
                break;
            }
            a = nums[i];
            
            for(int j = 1; j <= nums.length-1; j++){
                if(i == j){
                    continue;
                }
                b = nums[j];
                sum = a+b;
                if(sum == target){
                    result[0] = i;
                    result[1] = j;
                    edit = true;
                    break;
                }
            }
        
        }
                return result;
        }

    
}
