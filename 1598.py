
'''1598. Crawler Log Folder
Created on 2024-07-10 23:06:07

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def minOperations(self, logs: list[str]) -> int:
        result: int = 0  #current folder level
        for log in logs:
            match log[:-1]:
                case '..':
                    if result == 0:  # if already in *main folder*
                        continue  # remain in the same folder
                    result -= 1
                case '.':  # remain in the same folder
                    continue
                case _:  # move to the child folder
                    result += 1

        return result


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
