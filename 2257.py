
'''2257. Count Unguarded Cells in the Grid
Created on 2024-11-21 16:13:14
2024-11-21 18:06:54

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def hash_cell(self, cell: list[int]) -> int:
        #assert len(cell) == 2
        return cell[0] * self.x + cell[1]

    def countUnguarded(
        self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]
    ) -> int:
        self.x = n
        result: int = m * n

        # let `if *element* in *structure*` in O(1) because of `set`
        hash_guards: set[int] = set(map(self.hash_cell, guards))
        hash_walls: set[int] = set(map(self.hash_cell, walls))

        cell_limit: int = result  #hash cell maximum and plus 1 for iter_stop

        seen_cell: set[int] = set()
        for guard in guards:
            current_cell: int = self.hash_cell(guard)
            # search four cardinal directions
            if guard[0] != m - 1:    #south direction
                for cell in range(current_cell + n, cell_limit, n):
                    if cell in hash_walls or cell in hash_guards:
                        break
                    if cell not in seen_cell:
                        seen_cell.add(cell)
                        result -= 1
                #
            if guard[1] != n - 1:    #east direction
                for cell in range(current_cell + 1, guard[0] * n + n):
                    if cell in hash_walls or cell in hash_guards:
                        break
                    if cell not in seen_cell:
                        seen_cell.add(cell)
                        result -= 1
                #

            if guard[0] != 0:    #north direction
                for cell in range(current_cell - n, -1, -n):
                    if cell in hash_walls or cell in hash_guards:
                        break
                    if cell not in seen_cell:
                        seen_cell.add(cell)
                        result -= 1
                #
            if guard[1] != 0:    #west direction
                for cell in range(current_cell - 1, guard[0] * n - 1, -1):
                    if cell in hash_walls or cell in hash_guards:
                        break
                    if cell not in seen_cell:
                        seen_cell.add(cell)
                        result -= 1
                #

        result -= len(guards) + len(walls)

        return result


#%%    Main Function
Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]])

#%%    Main
if __name__ == '__main__':
    pass

#%%
