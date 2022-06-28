class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # test cases
        # "" -> [] not [""]
        # "1234"
        # "23"
        # "1"
        # "123"
        if digits == "": 
            return []
        phone = [[""],[""],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"], ["w","x","y","z"]]
        
        results = []
        def backtrack(i, result):
            # base case
            if i == len(digits): 
                results.append(""+result)
                return
            
            # recurssion 
            boxOfLetters = phone[int(digits[i])]
            for character in boxOfLetters:
                result += character 
                backtrack(i+1, result)
                result = result[:len(result)-1]
                
        backtrack(0,"")
        return results
        
        # time complexity will be: O(4^n) where n is length of digits
        # space complexity: O(n) + O(9*4=36 size of list of character) O(1) 
        # output: O(4^n)
        # if i was asked to construct digits=2356
        # [""],              0
        # ["a","b","c"],     1
        # ["d","e","f"],     2 -> result = "fi"
        # ["g","h","i"],     3
        # ["j","k","l"],     4
        # ["m","n","o"],     5
        # ["p","q","r","s"], 6
        # ["t","u","v"],     7
        # ["w","x","y","z"]] 8
# asking 234 i=3   result = "dh" 
#               2 [d,e,f], 4 [j,k,l]
#       2 d
#        /|\
#     3[g,h,i]
#     g   h  i
#        /|\
# 4[j,k,l]
#  /|\
# if i == len(digits):
#    results.append(result)
#    return 
#       2 e
#        /|\
#     3[g,h,i]
    
#       2 f
#        /|\
#     3[g,h,i]
        # first i will have boxes where the index is the number and value is the is the character
        # i will have an index (this is index is for the digits) "233"
            # backtracking function called construct
               # base check
                    # i want to check if the length of current result == length of the digit
                    # i will collect the current result 
                    # and halt the recurrsion
               # recurssion call 
                    # i will go througth the boxes and pick them one by one at index i
#                     so far: result = "a"
#                     3 -> ["d","e","f"]
#                     result = "ad"
#                     ad then calls the recurssion by incrementing i 
                    # backtrack by removing the last character in result 
#                     result = "ae"
#                     ae then calls the recurssion by incrementing
                    
                    # append to result and call recurssoin by incrementing i
        
        
        
        
        
        
        
        
        
        
        
        
        