
'''1963. Minimum Number of Swaps to Make the String Balanced
Created on 2024-10-08 13:12:53
2024-10-08 22:47:53

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def minSwaps(self, s: str) -> int:
        not_match: int = 0
        for bracket in s:
            if bracket == '[':
                not_match += 1
            elif not_match > 0:    # `bracket` is ']' and match!
                not_match -= 1
            # else: `bracket` is ']' and not match will swap. That is answer.

        return (not_match + 1) // 2

class Solution:
    def minSwaps(self, s: str) -> int:
        left_bracket: list[int] = []
        right_bracket: list[int] = []

        for index, bracket in enumerate(s):
            if bracket == ']':
                if len(left_bracket) > 0:
                    left_bracket.pop()
                else:
                    right_bracket.append(index)

            elif bracket == '[':
                left_bracket.append(index)

        return len(right_bracket) // 2 + len(right_bracket) % 2

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().minSwaps(
        "]][[")

#%%
