
'''1590. Make Sum Divisible by P
Created on 2024-10-07 14:17:17

@author: MilkTea_shih
'''

#%%    Packages
from typing import Optional

#%%    Variable


#%%    Functions
class Solution:
    #[reference](https://walkccc.me/LeetCode/problems/1590/#__tabbed_1_3)
    def minSubarray(self, nums: list[int], p: int) -> int:
        total: int = sum(nums)
        remainder: int = total % p

        if remainder == 0:
            return 0

        answer: int = len(nums)
        prefix: int = 0
        prefix_index_table: dict[int, int] = {0: -1}    #initial condition
        #when the 1st to nth elements are the subarray
        #let `index - prefix_index_table[target]` count 1 more for the current

        for index, num in enumerate(nums):
            prefix = (prefix + num) % p    #current remainder
            target: int = (prefix - remainder + p) % p    #rest remainder
            if target in prefix_index_table:
                answer = min(answer, index - prefix_index_table[target])

            prefix_index_table[prefix] = index

        return -1 if answer == len(nums) else answer

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().minSubarray([8, 32, 31, 18, 34, 20, 21, 13, 1, 27, 23, 22, 11, 15, 30, 4, 2], 148)

#%%
