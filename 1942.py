
'''1942. The Number of the Smallest Unoccupied Chair
Created on 2024-10-11 11:32:26
2024-10-11 16:58:29

@author: MilkTea_shih
'''

#%%    Packages
import heapq

#%%    Variable


#%%    Functions
class Solution:
    #[reference](https://algo.monster/liteproblems/1942)
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        friend_amount: int = len(times)
        empty_chair: list[int] = list(range(friend_amount))
        heapq.heapify(empty_chair)

        occupied_chair: list[list[int]] = []  # [departure, chair_number]
        #heapq.heapify(occupied_chair)

        times = sorted([*time, index] for index, time in enumerate(times))

        for arrival, departure, index in times:
            while occupied_chair and occupied_chair[0][0] <= arrival:
                heapq.heappush(empty_chair, heapq.heappop(occupied_chair)[1])

            current_chair: int = heapq.heappop(empty_chair)

            if index == targetFriend:
                return current_chair

            heapq.heappush(occupied_chair, [departure, current_chair])

        return current_chair


#%%    Main Function
class MinHeap:
    def __init__(self):
        self.heap = []

    def get_parent_index(self, index):
        return (index - 1) // 2

    def swap(self, frm, to):
        self.heap[frm], self.heap[to] = self.heap[to], self.heap[frm]

    def get_child_indexes(self, index):
        return {
            'left': index * 2 + 1,
            'right': index * 2 + 2,
        }

    def add(self, element):
        self.heap.append(element)
        current_working_index = len(self.heap) - 1
        while current_working_index > 0:
            parent_index = self.get_parent_index(current_working_index)
            if self.heap[parent_index] > self.heap[current_working_index]:
                self.swap(parent_index, current_working_index)
                current_working_index = parent_index
            else:
                break

    def remove(self):
        smallest_element = self.heap[0]
        if len(self.heap) == 1:
            self.heap = []
            return smallest_element
        last_element = self.heap.pop()
        self.heap[0] = last_element
        current_working_index = 0
        while True:
            child_indexes = self.get_child_indexes(current_working_index)
            left_child = self.heap[child_indexes['left']] if child_indexes['left'] < len(self.heap) else None
            right_child = self.heap[child_indexes['right']
                                    ] if child_indexes['right'] < len(self.heap) else None
            if left_child is None and right_child is None:
                break
            if left_child is not None and right_child is not None:
                smallest_index = child_indexes['left'] if left_child < right_child else child_indexes['right']
            elif left_child is not None:
                smallest_index = child_indexes['left']
            else:
                smallest_index = child_indexes['right']
            if self.heap[smallest_index] < self.heap[current_working_index]:
                self.swap(smallest_index, current_working_index)
                current_working_index = smallest_index
            else:
                break
        return smallest_element


#%%    Main
if __name__ == '__main__':
    Solution().smallestChair(
        [[82057, 89365],
         [32519, 49655],
         [7573, 20592],
         [8336, 11514],
         [638, 70162],
         [39511, 44262],
         [70399, 79785],
         [8702, 63564],
         [66644, 68330],
         [75156, 90448],
         [11884, 87096],
         [99068, 99875],
         [32555, 54053],
         [5910, 77572],
         [87649, 94390],
         [40084, 56483],
         [7911, 28699],
         [93308, 96154],
         [25562, 39605],
         [73966, 93173],
         [63450, 88007],
         [58811, 80045],
         [56160, 71952],
         [14333, 79867],
         [40342, 76876],
         [69943, 82175]],
        5)

#%%
