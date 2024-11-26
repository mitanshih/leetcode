
'''945. Minimum Increment to Make Array Unique
Created on 2024-06-15 14:27:12
2024-06-15 16:59:14

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        dp: list[int] = [0] * (max(nums) + 1)
        # counts the frequency of each number in `nums`
        for num in nums:
            dp[num] += 1

        count: int = 0
        for i in range(len(dp) - 1):
            if dp[i] > 1:
                #depleted_frequency: int = dp[i] - 1
                count += dp[i] - 1

                # Pass the `depleted_frequency` to the next index value
                dp[i + 1] += (dp[i] - 1)
                # then reset the frequency of i-th in `dp`
                #dp[i] = 1

        # sum of arithmetic sequence: `n` is the length of the sequence
        # list start from 0: (0 + (n - 1)) * n / 2

        # The last element of dp means the frequency of the duplicates
        # aren't be depleted, so the following formula will be:
        #   frequency: int = dp[index], the sequence shows as follows:
        #   [index, index + 1, index + 2, ..., index + frequency - 1]
        #   it is equal to -> [+0, +1, +2, ..., +(frequency - 1)]
        # Therefore, the sum of arithmetic sequence is:
        #       +1 +2 + .... +(frequency - 1)
        #   sum of the first and last element is `1 + (frequency - 1)`
        #   length of the sequence is `frequency - 1`
        # Example:
        #   frequency = 4
        #   sequence: [index+0, index+1, index+2, index+3]
        #   the sum of arithmetic sequence is:
        #       +1 +2 +3 = (1 + 3) * 3 / 2 = 6

        count += dp[-1] * (dp[-1] - 1) // 2
        return count

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        result: int = 0

        current_maximum: int = -1  #smaller than the minimum of `nums`
        for number in sorted(nums):
            if current_maximum < number:
                current_maximum = number
            else:
                step: int = current_maximum - number + 1
                result += step
                current_maximum += 1

        return result

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
