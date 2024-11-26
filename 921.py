
'''921. Minimum Add to Make Parentheses Valid
Created on 2024-10-09 14:07:17
2024-10-09 14:23:46

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        result: int = 0

        not_match_right_parenthesis: int = 0
        for parentheses in s:
            if parentheses == '(':
                result += 1
            elif result > 0:    #*left_parenthesis* exist
                result -= 1     # match!
            else:
                not_match_right_parenthesis += 1

        return result + not_match_right_parenthesis

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
