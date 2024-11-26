
'''2491. Divide Players Into Teams of Equal Skill
Created on 2024-10-07 16:53:44
2024-10-07 18:05:55

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        answer: int = 0
        amount: int = int(sum(skill) / (len(skill) / 2))

        skill_table: dict[int, int] = {}
        for item in skill:
            skill_table[item] = skill_table.get(item, 0) + 1

        if len(skill) == 2:    #NOTE: special case
            return skill[0] * skill[1]
        elif len(skill_table) % 2:    #`len(skill_table)` is odd
            middle_amount: int = int(amount / 2)
            if skill_table.get(middle_amount, 1) % 2:
                return -1

            answer = int(middle_amount ** 2 * skill_table[middle_amount] / 2)
            seen_set: set[int] = {middle_amount}
        else:    #NOTE: normal case   #`len(skill_table)` is even
            answer = 0
            seen_set = set()

        for item, count in skill_table.items():
            if item in seen_set:
                continue

            target_number: int = abs(amount - item)
            if (target_number in skill_table
                    and count == skill_table[target_number]):
                answer += item * target_number * count

                seen_set.add(target_number)

            else:
                return -1
        return answer


#%%    Main Function


#%%    Main
if __name__ == '__main__':
    Solution().dividePlayers([3, 2, 5, 1, 3, 4])

#%%
