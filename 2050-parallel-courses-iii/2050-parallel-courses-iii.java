class Solution {
    HashMap<Integer, List<Integer>> outDegree;
    int[] time;
    HashMap<Integer, Integer> mem = new HashMap<>();
    public int minimumTime(int n, int[][] relations, int[] time) {
        int[] inDegree = new int[n+1];
        outDegree = new HashMap<>();
        this.time = time;
        
        for(int i=0;i<relations.length;i++){
            int src = relations[i][0];
            int dest = relations[i][1];
            
            inDegree[dest] +=1;
            List<Integer> lst = outDegree.getOrDefault(src, new ArrayList<>());
            lst.add(dest);
            outDegree.put(src, lst);
        }
        
        int maxVal = Integer.MIN_VALUE;
        for(int i=1;i<n+1;i++){
            if(inDegree[i]==0){
                maxVal = Math.max(maxVal, dfs(i));
            }
        }
        return maxVal;
    }
    
    public int dfs(int cur){
        if(!outDegree.containsKey(cur)) return time[cur-1];
        if(mem.containsKey(cur)) return mem.get(cur);
        
        int m = 0;
        for(int nei : outDegree.get(cur)){
            m = Math.max(m, dfs(nei));
        }
        
        mem.put(cur, m+time[cur-1]);
        return mem.get(cur);
    }
}