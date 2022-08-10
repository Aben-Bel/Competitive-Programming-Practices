class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        def repeatedLen(s, index):
            ptr = index
            while ptr<len(s) and s[ptr]==s[index]:
                ptr+=1
            return ptr-index+1
        
        def isStrechy(word):
            ptrS = 0
            ptrW = 0 
            
            while ptrS < len(s) and ptrW < len(word):
                # print(ptrS, ptrW)
                if s[ptrS] != word[ptrW]:
                    return False
                countW = repeatedLen(word, ptrW) - 1
                countS = repeatedLen(s, ptrS) - 1
                
                if countW>countS:
                    return False
                if countW != countS and countS < 3:
                    return False
                
                ptrS += countS
                ptrW += countW
            
            return True if ptrS == len(s) and ptrW == len(word) else False
        
        ans = 0
        for word in words:
            if isStrechy(word):
                ans += 1
            
        return ans