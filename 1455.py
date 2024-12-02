
'''1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence
Created on 2024-12-02 13:22:21

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word_len: int = len(searchWord)
        strings: list[int] = [
            index for index, string in enumerate(sentence.split(' '), 1)
            if len(string) >= word_len and string[:word_len] == searchWord
        ]

        return strings[0] if strings else -1  # No matching returns -1.

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
