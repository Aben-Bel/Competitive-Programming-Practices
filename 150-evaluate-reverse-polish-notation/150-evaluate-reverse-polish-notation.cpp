class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        int a, b;
        
        stack<int> Expression;
        
        for(int i=0;i<tokens.size();i++){
            if(tokens[i].size() > 1 || isdigit(tokens[i][0])) 
                Expression.push(stoi(tokens[i]));
            else{
                a = Expression.top();
                Expression.pop();
                b = Expression.top();
                Expression.pop();
                
                switch(tokens[i][0]){
                    case '+':
                        Expression.push(a+b);
                        break;
                    case '-':
                        Expression.push(b-a);
                        break;
                    case '*':
                        Expression.push(a*b);
                        break;
                    case '/':
                        Expression.push(b/a);
                        break;
                }
            }
        }
        
        return Expression.top();
    }
};