
'''3075. Maximize Happiness of Selected Children
Created on 2024-05-09 16:57:11
2024-05-09 17:05:17

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        happiness.sort()

        result: int = 0
        for picked_times in range(k):
            child_happiness: int = happiness[-picked_times - 1] - picked_times
            if child_happiness < 0:
                break
            result += child_happiness
        return result


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
