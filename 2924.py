
'''2924. Find Champion II
Created on 2024-11-26 15:38:36
2024-11-26 15:51:42

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_reference:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        winner_list: list[bool] = [True] * n
        for strong, weak in edges:
            winner_list[weak] = False
        winner: int = -1    #initialization
        winner_count: int = 0
        for i in range(0, n):
            if winner_list[i]:
                winner = i
                winner_count += 1

        return winner if winner_count == 1 else -1


class Solution:
    def findChampion(self, n: int, edges: list[list[int]]) -> int:
        champion: set[int] = {i for i in range(n)}
        not_champion: set[int] = set()

        for strong, weak in edges:
            if weak in champion:
                champion.remove(weak)
            if strong in not_champion and strong in champion:  #fake champion
                champion.remove(strong)

            not_champion.add(weak)

        return -1 if len(list(champion)) != 1 else champion.pop()

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
