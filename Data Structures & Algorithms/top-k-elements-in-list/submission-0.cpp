class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> umap;
        vector<std::pair<int, int>> vec;
        vector <int> result;
        for(auto element: nums){
            umap[element]++;
        }
        for(auto element: umap){
            vec.push_back({element.second, element.first});
        }
        sort(vec.begin(), vec.end(),greater<>());
        for(int i = 0; i < k ; i++){
            result.push_back(vec[i].second);
        }
        return result;
    }
};
