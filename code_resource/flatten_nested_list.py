
'''
Created on 2024-12-10 15:45:33

@author: MilkTea_shih
'''

#%%    Packages
from typing import TypeVar

#%%    Variable
T = TypeVar('T')

#%%    Functions
class Solution:
    def flatten_list(self, nested_list: list) -> list[T]:
        flat_list: list[T] = []

        def flatten_recursive(x: list) -> None:
            for item in x:
                if isinstance(item, list):
                    flatten_recursive(item)
                else:
                    flat_list.append(item)
            #

        flatten_recursive(nested_list)
        return flat_list

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
