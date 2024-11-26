
'''3074. Apple Redistribution into Boxes
Created on 2024-04-26 14:12:29
2024-04-26 14:24:03

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def minimumBoxes(self, apple: list[int], capacity: list[int]) -> int:
        rest_apple: int = sum(apple)
        for index, item in enumerate(sorted(capacity, reverse=True), 1):
            rest_apple -= item
            if rest_apple <= 0:
                break

        return index


#%%    Main Function
print(Solution().minimumBoxes([5, 5, 5], [2, 4, 2, 7]))

#%%    Main
if __name__ == '__main__':
    pass

#%%
