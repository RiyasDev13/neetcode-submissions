class Solution {
    public int maxArea(int[] heights) {

        int n = heights.length;
        int left  = 0;
        int right = n - 1; 
        int max = -1;

        for(int i=1;i<n;i++){
            int width  = right - left; 
            int height = Math.min(heights[left],heights[right]);
            max        = Math.max(max,width * height);

            if(heights[left] < heights[right]){
                left++;
            }
            else{
                right--;
            }
        }
        
        return max;
    }
}
