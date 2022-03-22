class Solution {
    
    private HashMap<Pair<Integer,Integer>, Integer> mem = new HashMap<>();
    
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<Integer>();
        for(int i=0;i<=rowIndex;i++){
            res.add(p(rowIndex,i));
        }
        return res;
    }
    
    public int p(int i, int j){
        if(i==0 || j==0 || i==j) return 1;
        Pair<Integer, Integer> ij = new Pair(i,j);
        if(mem.containsKey(ij)) return mem.get(ij);
        
        int result = p(i-1,j-1) + p(i-1,j);
        mem.put(ij, result);
        return result;
    }
}