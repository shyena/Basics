'''
	Given an array of integers, return indices of the two numbers such that they add up to a specific target.

	You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	Given nums = [2, 7, 11, 15], target = 9,

	Because nums[0] + nums[1] = 2 + 7 = 9,
	return [0, 1].
'''

# good way O(n^2)-------------------------------------------------------------------

def twoSum(nums, target):
    length = len(nums)

    for i in range(length):
        for j in range(i+1,length):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []
    
twoSum([3,2,4],6)



# better way O(n)-------------------------------------------------------------------

def twoSum(nums, target):
    mapping = {}
    for index, value in enumerate(nums):    # O(n) - filling hash table
       mapping[value]= index


    for i in range(len(nums)):              # O(n) - navigating through hash table
        remaining = target - nums[i]
        
        if remaining == nums[i]:                 
            continue
            # say nums[i] == 3, target == 6, then remaining becomes 3 which will exist in hashtable as nums[i]
        
        if remaining in mapping:                 # O(1) - searching
            return [i, mapping[remaining]]

twoSum([3,2,4],6)


# best way O(n)-------------------------------------------------------------------

def twoSum(nums, target):
    mapping = {}

    for index, value in enumerate(nums):
        remainig = target - value
        
        if remainig in mapping:                   # O(1)
            return [index, mapping[remainig]]
        else:
            mapping[value] = index
            
twoSum([3,2,4],6)



''' CPP--------------------------------------------------------------------------
// Time:  O(n)
// Space: O(n)

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> lookup;
        for (int i = 0; i < nums.size(); ++i) {
            if (lookup.count(target - nums[i])) {
                return {lookup[target - nums[i]], i};
            }
            lookup[nums[i]] = i;
        }
        return {};
    }
};
            
'''