class Solution {
public:
    bool isValid(string s) {

        if(s.length() == 0){
            return true;
        }
        stack<char> stack;

        for(char ch : s){
            if(ch == '[' || ch == '{' || ch == '('){
                stack.push(ch);
            }
            else{
                if(stack.empty()){
                    return false;
                }
                if(ch == ']' && stack.top() == '['){
                    stack.pop();
                }
                else if(ch == '}' && stack.top() == '{' ){
                    stack.pop();
                }
                else if(ch == ')' && stack.top() == '(' ){
                    stack.pop();
                }else{
                    return false;
                }
            }
        }
        return stack.empty();
    }
};
