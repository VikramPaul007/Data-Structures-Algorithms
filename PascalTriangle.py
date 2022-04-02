"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/pascals-triangle/

    Problem Statement: Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

                            1
                        1       1
                    1       2       1
                1       3       3       1
            1       4       6       4       1

    Example 1:

    Input: numRows = 5
    Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

    Example 2:

    Input: numRows = 1
    Output: [[1]]    

    Constraints:

    1 <= numRows <= 30
"""

class PascalTriangle:
    def __init__(self) -> None:
        pass

    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for i in range(numRows):
            row = []
            for j in range(0, i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i-1][j-1] + res[i-1][j])
            
            res.append(row)
            
        return res

numOfRows = 5
pascalTriangleObj = PascalTriangle()
print(pascalTriangleObj.generate(numOfRows))