# Evaluate Reverse Polish Notation


>
Evaluate the value of an arithmetic expression in Reverse Polish Notation.
Valid operators are +, -, *, /. Each operand may be an integer or another expression.
>Some examples:
>
>   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9  
>   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6


解题思路：后缀表达式求值，用一个stack即可。
字符串转数字其实可以用库函数: int [stoi](http://www.cplusplus.com/reference/string/stoi/?kw=stoi) (const string&  str, size_t* idx = 0, int base = 10);

```cpp
bool isOperator(string s){
    if(s.length() == 1 &&
       (s[0] == '+' || s[0] == '-' || s[0] == '*' || s[0] == '/'))
        return true;
    return false;
}
int toInt(string s){
    stringstream ss(s);
    int r;
    ss >> r;
    return r;
}
int evalRPN(vector<string> &tokens) {
    stack<int> op;
    for(int i = 0; i < tokens.size(); i++){
        string t = tokens[i];
        int op2 = 0; int op1 = 0;
        if(isOperator(t)){
            switch (t[0]){
                case '+':
                    assert(op.size()>=2);
                    op2 = op.top(); op.pop();
                    op1 = op.top(); op.pop();
                    op.push(op1+op2);
                    break;
                case '-':
                    assert(op.size()>=2);
                    op2 = op.top(); op.pop();
                    op1 = op.top(); op.pop();
                    op.push(op1-op2);
                    break;
                case '*':
                    assert(op.size()>=2);
                    op2 = op.top(); op.pop();
                    op1 = op.top(); op.pop();
                    op.push(op1*op2);
                    break;
                case '/':
                    assert(op.size()>=2);
                    op2 = op.top(); op.pop();
                    op1 = op.top(); op.pop();
                    assert(op2 != 0);
                    op.push(op1/op2);
                    break;
                default:
                    assert(false);
                    break;
            }
        }else{
            op.push(toInt(t));
        }
    }
    return op.top();
}
```

