
'''1331. Rank Transform of an Array
Created on 2024-10-07 15:21:39
2024-10-07 15:26:43

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        rank_table: dict[int, int] = {
            number: rank for rank, number in enumerate(sorted(set(arr)), 1)}

        return [rank_table[number] for number in arr]

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
