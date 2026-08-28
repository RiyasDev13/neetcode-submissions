class Solution {
    public boolean canJump(int[] nums) {

        int stepJump = nums[0];

        for(int i = 1; i < nums.length ; i++){
            stepJump--;

            if(stepJump < 0){
                return false;
            }
            
            if(nums[i] > stepJump){
                 stepJump = nums[i];
            }
        }

        return true;
        
    }
}
