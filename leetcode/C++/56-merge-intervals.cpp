
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> res;
        
        // sort
        sort(intervals.begin(), intervals.end()); 
        
        // iteration
        for (int i=0; i < intervals.size(); i++) {
            if (res.size() > 0 && res.back()[1] >= intervals[i][0]){
                vector<int> tmp{min(res.back()[0], intervals[i][0]), 
                                max(res.back()[1], intervals[i][1])};
                res.back() = tmp;
            }    
            else
                res.push_back(intervals[i]);
        }
        return res;
    }
};
