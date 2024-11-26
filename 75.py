
'''75. Sort Colors
Created on 2024-06-16 17:02:46

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left, current, right = 0, 0, len(nums) - 1

        while current <= right:
            if nums[current] == 2:
                nums[current], nums[right] = nums[right], nums[current]

                #current += 1  #NOTICE: switch `current` to `right`
                # do not increase the current index!!
                right -= 1
            elif nums[current] == 1:
                current += 1
            else:
                nums[left], nums[current] = nums[current], nums[left]

                current += 1
                left += 1


#%%    Main Function

#%%    Main
if __name__ == '__main__':
    pass

#%%
class Solution_:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index, length_nums = 0, len(nums)

        while index < length_nums:
            if nums[index] == 2:
                nums.append(nums.pop(index))
                length_nums -= 1

            else:
                if not nums[index]:
                    nums.insert(0, nums.pop(index))

                index += 1
