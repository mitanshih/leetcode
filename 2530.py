
'''2530. Maximal Score After Applying K Operations
Created on 2024-10-14 12:37:39
2024-10-14 13:57:52

@author: MilkTea_shih
'''

#%%    Packages
import heapq

#%%    Variable


#%%    Functions
class Solution:
    def ceil(self, x: int, y: int = 3) -> int:
        x += (y - 1)
        x //= y

        return x

    def maxKelements(self, nums: list[int], k: int) -> int:
        result: int = 0

        max_heap: list[int] = [-num for num in nums]
        heapq.heapify(max_heap)

        for _ in range(k):
            selected_number: int = heapq.heappop(max_heap)
            result -= selected_number

            heapq.heappush(max_heap, self.ceil(selected_number))

        return result


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().maxKelements(
        [756902131, 995414896, 95906472, 149914376, 387433380, 848985151],
        6)

#%%
