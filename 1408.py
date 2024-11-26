
'''1408. String Matching in an Array
Created on 2024-02-09 14:34:44
2024-02-09 16:33:04  have a break, father calls me for a help
2024-02-09 17:33:17  restart coding, I try to not think about program
2024-02-09 18:39:25

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def make_table(self, strings: list[str]) -> dict[int, list[int]]:
        """make table with elements in `strings`. 

        Args:
            strings (list[str]): string list will be converted to a table

        Returns:
            dict[str, list[int]]: clear dictionary: key is string length, 
            and value is its index in `strings`.
        """
        table: dict[int, list[int]] = {}
        for idx, element in enumerate(strings):
            if (string_length := len(element)) in table:
                table[string_length].append(idx)
            else:
                table[string_length] = [idx]

        return table

    def match_string(self, strings_key: list[int], pattern_index: int
                     ) -> str:  # type: ignore
        patterns: list[int] = self.string_length_table[pattern_index]
        while (strings :=
               self.string_length_table[strings_key.pop()]) if strings_key \
                else False:
            for pattern in patterns:
                for string in strings:
                    if self.words[pattern] in self.words[string]:
                        yield self.words[pattern]

        return ''

    def stringMatching(self, words: list[str]) -> list[str]:
        self.words: list[str] = words

        self.string_length_table: dict[int, list[int]] = self.make_table(words)
        string_length_list: list[int] = sorted(self.string_length_table.keys(),
                                               reverse=True)

        result_set: set[str] = set()  #remove duplicates from the list.
        for idx in range(len(string_length_list)):
            result_list_: list[str] = [i
                                       for i in self.match_string(
                                           string_length_list[:-idx - 1],
                                           string_length_list[-idx - 1]) if i]

            #REVIEW: before: result_list.append(result_list_)
            result_set.update(result_list_)

        return [*result_set] if result_set else []


#%%    Main Function
#the first test in wrong answer
print(Solution().stringMatching(["leetcoder", "leetcode", "od", "hamlet", "am"]))
#REVIEW: Duplicate substrings are not taken into consideration.
# change `result_list` to a set and change back to list before return

#%%    Main
if __name__ == '__main__':
    pass

#%%
class Solution_:    #TODO: different `make_table()` isn't test it speed
    def make_table(self, strings: list[str]) -> dict[int, list[int]]:
        """make table with elements in `strings`. 

        Args:
            strings (list[str]): string list will be converted to a table

        Returns:
            dict[str, list[int]]: clear dictionary: key is string length, 
            and value is its index in `strings`.
        """
        #max length is given as 30
        table: dict[int, list[int] | False] = dict.fromkeys(range(1, 30 + 1),
                                                            False)
        for idx, element in enumerate(strings):
            string_length: int = len(element)
            if table[string_length]:
                table[string_length].append(idx)
            else:
                table[string_length] = [idx]

        return {k: v for k, v in table.items() if v}

    def stringMatching(self, words: list[str]) -> list[str]:
        string_length_table: dict[int, list[int]] = self.make_table(words)
        #string_length_list: list[int] = string_length_table.keys()
        for i in string_length_table.keys():
            print(i)
        return []
