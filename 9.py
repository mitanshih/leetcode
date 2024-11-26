
'''9. Palindrome Number
Created on 2024-10-09 14:39:02
2024-10-09 17:08:51

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            temp: int = x
            reverse_x: int = 0
            while temp > 0:
                # forward previous number and add current
                reverse_x = reverse_x * 10 + temp % 10
                # backward `temp`
                temp //= 10

            return reverse_x == x

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x < 10:
            return True
        elif x < 100:
            return x % 11 == 0

        temp: int = x
        digits: int = 1
        while (temp := temp // 10):
            digits += 1

        iterations, extra = divmod(digits, 2)
        left_number, right_number = divmod(x, 10 ** iterations)

        if iterations == 1:    # from 101 to 999
            return left_number // 10 == right_number

        if extra:    #odd digits
            left: tuple[int, int] = divmod(left_number, 10)
            left = (left[1], left[0])
        else:
            left = divmod(left_number, 10 ** iterations)
        right: tuple[int, int] = divmod(right_number, 10)

        for iteration in range(iterations - 1, -1, -1):
            left = divmod(left[1], 10 ** iteration)
            if left[0] != right[1]:    #not palindrome
                return False

            right = divmod(right[0], 10)

        return True

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    test: tuple[int, ...] = (1000030001,)
    for number in test:
        print(Solution_reference().isPalindrome(number))

#%%
