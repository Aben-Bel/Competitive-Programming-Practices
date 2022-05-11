class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> IncreasingIndex;
        unordered_map<int, int> NextGreater;
        
        if(nums2.size() == 1) nums1[0] = -1;
        else{
            for(int i=0; i<nums2.size(); i++){
                 NextGreater[nums2[i]] = -1;
                if(IncreasingIndex.empty()) IncreasingIndex.push(i);
                else{
                    while(!IncreasingIndex.empty() &&
                         nums2[i] > nums2[IncreasingIndex.top()]){
                        int top = IncreasingIndex.top();
                        NextGreater[nums2[top]] = nums2[i];
                        IncreasingIndex.pop();
                    }
                    IncreasingIndex.push(i);
                }
            }
                    
            for(int j=0; j<nums1.size();j++){
                nums1[j] = NextGreater[nums1[j]];
            }
        }
        return nums1;
    }
};