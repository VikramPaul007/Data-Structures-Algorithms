"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/linked-list-cycle/

    Problem Statement: Given head, the head of a linked list, determine if the linked list has a cycle in it.
    There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
    Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.
    Return true if there is a cycle in the linked list. Otherwise, return false.

    Example 1:

    Input: head = [3,2,0,-4], pos = 1
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

    Example 2:

    Input: head = [1,2], pos = 0
    Output: true
    Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

    Example 3:

    Input: head = [1], pos = -1
    Output: false
    Explanation: There is no cycle in the linked list.

    Constraints:

    The number of the nodes in the list is in the range [0, 104].
    -105 <= Node.val <= 105
    pos is -1 or a valid index in the linked-list.

    Follow up: Can you solve it using O(1) (i.e. constant) memory?

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedListCycle:
    def __init__(self) -> None:
        pass
    # Hair-Tortoise(Floyd's cycle detection) algorithm
    # can be used to find if the given list has any cycle.

    # The algorithm is a pointer algorithm that uses only two pointers, 
    # moving through the sequence at different speeds. This algorithm 
    # is used to find a loop in a linked list. It uses two pointers one 
    # moving twice as fast as the other one. 

    # How Does Floyd’s Cycle Finding Algorithm Works?
    # While traversing the linked list one of these things will occur-
    # The Fast pointer may reach the end (NULL) this shows that there is no loop n the linked list.
    # The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.

    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if slow is fast:
                return True

        return False

# Algorithm to create a cyclic linked list for testing
arr = [2, 5, 4, 3]
valueOfCyclicNode = 3
positionOfCycle = 1

headNode = ListNode(0)
nodeObj = headNode

for ind, item in enumerate(arr):
    nodeObj.next = ListNode(item)
    nodeObj = nodeObj.next
    if ind == positionOfCycle:
        cyclicNode = nodeObj
    if item == valueOfCyclicNode and cyclicNode is not None:
        nodeObj.next = cyclicNode
        break

# Check if the linked list has any cycle
linkedListCycleObj = LinkedListCycle()
print(linkedListCycleObj.hasCycle(headNode.next))
