
'''
Created on 2024-10-18 17:09:16

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
def combi(r, n):  # rC_n = rC_n-1 * (r - n + 1) // n
    return 1 if n == 0 else combi(r, n - 1) * (r - n + 1) // n


#%%    Main Function
height = 12
array = [[combi(r, n) for n in range(r + 1)] for r in range(height)]

maximum_digit: int = 0
maximum_in_array: int = array[-1][(len(array[-1]) + 1) // 2]  # array middle
while maximum_in_array:
    maximum_in_array //= 10
    maximum_digit += 1

# rC_n
for r in range(len(array)):
    print(f"\n{(len(array) - r) * maximum_digit * ' '}", end="")
    for n in range(len(array[r])):
        print(f"{array[r][n]:{maximum_digit * 2}d}", end="")

#%%    Main
if __name__ == '__main__':
    pass

#%%
