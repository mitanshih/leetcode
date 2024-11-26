
'''1405. Longest Happy String
Created on 2024-10-16 12:45:12

@author: MilkTea_shih
'''

#%%    Packages
import heapq

#%%    Variable


#%%    Functions
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        input_length: list[list[int]] = [
            [-value, index]    #get max value while heappop the smallest
            for index, value in enumerate([a, b, c]) if value > 0
        ]
        heapq.heapify(input_length)

        letters: tuple[str, str, str] = ('a', 'b', 'c')    #index-letter table

        # Initialization
        most_occurrence: list[int] = heapq.heappop(input_length)
        result: str = letters[most_occurrence[1]]
        most_occurrence[0] += 1
        if most_occurrence[0] < 0:
            heapq.heappush(input_length, most_occurrence)
        #

        has_repeated: bool = False
        while input_length:
            most_occurrence = heapq.heappop(input_length)
            if letters[most_occurrence[1]] != result[-1]:
                result += letters[most_occurrence[1]]
                most_occurrence[0] += 1
                if most_occurrence[0] < 0:
                    heapq.heappush(input_length, most_occurrence)

                has_repeated = False

            elif has_repeated and input_length:
                # get `second_occurrence` while `has_repeated` and
                # `letters[most_occurrence[1]] == result[-1]`
                second_occurrence: list[int] = heapq.heapreplace(
                    input_length, most_occurrence)
                result += letters[second_occurrence[1]]
                second_occurrence[0] += 1
                if second_occurrence[0] < 0:
                    heapq.heappush(input_length, second_occurrence)

                has_repeated = False
            elif has_repeated:  #while `has_repeated` and no `input_length`
                break

            else:  #most_occurrence is equal to `result[-1]` and not repeated
                result += letters[most_occurrence[1]]
                most_occurrence[0] += 1
                if most_occurrence[0] < 0:
                    heapq.heappush(input_length, most_occurrence)

                has_repeated = True

        return result

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().longestDiverseString(1, 1, 8)

#%%
