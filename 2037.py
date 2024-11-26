
'''2037. Minimum Number of Moves to Seat Everyone
Created on 2024-06-16 16:47:14

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        result: int = 0
        seats.sort()
        students.sort()

        index: int = 0
        while index < len(seats):
            seat, student = seats[index], students[index]

            result += abs(seat - student)

            index += 1

        return result

class Solution_one_line:
    def minMovesToSeat(self, seats: list[int], students: list[int]) -> int:
        return sum(abs(seat - student) for seat, student
                   in zip(*map(sorted, (seats, students))))  # type: ignore

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
