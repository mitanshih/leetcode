
'''1346. Check If N and Its Double Exist
Created on 2024-12-01 13:54:58

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        hash_arr: set[int] = set(arr)    # Searching item in set costs O(1).
        return (any((item * 2 in hash_arr or item / 2 in hash_arr)    # faster
                    for item in hash_arr if item != 0)
                or arr.count(0) > 1)    #edge case for '0'

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
