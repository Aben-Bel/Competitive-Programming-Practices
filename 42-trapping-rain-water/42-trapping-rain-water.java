class Solution {
    public int trap(int[] height) {
        int max = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for(int i=0;i<height.length;i++){
            while(!stack.isEmpty() && height[stack.peek()] < height[i]){
                int top = stack.pop();
                if(stack.isEmpty()) break;
                int dis = i - stack.peek() - 1;
                int h = Math.min(height[i], height[stack.peek()])-height[top];
                max += dis*h;
            }
            stack.push(i);
        }
        return max;
    }
}