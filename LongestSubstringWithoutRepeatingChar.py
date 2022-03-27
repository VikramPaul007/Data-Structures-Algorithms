"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

    Problem Statement: Given a string s, find the length of the longest substring without repeating characters.

    Example 1:

    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

    Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
"""

class LongestSubstring:
    def __init__(self) -> None:
        pass

    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        map = {}
        prev_max, curr_max = 0, 0
        
        for ind, val in enumerate(s):
            if val in map.keys():
                prev_max = max(prev_max, map[s[ind]] + 1)
                
            map[s[ind]] = ind
            curr_max = max(curr_max, ind - prev_max + 1)
            
        return curr_max

str = "How are you?"
#answer should be 8, note that space is not considered 
#as a char when using a dictionary data structure
longestSubstring = LongestSubstring()
print(longestSubstring.lengthOfLongestSubstring(str))