
'''2938. Separate Black and White Balls
Created on 2024-10-15 21:40:41

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def minimumSteps(self, s: str) -> int:
        result, swaps = 0, 0
        for item in s:
            if item == '1':
                swaps += 1
            else:
                result += swaps

        return result


class Solution:
    def minimumSteps(self, s: str) -> int:
        result: int = 0
        step: int = 0
        multiplication: int = 0
        current: int = 0

        s_length: int = len(s)

        while current < s_length:
            if s[current] == '1':
                multiplication += 1

                step = current + 1
                while step < s_length:
                    if s[step] == '1':
                        break
                    step += 1
                result += (step - current - 1) * multiplication

                current = step
            else:
                current += 1

        return result

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().minimumSteps("11000111")

#%%
