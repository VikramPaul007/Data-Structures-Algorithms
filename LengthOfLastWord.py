"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/length-of-last-word/

    Problem Statement: Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.
    A word is a maximal substring consisting of non-space characters only.

    Example 1:

    Input: s = "Hello World"
    Output: 5
    Explanation: The last word is "World" with length 5.

    Example 2:

    Input: s = "   fly me   to   the moon  "
    Output: 4
    Explanation: The last word is "moon" with length 4.

    Example 3:

    Input: s = "luffy is still joyboy"
    Output: 6
    Explanation: The last word is "joyboy" with length 6.

    Constraints:

    1 <= s.length <= 104
    s consists of only English letters and spaces ' '.
    There will be at least one word in s.
"""

class LengthOfLastWord:
    def __init__(self) -> None:
        pass
    
    # The idea is to traverse the list from end &
    # calculate the length of last word.
    def lengthOfLastWord(self, s: str) -> int:
        # Variable to hold if count has started,
        # to check for cases where end of the string
        # contains one or more spaces.
        count_started = False
        last_word_length = 0
        
        #Traversing the string from end
        for i in reversed(s):
            if i == " ":
                # If the char is space & count hasn't started yet
                # then just continue to the previous char else
                # break the loop as we have now counted the length
                # of the last word in the given string
                if count_started == False:
                    continue
                else:
                    break
            else:
                # If the char is not a space and count
                # hasn't started yet, we update count_started
                # variable to True and update the length counter by 1
                if count_started == False:
                    count_started = True
                last_word_length += 1
                
        # Return the length counter variable        
        return last_word_length


str = " Hello World "
# Length of last word should be 5

obj = LengthOfLastWord()
print(obj.lengthOfLastWord(str))
            