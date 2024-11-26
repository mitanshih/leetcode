
'''1497. Check If Array Pairs Are Divisible by k
Created on 2024-10-01 15:32:14
2024-10-01 16:37:45

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def canArrange(self, arr: list[int], k: int) -> bool:
        if k > 2:
            remainder_count: list[int] = [0] * k
            for item in arr:
                remainder_count[item % k] += 1
            if remainder_count[0] % 2:    # Can not be pairs while divisible
                return False

            #quotient, remainder = divmod(k, 2)
            #median of k: quotient + remainder
            for index in range(1, k // 2 + k % 2):
                if remainder_count[index] != remainder_count[-index]:
                    return False
        elif k == 2:
            return sum(arr) % 2 == 0
        return True


class Solution_:
    def canArrange(self, arr: list[int], k: int) -> bool:
        if k > 2:
            remainders: list[list[int]] = [[] for _ in range(k)]
            for item in arr:
                remainders[item % k].append(item)
            if len(remainders[0]) % 2:
                return False

            quotient, remainder = divmod(k, 2)
            #median of k: quotient + remainder%2
            for index in range(1, quotient + remainder % 2):
                if len(remainders[index]) != len(remainders[-index]):
                    return False
        elif k == 2:
            return not sum(arr) % 2
        return True
#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
