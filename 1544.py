
'''1544. Make The String Great
Created on 2024-04-07 15:04:55
2024-04-07 16:33:39 [ Time taken: 1 hr 15 m 9 s ]
2024-04-07 16:37:46 optimize
2024-04-07 16:50:27 [ Time taken: 2 m 32 s ]

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def makeGood(self, s: str) -> str:
        stack: list[str] = []

        for item in s:
            if stack:
                if item == stack[-1].swapcase():
                    stack.pop()
                else:
                    stack.append(item)
            else:
                stack.append(item)

        return "".join(stack)


#%%    Main Function
print(Solution().makeGood("leEeetcode"))

#%%    Main
if __name__ == '__main__':
    pass

#%%
class Solution_:
    def makeGood(self, s: str) -> str:
        stack: list[int] = []

        for item in map(ord, s):
            if stack:
                # Difference between lower-case and upper-case
                if abs(item - stack[-1]) == 32:  #ASCII difference
                    stack.pop()
                else:
                    stack.append(item)
            else:
                stack.append(item)

        return "".join(map(chr, stack))
