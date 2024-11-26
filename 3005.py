
'''3005. Count Elements With Maximum Frequency
Created on 2024-03-09 15:00:25
2024-03-09 15:33:27

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        def sort_nums(nums: list[int]) -> list[tuple[int, int]]:
            result: dict[int, int] = {}
            for i in nums:
                if i in result:
                    result[i] += 1
                else:
                    result[i] = 1

            return sorted(result.items(), key=lambda item: item[1])

        sorted_nums: list[tuple[int, int]] = sort_nums(nums)  #sort by value
        result: int = 0
        _, value = sorted_nums.pop()  #default comparison
        while sorted_nums:
            _, value_ = sorted_nums.pop()
            if value != value_:
                break
            result += value_

        return result + value


#%%    Main Function
print(Solution().maxFrequencyElements([1, 2, 3, 4, 5]))

#%%    Main
if __name__ == '__main__':
    pass

#%%
