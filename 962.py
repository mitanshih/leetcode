
'''962. Maximum Width Ramp
Created on 2024-10-11 23:05:29

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack: list[int] = []
        for index, num in enumerate(nums):
            while not stack or nums[stack[-1]] > num:    #chance for start
                stack.append(index)

            #
        answer: int = 0

        for index in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[index]:
                answer = max(answer, index - stack.pop())

            #
            if not stack:
                break

        return answer

class Solution_bad:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack: list[int] = []

        left: int = 0
        right: int = -1
        answer: int = 0
        for index, num in enumerate(nums):
            while stack and num < stack[0]:
                stack.pop()
                if stack == []:
                    left = index
                    right = index - 1

            stack.append(num)
            right += 1

        for index, num in enumerate(nums[left::-1]):
            if num <= stack[-1]:
                left -= index

        return right - left


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().maxWidthRamp([6, 0, 8, 2, 1, 5, 6, 7, 7, 7, 8])

#%%
