
'''2285. Maximum Total Importance of Roads
Created on 2024-06-28 23:04:22
2024-06-29 00:58:53

@author: MilkTea_shih
'''

#%%    Packages


#%%    Variable


#%%    Functions
class Solution_referenceOfListRecorded:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        #Adding the new key in Dictionary is slower
        # than allocating memory directly by `n` size in List.
        city_visited_times: list[int] = [0] * n

        for cityA, cityB in roads:
            city_visited_times[cityA] += 1
            city_visited_times[cityB] += 1

        city_visited_times.sort()

        return sum(frequency * n
                   for n, frequency in enumerate(city_visited_times, 1))

class Solution_dictionaryOfRecorded:
    def maximumImportance(self, n: int, roads: list[list[int]]) -> int:
        city_visits: dict[int, int] = {}

        for cities in roads:
            for city in cities:
                #Memory allocation while adding the new key
                # requires additional overhead.
                city_visits[city] = city_visits.get(city, 0) + 1
            #

        for city, _ in sorted(city_visits.items(),
                              key=lambda x: x[1], reverse=True):
            city_visits[city] = n
            n -= 1

        return sum(city_visits[city] for cities in roads for city in cities)

#%%    Main Function


#%%    Main
if __name__ == '__main__':
    pass

#%%
