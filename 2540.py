
'''2540. Minimum Common Value
Created on 2024-03-09 13:59:05
2024-03-09 14:26:54

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_UseSet:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums_sets: map[set[int]] = map(set, (nums1, nums2))
        intersection: set[int] = set.intersection(*tuple(nums_sets))
        return min(intersection) if intersection else -1

class Solution_TwoPointer:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        nums1_index = nums2_index = 0
        nums1_length, nums2_length = len(nums1), len(nums2)

        while nums1_index < nums1_length and nums2_index < nums2_length:
            if nums1[nums1_index] == nums2[nums2_index]:
                return nums1[nums1_index]
            elif nums1[nums1_index] < nums2[nums2_index]:
                nums1_index += 1
            else:  #nums1[nums1_index] > nums2[nums2_index]
                nums2_index += 1
        return -1


#%%    Main Function
Solution = Solution_UseSet()  #fast
#Solution = Solution_TwoPointer()
print(Solution.getCommon([1, 2, 3], [2, 4]))

#%%    Main
if __name__ == '__main__':
    pass

#%%
