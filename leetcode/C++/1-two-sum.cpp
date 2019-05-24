class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector <int> ans;
        int num_all = nums.size();
        map <int, int> hashMap;
         
        for (int i=0; i < num_all; i++){
            map <int, int>::iterator iter = hashMap.find(target-nums[i]);  
             
            if (iter != hashMap.end()){
                ans.push_back(iter->second);
                ans.push_back(i);
                return ans;
            }
            else
                hashMap.insert(pair<int, int>(nums[i], i)); 
        }
        return ans;
    }
};