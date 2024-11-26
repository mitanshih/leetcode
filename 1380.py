
'''1380. Lucky Numbers in a Matrix
Created on 2024-07-19 23:25:52

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def luckyNumbers (self, matrix: list[list[int]]) -> list[int]:
        maximum_element: list[int] = [max(column) for column in zip(*matrix)]
        minimum_element: list[int] = [min(row) for row in matrix]

        return list(set(maximum_element) & set(minimum_element))

    #TODO: use for-loop and do it again

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
