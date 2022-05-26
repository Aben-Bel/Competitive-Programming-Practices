class Solution {
public:
    string decodeString(string s) {
        stack<char> stack;
        
        for(int i=0;i<s.length();i++){
            if(s[i] == ']'){
                string toDecodeString = "";
                
                // first get the decode string
                while(stack.top() != '['){
                    toDecodeString += stack.top();
                    stack.pop();
                }
                
                // get the k 
                stack.pop(); // pop '['
                int basePlace = 1;
                int k = 0;
                while (!stack.empty() && isdigit(stack.top())){
                    k = k + (stack.top() - '0') * basePlace;
                    stack.pop();
                    basePlace *= 10;
                }
                
                // push toDecodeString in reverse order k times
                while(k!=0){
                    for(int j=toDecodeString.size()-1; j>=0;j--){
                        stack.push(toDecodeString[j]);
                    }
                    k--;
                }
                
            }else{
                stack.push(s[i]);
            }
        }
        
        string result = "";
        for(int i=stack.size()-1;i>=0;i--){
            result = stack.top() + result;
            stack.pop();
        }
        return result;
    }
};