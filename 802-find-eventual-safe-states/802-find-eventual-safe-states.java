class Solution {
    int[][] graph;
    public List<Integer> eventualSafeNodes(int[][] graph) {
        this.graph = graph;
        List<Integer> result = new ArrayList<>();
        int[] color = new int[graph.length];
        
        for(int i=0;i<graph.length;i++){
            if(dfs(i,color)){
                result.add(i);
            }
        }
        return result;
    }
    // White: 0, Grey: 1, Black: 2 
    public boolean dfs(int node, int[] color){
        if(color[node] > 0) return color[node] == 2;
        
        color[node] = 1;
        for(int i=0;i<graph[node].length;i++){
            if(color[graph[node][i]] == 2) continue;
            
            if(color[graph[node][i]] == 1 || !dfs(graph[node][i],color)) return false;
        }
        
        color[node] = 2;
        return true;
    }
}