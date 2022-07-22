class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        li1 = {}
        for i, val in enumerate(list1):
            li1[val] = i
        
        result = []
        for i, val in enumerate(list2):
            if val in li1:
                result.append((i+li1[val], val))
        
        result.sort()
        print(result)
        
        answer = [result[0][1]]
        for i in range(1,len(result)):
            if result[i][0] != result[i-1][0]:
                break
            answer.append(result[i][1])
        
        return answer
            