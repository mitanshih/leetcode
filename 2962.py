
'''2962. Count Subarrays Where Max Element Appears at Least K Times
Created on 2024-03-29 15:55:16
Pass on 2024-03-29 17:53:54
2024-03-29 18:08:55 Optimize done!

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def countSubarrays(self, nums: list[int], k: int) -> int:
        result: int = 0

        max_element, length = max(nums), len(nums)

        head_index: int = 0  #start index of sliding window
        count: int = 0
        for index, num in enumerate(nums):  #end index of sliding window
            if num == max_element:
                count += 1
            while count >= k:
                result += (length - index)  #rest of times (right of index)

                if nums[head_index] == max_element:
                    count -= 1
                head_index += 1  #move sliding window

        return result


#%%    Main Function
print(Solution().countSubarrays(
    [73, 54, 15, 4, 23, 70, 53, 65, 73, 73, 2, 72, 36, 71, 73, 69, 35,
     18, 62, 73, 62, 73, 73, 50, 30, 73, 20, 71, 60, 9, 12, 57, 48, 73,
     40, 20, 8, 73, 73, 73, 34, 59, 31, 49, 73, 5, 51, 36, 47, 38, 36,
     58, 34, 42, 23, 28, 52, 73],
    1))    #IndexError: `head_index+=1` in front of `nums[head_index]`


#%%    Main
if __name__ == '__main__':
    class Solution_bestReference:
        def countSubarrays(self, nums: list[int], k: int) -> int:
            #let element at index 0 be `max_element` and record 0 in list
            max_element: int = nums[0]
            max_element_index_list: list[int] = [0]

            nums_length = len(nums)
            for i in range(1, nums_length):  #skip element at index 0
                if nums[i] > max_element:  #find maximum in `nums`
                    max_element = nums[i]
                    max_element_index_list = [i]  #reassign list
                elif nums[i] == max_element:  #record index of maximum
                    max_element_index_list.append(i)

            # appear times of elements in `nums` cannot be satisfied
            if len(max_element_index_list) < k:
                return 0
            else:
                ans: int = 0
                previous_index: int = -1
                #`-k`: the last k elements is neglected
                #`+k`: skip k elements to satisfy the condition
                for l in range(len(max_element_index_list) - k + 1):
                    ans += ((nums_length - max_element_index_list[l + k - 1])
                            * (max_element_index_list[l] - previous_index))
                    #The answer can separate to 2 parts:
                    #the length from right-to-end of the last max_element;
                    #the length from start-to-left of the first max_element
                    #and plus the answer by multiple two parts in each loop
                    previous_index = max_element_index_list[l]
                return ans

#%%
