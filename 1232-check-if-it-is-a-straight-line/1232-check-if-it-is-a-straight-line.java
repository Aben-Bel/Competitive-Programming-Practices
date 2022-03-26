class Solution {
    public boolean checkStraightLine(int[][] coordinates) {
        double x1 = coordinates[0][0], x2 = coordinates[1][0];
        double y1 = coordinates[0][1], y2 = coordinates[1][1];
        // y = mx + b -> b = y-mx;
        double m = x1!=x2 ? (y1-y2)/(x1-x2) : 0;
        double b = y1-m*x1;
        double firstX = x1;
        double firstY = y1;
        boolean horizontal = y1==y2;
        for(int i=2;i<coordinates.length;i++){ 
            x1 = coordinates[i][0];
            y1 = coordinates[i][1];
            System.out.println(m*x1 + b);
            if(horizontal){
                if(y1==firstY) continue;
                else return false;
            }
            if(m==0 && x1 != firstX) return false;
            if(m!=0 && m*x1 + b != y1) return false; 
        }
        return true;
    }
}