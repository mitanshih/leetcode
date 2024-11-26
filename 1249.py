
'''1249. Minimum Remove to Make Valid Parentheses
Created on 2024-04-06 17:18:32
2024-04-06 19:20:55 stop to eat dinner
2024-04-06 20:26:32 restart
2024-04-06 22:08:07 [ Time taken: 2 hrs 43 m 43 s ]
2024-04-06 23:22:20 start optimizing
2024-04-07 00:30:05 [ Time taken: 1 hr 0 m 46 s ]

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_split: list[str] = s.split(')')  #len(s_split)-1: count of ')'

        *s_split, final = s_split
        final = final.replace('(', '')  # final part only has characters
        if s_split == []:  #right parenthesis never exists
            return final

        result: str = ''
        balance_parentheses: int = 0

        for string in s_split:
            balance_parentheses += string.count('(')
            result += string
            if balance_parentheses:
                result += ')'
                balance_parentheses -= 1

        # remove extra left parenthesis
        return ''.join(result.rsplit('(', balance_parentheses)) + final


#%%    Main Function
#wrong special cases
print(Solution().minRemoveToMakeValid("(a(b(c)d)"))
#wrong position of the non-parentheses condition
print(Solution().minRemoveToMakeValid("abc"))
#NO! I think between two parentheses must exist at least 1 character!!
print(Solution().minRemoveToMakeValid("())()(((a"))
#the non-parentheses condition
print(Solution().minRemoveToMakeValid("((((("))


#%%    Main
if __name__ == '__main__':
    pass

#%%
class Solution_bestReference:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list: list[str] = list(s)

        stack: list[int] = []
        for index, item in enumerate(s_list):
            if item == '(':
                stack.append(index)
            elif item == ')':
                if stack:
                    stack.pop()    #match!
                else:
                    s_list[index] = ''

        for index in stack:    #'(' in `s_list` not match with ')'
            s_list[index] = ''

        return "".join(s_list)

class Solution_:
    def minRemoveToMakeValid(self, s: str) -> str:
        specified_symbol: set[str] = {'(', ')'}

        characters: list[str] = []
        parentheses: dict[int, str] = {}
        characters_temp_index: int = 0
        for index, string in enumerate(s):
            if string in specified_symbol:
                parentheses[index] = string

                characters.append(s[characters_temp_index:index])
                characters_temp_index = index + 1
            #
        if parentheses == {}:
            return s
        parentheses_index: int = next(reversed(parentheses))
        if parentheses_index < len(s):
            characters.append(s[parentheses_index + 1:])  #final pattern

        # string before parentheses
        result: str = '' if s[0] in specified_symbol else characters[0]

        balance_parentheses: int = 0
        times: int = 1
        for index in parentheses:
            if times >= len(characters):
                break
            if parentheses[index] == '(':
                balance_parentheses += 1
            else:
                if balance_parentheses < 1:
                    result += characters[times]
                    times += 1
                    continue    #right parenthesis exists before left's
                balance_parentheses -= 1

            result += parentheses[index] + characters[times]
            times += 1

        # remove extra left parenthesis
        return ''.join(result.rsplit('(', balance_parentheses))
