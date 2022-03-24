class Solution {
    public int scheduleCourse(int[][] courses) {
        Arrays.sort(courses, (course1,course2)->course1[1]-course2[1]);
        PriorityQueue<Integer> pq = new PriorityQueue<>((a,b)->b-a);
        int at = 0;
        int taken = 0;
        for(int i=0;i<courses.length;i++){
            if(courses[i][0]+at<=courses[i][1]){
                taken+=1;
                pq.offer(courses[i][0]);
                at += courses[i][0];
            }else if(!pq.isEmpty() && pq.peek() > courses[i][0]){
                at += courses[i][0] - pq.poll();
                pq.offer(courses[i][0]);
            }
        }
        
        return taken;
    }
}