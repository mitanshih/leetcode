
'''2108. Find First Palindromic String in the Array
Created on 2024-07-10 23:25:19

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if word == word[::-1]:  # compare `word` to the reversed `word`
                return word

        return ''

class Solution_compare_each_letter_in_word:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            index: int = 0
            while index < len(word) // 2:
                if word[index] != word[-index - 1]:
                    break  # `word` is not palindromic!
                # keep iterating if `word[index] == word[-index - 1]`
                index += 1
            else:
                return word

        return ''

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
