"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/pascals-triangle-ii/

    Problem Statement: Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

                            1
                        1       1
                    1       2       1
                1       3       3       1
            1       4       6       4       1

    Example 1:

    Input: rowIndex = 3
    Output: [1,3,3,1]

    Example 2:

    Input: rowIndex = 0
    Output: [1]

    Example 3:

    Input: rowIndex = 1
    Output: [1,1]    

    Constraints:

    0 <= rowIndex <= 33
    
    Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
"""

class PascalTriangleII:
    def __init__(self) -> None:
        pass
    
    # The idea is to have an list of size rowIndex,
    # and update the same list based on previous values
    # according to the Pascal's algorithm.
    # So, effectively the space complexity of the solution
    # would be O(rowIndex) for the list.
    def getRow(self, rowIndex: int) -> list[int]:
        res = [0] * (rowIndex + 1)
        res[0] = 1
        
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
                
        return res

rowInd = 6
pascalTriangleObj = PascalTriangleII()
print(pascalTriangleObj.getRow(rowInd))