class Solution {
    
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        HashMap<Integer, List<Integer>> outDegree = new HashMap<>();
        int[] inDegree = new int[numCourses];
        Queue<Integer> queue = new LinkedList<>();
        
        for(int i=0;i<prerequisites.length;i++){
            int src = prerequisites[i][1];
            int dest = prerequisites[i][0];
            List<Integer> lst = outDegree.getOrDefault(src, new ArrayList<>());
            lst.add(dest);
            outDegree.put(src, lst);
            inDegree[dest]+=1;
        }
        for(int i=0;i<numCourses;i++){
            if(inDegree[i] == 0) queue.offer(i);
        }
        
        
        int[] result = new int[numCourses];
        int i=0;
        while(!queue.isEmpty()){
            int node = queue.remove();
            result[i++] = node;
            
            for(int nei : outDegree.getOrDefault(node, new ArrayList<>())){
                inDegree[nei]-=1;
                if(inDegree[nei] == 0) queue.offer(nei);
            }
        }
        
        if(i==numCourses) return result;
        
        return new int[0];
    }
}