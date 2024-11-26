
'''1863. Sum of All Subset XOR Totals
Created on 2024-10-18 15:21:58

@author: MilkTea_shih
'''

#%%    Packages
import functools
import operator

#%%    Variable


#%%    Functions
class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        ors = functools.reduce(operator.or_, nums)
        ans = 0

        def dfs(i: int, path: int) -> None:
            nonlocal ans
            if i == len(nums):
                if path == ors:
                    ans += 1
                return

            dfs(i + 1, path)
            dfs(i + 1, path | nums[i])

        dfs(0, 0)
        return ans

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().subsetXORSum([3, 2, 1, 5])

#%%
