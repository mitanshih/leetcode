
'''1072. Flip Columns For Maximum Number of Equal Rows
Created on 2024-11-22 16:20:37
2024-11-22 17:57:34

@author: MilkTea_shih
'''

#%%    Packages
from typing import Callable

#%%    Variable


#%%    Functions
class Solution:
    def __init__(self) -> None:
        self.invert_binary_bit: Callable[[int], int] = lambda x: x ^ 1

    def hash_row(self, array: list[int]) -> int:
        return int(''.join(map(str, array)), 2)

    def invert_binary(self, array: list[int]) -> list[int]:
        return list(map(self.invert_binary_bit, array))
        #return [binary ^ 1 for binary in array]

    def maxEqualRowsAfterFlips(self, matrix: list[list[int]]) -> int:
        hash_table: dict[int, int] = {}

        for row in matrix:
            if row[0] == 1:
                row = self.invert_binary(row)

            hashed_row: int = self.hash_row(row)

            hash_table[hashed_row] = hash_table.get(hashed_row, 0) + 1

        #result: int = 0
        #for hashed_row, count in hash_table.items():
        #    result = max(result, count)

        #return result

        return max(hash_table.values())


#%%    Main Function
Solution().maxEqualRowsAfterFlips([[0, 1], [1, 0]])

#%%    Main
if __name__ == '__main__':
    pass

#%%
