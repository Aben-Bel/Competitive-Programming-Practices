class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        HashMap<Integer, List<Integer>> adjList = new HashMap<>();
        
        for(int[] edge : prerequisites){
            indegree[edge[0]]+=1;
            List<Integer> neighbours = adjList.getOrDefault(edge[1], new ArrayList<Integer>());
            neighbours.add(edge[0]);
            adjList.put(edge[1], neighbours);
        }
        
        Queue<Integer> queue = new LinkedList<>();
        for(int i=0;i<numCourses;i++){
            if(indegree[i] == 0){
                queue.offer(i);
            }
        }
        
        int[] topSort = new int[numCourses];
        int i = 0;
        while(!queue.isEmpty()){
            int cur = queue.remove();
            topSort[i++] = cur;
            if (adjList.containsKey(cur)) {
                for(int node : adjList.get(cur)){
                    indegree[node]-=1;
                    if(indegree[node]==0){
                        queue.offer(node);
                    }
                }
            }
        }
        
        if(i==numCourses){
            return true;
        }
        return false;
    }
}