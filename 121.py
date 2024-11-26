
'''121. Best Time to Buy and Sell Stock
Created on 2024-03-03 20:15:52
2024-03-04 01:33:01

@author: MilkTea_shih
'''

#%%    Packages
import test_input_121 as test

#%%    Variable
'''
must the right element minus the left, 
the right element is the biggest and the left element is the smallest, 
will get the maximum return.
The return must upper than zero, or return zero.

#`right` - `left` > 0 -> return `profit`; else 0
'''
""" NOTE
I was too obsessed with thinking 
that the element on the left must be smaller than the element on the right, 
which resulted in `max(list[current_index + 1:])` appearing in my code.
Every time a smaller number appears, 
I recheck to see if there is a larger number to the right of it.

The time complexity of max() is *O(n)*, and it goes into my loop, 
so the time complexity of my original code is *O(n^2)*.

"""

#%%    Functions
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        #min_price = float('inf')  #origin source code
        min_price: int
        min_price, *rest_prices = prices
        max_profit: int = 0  #if `profit` is smaller than zero, return 0

        for price in rest_prices:  #skip the first element in `prices`
            if price < min_price:  #find the minimum in `rest_prices`
                min_price = price
            elif (profit := (price - min_price)) > max_profit:
                max_profit = profit

        return max_profit


#%%    Main Function
print(Solution().maxProfit([7, 12, 1, 5, 3, 6, 4]))
print(Solution().maxProfit(test.test_input))  #[Time Limit Exceeded]
#print(Solution().maxProfit([1, 2, 4, 2, 5, 7, 2, 4, 9, 0]))
#print(Solution().maxProfit([2, 1, 2, 0, 1]))
#print(Solution().maxProfit([1, 4, 1, 4, 3, 1]))

#%%    Main
if __name__ == '__main__':
    pass
#%%
class Solution_myself:
    def maxProfit(self, prices: list[int]) -> int:
        right_element: int = 0  #definition of the minimum prices
        right_temp: int
        left_element: int = 10_000  #definition of the maximum prices

        if len(prices) > 1:
            price_dict: dict[int, int] = {}
            #key not update while making the dictionary
            #price_dict = {price: idx for idx, price in enumerate(prices)
            #              if price not in price_dict.keys()}
            for idx, price in enumerate(prices):
                if price not in price_dict.keys():
                    price_dict[price] = idx
            profit: int = right_element - left_element
            for price, idx in price_dict.items():
                if price < left_element:
                    if (prices[idx + 1:]  # check at the end of `prices`
                            and ((right_temp
                                 := max(prices[idx + 1:])) - price > profit)):
                        right_element = right_temp
                        left_element = price
                        profit = right_element - left_element

            return profit if right_element > left_element else 0
        else:
            return 0  #`len(prices) <= 1` can not calculate the profit
