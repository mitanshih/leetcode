
'''2696. Minimum String Length After Removing Substrings
Created on 2024-10-07 15:45:07
2024-10-07 16:47:46

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def minLength(self, s: str) -> int:
        answer: list[str] = []
        for item in s:
            if (answer and ((item == 'B' and answer[-1] == 'A')
                            or (item == 'D' and answer[-1] == 'C'))):
                answer.pop()
            else:
                answer.append(item)

        return len(answer)

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
