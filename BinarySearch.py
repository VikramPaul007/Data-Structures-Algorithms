"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/binary-search/

    Problem Statement: Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
    If target exists, then return its index. Otherwise, return -1. You must write an algorithm with O(log n) runtime complexity.

    Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4

    Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1

    Constraints:
    1 <= nums.length <= 104
    -104 < nums[i], target < 104
    All the integers in nums are unique.
    nums is sorted in ascending order.
"""

class BinarySearch:
    def __init__(self):
        pass
    
    def search(self, nums, target) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end)//2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return -1

nums = [0, 3, 5, 8, 9, 11]
target = 5
binarySearch = BinarySearch()

print(binarySearch.search(nums, target))