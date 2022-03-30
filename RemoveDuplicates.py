"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

    Problem Statement: Return k after placing the final result in the first k slots of nums.
    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }

    If all assertions pass, then your solution will be accepted.

    Example 1:

    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Example 2:

    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Constraints:

    1 <= nums.length <= 3 * 104
    -100 <= nums[i] <= 100
    nums is sorted in non-decreasing order.
"""

class RemoveDuplicate:
    def __init__(self) -> None:
        pass

    def removeDuplicates(self, nums: list[int]) -> int:
        nums_length = len(nums)

        # If the length of the array is 0 or 1
        # then we know their won't be any duplicates, 
        # hence return the length of the list.
        if nums_length < 2:
            return nums_length

        # Hold count of unique elements and the current index
        # which is to be updated with next unique element.
        unique_count = 1
        current_idx = 1

        # We can safely assume that the first element
        # will always be a unique element. So, we'll
        # loop through the range of 1 to end of the array.
        for i in range(1, nums_length):
            # If the current element is not equal to the previous element,
            # we'll update unique count by 1. Then we'll update the array
            # position of current index with the current value and update
            # the current index count by 1 for next unique element
            if nums[i] != nums[i-1]:
                unique_count += 1
                nums[current_idx] = nums[i]                
                current_idx += 1 
        
        # Return the no of unique elements
        return unique_count


nums = [0,0,1,1,1,2,2,3,3,4]
expected_nums = [0, 1, 2, 3, 4]
unique_elements = len(expected_nums)
removeDuplicateFromArray = RemoveDuplicate()

k = removeDuplicateFromArray.removeDuplicates(nums)

if k == unique_elements:
    for i in range(0, unique_elements):
        if expected_nums[i] != nums[i]:
            print("Incorrect value at position {i}")
            break
    
    print("Success")
else:
    print("Incorrect value of unique elements in the array. Should be {unique_elements} instead of {k}")