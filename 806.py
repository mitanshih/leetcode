
'''806. Number of Lines To Write String
Created on 2024-02-17 13:48:59
2024-02-17 15:23:49
2024-02-17 15:45:04  start to optimize
2024-02-17 16:57:59

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def make_table(self, char_width_list: list[int]) -> dict[str, int]:
        char_list: map = map(chr, range(97, 123))  #lowercase of English
        return dict(zip(char_list, char_width_list))

    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        LIMIT_LENGTH: int = 100
        length_table: dict[str, int] = self.make_table(widths)

        line: int = 1
        current_length: int = 0
        for char_length in (length_table[i] for i in s):
            current_length += char_length
            #
            if current_length > LIMIT_LENGTH:
                line += 1
                current_length = char_length
            #
            #line += (new_line_flag := current_length > LIMIT_LENGTH)
            #current_length = (current_length * (not (new_line_flag))
            #                  + char_length * new_line_flag)

        return [line, current_length]


#%%    Main Function
print(Solution().numberOfLines(
    [10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10],
    "a"))

#%%    Main
if __name__ == '__main__':
    s = "abcdefghijklmnopqrstuvwxyz"
    current_char, *s = s  # type: ignore
    s_iter = iter(s)
    while len(s) > 1:
        try:
            char = next(s_iter)
        except StopIteration:
            break
        else:
            print(char)
    pass

#%%
class Solution_:
    def make_table(self, char_width_list: list[int]) -> dict[str, int]:
        char_list: map = map(chr, range(97, 123))  #lowercase of English
        return dict(zip(char_list, char_width_list))

    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        LIMIT_LENGTH: int = 100
        length_table: dict[str, int] = self.make_table(widths)
        line: int = 1

        current_length: int = 100
        current_char: str = s[0:1]
        char_length: int = length_table[current_char]

        if len(s) > 1:
            s_iter = iter(s[1:])  #Iterator
            while True:
                current_length -= char_length
                try:
                    character: str = next(s_iter)
                except StopIteration:
                    return [line, (LIMIT_LENGTH - current_length)]
                else:
                    char_length = length_table[character]  #the next character length
                    if current_length < char_length:
                        #NOTICE: `current_length` < 2: maybe no need to check
                        #or current_length < 2):  #the smallest length of `s`
                        line += 1
                        current_length = LIMIT_LENGTH
                finally:
                    current_char = character

        else:
            return [line, char_length]
