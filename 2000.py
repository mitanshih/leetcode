
'''2000. Reverse Prefix of Word
Created on 2024-05-09 17:32:19
2024-05-09 17:40:02  bad performance, start optimizing
2024-05-09 17:46:20  Done! Runtime is decreasing from 42 to 33 ms.

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reversed_list: list[str] = []
        for index, letter in enumerate(word):
            reversed_list.append(letter)
            if letter == ch:
                return ''.join(reversed(reversed_list)) + word[index + 1:]

        return word


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
class Solution_referenceBest:
    def reversePrefix(self, word: str, ch: str) -> str:
        ch_index = word.find(ch)  #NOTICE: better than `str.index` then raise
        if ch_index != -1:
            return word[ch_index::-1] + word[ch_index + 1:]
        return word


class Solution_:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            ch_index: int = word.index(ch)
        except ValueError:  #`ch` is not in `word`
            return word
        else:
            ch_index += 1  #slice-string is end at `index + 1`
            return word[:ch_index][::-1] + word[ch_index:]
