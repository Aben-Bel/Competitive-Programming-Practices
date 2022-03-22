class Solution {
    public int openLock(String[] deadends, String target) {
        HashSet<String> blockades = new HashSet<>();
        for(String s : deadends){
            blockades.add(s);
        }
        int level = 0;
        HashSet<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        if(!blockades.contains("0000")) queue.offer("0000");
        visited.add("0000");
        while(!queue.isEmpty()){
            int size = queue.size();
            while(size>0){
                String cur = queue.remove();
                if(cur.equals(target)) return level;
                String[] nextMove = generatePath(cur);
                for(String next : nextMove){
                    if(!blockades.contains(next) && !visited.contains(next)){
                        queue.offer(next);
                        visited.add(next);
                    }
                }
                size-=1;
            }
            level+=1;
        }
        return -1;
    }
    
    public String[] generatePath(String cur){
        String[] result = new String[8];
        int j=0;
        for (int i = 0; i < 4; ++i) {
            for (int d = -1; d <= 1; d += 2) {
                int y = ((cur.charAt(i) - '0') + d + 10) % 10;
                String nei = cur.substring(0, i) + ("" + y) + cur.substring(i+1);
                result[j] = nei;
                j++;
            }
        }
        return result;
    }
}