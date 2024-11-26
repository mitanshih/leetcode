
'''670. Maximum Swap
Created on 2024-10-17 12:46:24

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def maximumSwap(self, num: int) -> int:
        num_string: list[str] = list(str(num))
        number_table: dict[str, list[int]] = {}    #number: [index, ...]
        for index, string in enumerate(num_string):
            number_table.setdefault(string, []).append(index)

        digits: int = 0
        for string_key in ''.join(f'{i}' for i in range(9, -1, -1)):
            index_list: list[int] = number_table.get(string_key, [])
            if index_list:    #there is `string_key` in `num_string`
                digits += len(index_list)
                if digits < index_list[-1] + 1:
                    break    #have found the range of swapped numbers placed
            #
        else:    #`num` is the maximum valued number.
            return num

        for string in num_string[digits - len(index_list):digits]:
            if string != string_key:    #confirm the number needs to swap
                break

        # swap with index beside
        #result: int = int(  #swap `index - 1` and `index` in `num_string`
        #    num_string[:index - 1] + num_string[index]
        #    + num_string[index - 1] + num_string[index + 1:]
        #)
        # swap with target index
        num_string[number_table[string][0]], num_string[number_table[string_key][-1]] = \
            num_string[number_table[string_key][-1]], num_string[number_table[string][0]]
        result: int = int(''.join(num_string))

        return result

class Solution_:
    def maximumSwap(self, num: int) -> int:
        num_string: str = str(num)
        previous: str = num_string[0]
        for index, string in enumerate(num_string):
            if previous < string:
                break
        else:    #`num` is the maximum valued number.
            return num

        result: int = int(  #swap `index - 1` and `index` in `num_string`
            num_string[:index - 1] + num_string[index]
            + num_string[index - 1] + num_string[index + 1:]
        )
        return result

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().maximumSwap(98368)

#%%
