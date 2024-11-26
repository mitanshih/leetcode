
'''1. Two Sum
Created on 2024-10-09 14:25:37

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen_table: dict[int, int] = {}
        for index, num in enumerate(nums):
            if target - num in nums:
                return [seen_table[target - num], index]
            seen_table[num] = index

        return []

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
