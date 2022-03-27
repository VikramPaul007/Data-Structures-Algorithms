"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/add-two-numbers/

    Problem Statement: You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, 
    and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example 1:

    2--> 4--> 3
    5--> 6--> 4
    -----------
    7    0    8 (Reverse is 807)

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807

    Example 2:
    Input: l1 = [0], l2 = [0]
    Output: [0]

    Example 3:
    Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
    Output: [8,9,9,9,0,0,0,1]

    Constraints:
    The number of nodes in each linked list is in the range [1, 100].
    0 <= Node.val <= 9
    It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
from audioop import add


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class AddTwoNumbers:
    def __init__(self) -> None:
        pass
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        op = result        
        carry = 0
        
        """
            Loop until the Lists are empty with no carry
            Carry check is needed for the sum of last element 
            in the lists to check if the sum is greater than 10.
            In that case add one more node with val carry//10
        """
        while l1 is not None or l2 is not None or carry > 0:
            if l1 is not None:
                carry += l1.val
                l1 = l1.next
            if l2 is not None:
                carry += l2.val
                l2 = l2.next
            
            op.next = ListNode(carry % 10)
            op = op.next
            
            carry //= 10
        
        return result.next

l1 = ListNode(9)
l1.next = ListNode(9)
l1.next.next = ListNode(9)

l2 = ListNode(9)
l2.next = ListNode(9)
# l2.next.next = ListNode(9)

addTwoNumbers = AddTwoNumbers()
result = addTwoNumbers.addTwoNumbers(l1, l2)
result_list = []
while result is not None:
    result_list.append(result.val)
    result = result.next

print(result_list)