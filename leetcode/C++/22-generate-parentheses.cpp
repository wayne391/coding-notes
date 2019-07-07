/*
1. string 串接可以用 + 'char'或是 + "string"
2. pass vector to function, it will be created
    https://www.geeksforgeeks.org/passing-vector-function-cpp/
3. if 沒大括號允許一行

*/

class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector < string > res;
        dfs(n, n, "", res);
        return res;
        
    }
    
    void dfs(int left, int right, string str, vector <string> & res){ // <-- 2. &
        if (left > right) 
            return;
        if (left == 0 && right == 0) 
            res.push_back(str);
        else{
            if (left > 0) 
                dfs(left - 1, right, str + '(', res);
            if (right > 0) 
                dfs(left, right - 1, str + ')', res);
        }
    }
};