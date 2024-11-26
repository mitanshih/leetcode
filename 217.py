
'''217. Contains Duplicate
Created on 2024-03-09 15:55:42
2024-03-09 15:59:31

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_CompareLength:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))

class Solution_List:
    def containsDuplicate(self, nums: list[int]) -> bool:
        duplicate: set[int] = set()
        for num in nums:
            if num in duplicate:
                return True
            duplicate.add(num)

        return False


#%%    Main Function
Solution = Solution_CompareLength()  #fast
#Solution = Solution_List()

print(Solution.containsDuplicate([1, 2, 3, 1]))

#%%    Main
if __name__ == '__main__':
    pass

#%%
