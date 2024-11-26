
'''28. Find the Index of the First Occurrence in a String
Created on 2024-01-28 15:47:45
Pass on 2024-01-28 18:20:55

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def make_table(self, string: str) -> dict[str, list[int] | bool]:
        char_list: map = map(chr, range(97, 123))  #lowercase of English
        table: dict[str, list[int] | False] = dict.fromkeys(char_list, False)
        for idx, element in enumerate(string):
            if table[element]:
                table[element].append(idx)
            else:
                table[element] = [idx]

        return table

    def match_strStr(self, match_str: str, check_length: int) -> bool:
        for idx in range(check_length):
            idx_: int = -(idx + 1)
            match_start, match_end = match_str[idx], match_str[idx_]
            if not (self.needle[idx_] == match_end
                    and self.needle[idx] == match_start):
                return False
        else:
            return True

    def strStr(self, haystack: str, needle: str) -> int:
        self.needle = needle
        self.letter_table: dict[str, list[int] | False] = self.make_table(haystack)
        if self.letter_table[needle[0]]:  #letter_table.value == False will return -1
            index_list: list[int] = self.letter_table[needle[0]]  # type: ignore
            if needle_length := len(needle):
                needle_length_half: int = int(needle_length / 2) \
                    + (needle_length % 2)
                for i in index_list:
                    haystack_slice: str = haystack[slice(i, i + needle_length)]
                    if needle_length <= len(haystack_slice) \
                            and self.match_strStr(haystack_slice, needle_length_half):
                        return i  #find!!
                return -1  #`needle` not in `haystack`

            else:
                return index_list[0]  #`needle` is a letter in haystack

        else:
            return -1  #the first letter of `needle` not in haystack


#%%    Main Function
print(Solution().strStr("babba", "bbb"))  #the first test in wrong answer
#REVIEW: `needle_length_half` with `round(float_number)` in Python
# does not always return the desired result,
# e.g., `round(4.5)` = 4;  `round(5.5)` = 6.

#%%    Main
if __name__ == '__main__':
    pass
    #char_list: map = map(chr, range(97, 123))
    #table: dict[str, list | int] = dict.fromkeys(char_list, -1)
    #for idx, element in enumerate("letters"):
    #    if table[element] == -1:
    #        table[element] = [idx]
    #    else:
    #        table[element].append(idx)  # type: ignore

#%%
