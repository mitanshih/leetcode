
'''459. Repeated Substring Pattern
Created on 2024-02-02 16:07:21
2024-02-02 18:09:26
2024-02-02 18:40:01  optimize the string-matching but performance is bad.
2024-02-02 20:23:24  string-matching: `s[slice] != s` -> `head_tail_search`

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def find_first_letter_index(self, string: str) -> list[int]:
        first_letter: str = string[0]
        return [idx for idx, element in enumerate(string)
                if element == first_letter]

    def head_tail_search(self, string: str, pattern: str, check_time: int
                         ) -> bool:
        pattern_length: int = len(pattern)
        idx_: int = -1
        for idx in range(check_time):
            match_start, match_end = string[idx], string[idx_]
            idx %= pattern_length  #ensure the range of the index
            if not (pattern[-idx - 1] == match_end
                    and pattern[idx] == match_start):
                return False
            idx_ -= 1
        return True

    def match_string_head_tail_search(self, pattern: str, s: str) -> bool:
        remainder = (length_s := len(s)) % len(pattern)
        if remainder:
            return False
        else:
            string_length_half: int = int(length_s / 2) + (length_s % 2)
            return self.head_tail_search(s, pattern, string_length_half)

    def match_string(self, pattern: str, s: str) -> bool:
        quotient, remainder = divmod(len(s), pattern_len := len(pattern))
        #remainder = (length_s := len(s)) % len(pattern)
        if remainder:  #length of s is not divisible by pattern's
            return False  #means pattern cannot be repeated completely.
        else:
            for time in range(quotient):  #how many times of substring
                if s[time * pattern_len:(time + 1) * pattern_len] != pattern:
                    return False
                #
            return True
            #string_length_half: int = int(length_s / 2) + (length_s % 2)
            #return self.head_tail_search(s, pattern, string_length_half)

    def repeatedSubstringPattern(self, s: str) -> bool:
        index_list: list[int] = self.find_first_letter_index(s)
        if (s_length := len(s)) <= 1:  #never repeated substring
            return False
        elif s_length == len(index_list):  #s consists of only 1 letter
            return True
        else:
            #reverse `index_list` to use list.pop() in O(1)
            # instead of list.pop(0) in O(n)
            #index_list.reverse()
            #index_list.pop()
            #
            #REVIEW: use first element (0) in index_list to break loop
            while True if (index := index_list.pop()) else False:
                #slicing string and finding the pattern
                if self.match_string(s[:index], s[index:]):
                    return True

            return False


#%%    Main Function
#the first test in wrong answer
print(Solution().repeatedSubstringPattern("ababab"))
#REVIEW: in `match_string()` forgets to time the `pattern_len` when iterate
# s[time:time + pattern_len] -> s[time * pattern_len:(time + 1) * pattern_len]

print(Solution().repeatedSubstringPattern("abcabcabcabc"))

#%%    Main
if __name__ == '__main__':
    pass

#%%
