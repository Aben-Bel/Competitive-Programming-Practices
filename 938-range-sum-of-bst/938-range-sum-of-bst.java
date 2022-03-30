/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rangeSumBST(TreeNode root, int low, int high) {
        ArrayDeque<TreeNode> stack = new ArrayDeque<>();
        int sum = 0;
        TreeNode cur = root;
        while(cur != null || !stack.isEmpty()){
            if(cur!=null){
                stack.push(cur);
                cur = cur.left;
            }else{
                TreeNode node = stack.pop();
                if(node.val> high) return sum;
                if(node.val <= high && node.val >= low){
                    sum+=node.val;
                }
                cur = node.right;
            }
        }
        return sum;
    }
}