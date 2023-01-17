'''
	Given a string, find the length of the longest substring without repeating characters.
	Examples:
	Given "abcabcbb", the answer is "abc", which the length is 3.
	Given "bbbbb", the answer is "b", with the length of 1.
	Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''
#------------------------------------------------------------------------------

# (1/3) My solution. Time: O (2n)

def lengthOfLongestSubstring(s):
    
    ht = {}

    # filled up hash table
    for index, value in enumerate(s):
        if value in ht:
            ht[value].append(index)
        else:
            ht[value] = [index]

    longestsubs =0
    subs =""

    for index, value in enumerate(s):

        if value in subs:
            if len(subs)> longestsubs:
                longestsubs = len(subs)

            # if current value found duplicate in substring, 
            # then restart substring indexed after duplicate value  
            
            subs_new_begining = ht[value][ht[value].index(index)-1]
            subs = s[subs_new_begining+1:index+1]
        else:
            subs +=  value

    # test input " "
    return max(len(subs),longestsubs)  


#------------------------------------------------------------------------------
''' (2/3)
another way. Time:  O(n) | Space: O(1)
streching left,right pointers on string 's' by taking reference of hashtable for 
begining index of longest substring'''  

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        result, left = 0, 0
        lookup = {}
        for right in range(len(s)):
            if s[right] in lookup:
                left = max(left, lookup[s[right]]+1)
            lookup[s[right]] = right
            result = max(result, right-left+1)
        return result
 
    

''' C++
// Time:  O(n)
// Space: O(1)

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int result = 0;
        unordered_map<char, int> lookup;
        for (int left = 0, right = 0; right < s.length(); ++right) {
            if (lookup.count(s[right])) {
                left = max(left, lookup[s[right]] + 1);
            }
            lookup[s[right]] = right;
            result = max(result, right - left + 1);
        }
        return result;
    }
};



Readings:  on s = "abcabcbb"  
left   right   result   lookup{}
0       0       1       {a : 1}
0       1       2       {a : 1, b :2}
0       2       3       {a : 1, b :2 , c :3 }
1       3       3       {a : 4, b :2 , c :3 }
2       4       3       {a : 4, b :3 , c :3 }

'''    
    


''' (3/3) 
#------------------------------------------------------------------------------
another way. Time:  O(n) | Space: O(1)
streching left,right pointers on string 's' by taking reference of charset
[instead of hashtable, assuming 128 possible characters in i/p string] for 
begining index of longest substring'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = [None] * 128

        left = right = 0

        res = 0
        while right < len(s):
            r = s[right]

            index = chars[ord(r)]
            if index is not None and left <= index < right:
                left = index + 1

            res = max(res, right - left + 1)

            chars[ord(r)] = right
            right += 1
        return res
    
'''C++

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        // we will store a senitel value of -1 to simulate 'null'/'None' in C++
        vector<int> chars(128, -1);

        int left = 0;
        int right = 0;

        int res = 0;
        while (right < s.length()) {
            char r = s[right];

            int index = chars[r];
            if (index != -1 and index >= left and index < right) {
                left = index + 1;
            }
            res = max(res, right - left + 1);

            chars[r] = right;
            right++;
        }
        return res;
    }
};
    
'''
#------------------------------------------------------------------------------