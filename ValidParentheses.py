"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/valid-parentheses/

    Problem Statement: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

    An input string is valid if:
    1. Open brackets must be closed by the same type of brackets.
    2. Open brackets must be closed in the correct order.

    Example 1:

    Input: s = "()"
    Output: true

    Example 2:

    Input: s = "()[]{}"
    Output: true

    Example 3:

    Input: s = "(]"
    Output: false

    Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

from collections import deque

class ValidParentheses:
    def __init__(self) -> None:
        pass

    def isValid(self, s: str) -> bool:
        stack = deque()

        # If length of input string is less than 2, 
        # then return False as not enough chars present 
        # in the string to make it Valid.
        if len(s) < 2 or len(s) % 2 != 0:
            return False
        
        # Looping over the chars in the input string
        for c in s:
            # The idea is to push the closing parentheses into 
            # stack upon encountering the opening one.
            # Otherwise will work just as fine.
            if c == '{':
                stack.append('}')
            elif c == '[':
                stack.append(']')
            elif c == '(':
                stack.append(')')

            # When the parentheses that are being pushed into the
            # stack is encountered, check if the stack is empty
            # or if the top most element in stack is the currently 
            # encountered char. This is because of the 2nd condition
            # (Open brackets must be closed in the correct order).
            # If not return False as it invalidates the 2nd condition.
            elif c == '}' or c == ']' or c == ')':
                if len(stack) == 0 or stack.pop() != c:
                    return False
            else:
                pass
        
        # Return True if stack is empty, else False
        return len(stack) == 0

str_list = ["{}[]", "({])}", "({}[])"]
obj = ValidParentheses()

for str in str_list:
    print(obj.isValid(str))
                