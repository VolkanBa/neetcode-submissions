class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> dict;
        vector<vector<string>> vec;
        for(string str:strs){
           string copy = str;
           sort(copy.begin(),copy.end());
           dict[copy].push_back(str);
            
        }

        for(auto str : dict){
            vec.push_back(str.second);
        }

        return vec;
    }
};
