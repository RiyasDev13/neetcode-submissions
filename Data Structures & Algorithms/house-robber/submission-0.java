class Solution {
    public int rob(int[] nums) {

        int rob    = 0;
        int no_rob = 0;

        for(int num:nums){
            int new_rob     = no_rob + num;
            int new_no_rob  = Math.max(rob,no_rob);
            rob    = new_rob;
            no_rob = new_no_rob;
        }

        return Math.max(rob,no_rob);
        
    }
}
