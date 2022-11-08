class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:        
        if turnedOn == 0:
            return ["0:00"]
        
        hours = [8,4,2,1]
        minutes = [32, 16, 8, 4, 2, 1]
        generatedHour = {0:["0"]}
        generatedMinute = {0:["00"]}
        for i in range(1, turnedOn+1):
            generatedHour[i] = []
            self.generateNums(0,0, generatedHour[i], hours, i, 12)
        for i in range(1, turnedOn+1):
            generatedMinute[i] = []
            self.generateNums(0,0, generatedMinute[i], minutes, i, 60)
        
        ans = []
        for i in range(turnedOn+1):
            for j in range(turnedOn+1):
                if i + j == turnedOn:
                    for hour in generatedHour[i]:
                        temp = [str(hour), ":",""]
                        for minute in generatedMinute[j]:
                            string = str(minute)
                            if len(string) == 1:
                                temp[-1] = "0" + string
                            else:
                                temp[-1] = string
                            ans.append("".join(temp))
        
        return ans
        
    def generateNums(self, i, picked, answer, bucket, numOfPicks, maxSum):
        if numOfPicks == 0:
            if picked < maxSum:
                answer.append(picked)
            return
        
        for j in range(i, len(bucket)):
            self.generateNums(j+1, picked + bucket[j], answer, bucket, numOfPicks - 1, maxSum)
        
        
        
        
        
        
                
