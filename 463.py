
'''463. Island Perimeter
Created on 2024-04-18 17:26:51
2024-04-18 18:59:20

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        result: int = 0
        row_length, column_length = len(grid), len(grid[0])
        for row_index, row in enumerate(grid):
            for column_index, item in enumerate(row):
                if item:
                    if 1 <= column_index:
                        if not grid[row_index][column_index - 1]:
                            result += 1
                    else:
                        result += 1
                    if column_index < column_length - 1:
                        if not grid[row_index][column_index + 1]:
                            result += 1
                    else:
                        result += 1
                    if 1 <= row_index:
                        if not grid[row_index - 1][column_index]:
                            result += 1
                    else:
                        result += 1
                    if row_index < row_length - 1:
                        if not grid[row_index + 1][column_index]:
                            result += 1
                    else:
                        result += 1
        return result

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
class Solution_reference:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        result: int = 0
        x, y = len(grid), len(grid[0])

        for i in range(x):
            for j in range(y):
                if grid[i][j]:
                    result += 4
                    if i > 0 and grid[i - 1][j]:
                        result -= 2
                    if j > 0 and grid[i][j - 1]:
                        result -= 2

        return result
