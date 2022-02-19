"""
You are given an array of integers where the items correspond to stock prices and the indexes of the array correspond
to sequential days. Write a function getMaxProfit that calculates the maximum amount you can earn by buying once and
selling once. The worst you can do is a profit of $0 (you buy/sell even or don’t buy/sell at all).

You can only sell a stock on a day after you bought it.
You can’t sell before you buy
You can’t sell on the same day that you buy
"""


def get_max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return print(f"Max profit of stock price {prices} is: [{max_profit}].")


if __name__ == '__main__':
    get_max_profit([9, 2, 4, 3, 8, 5])
    get_max_profit([10, 8, 7, 6, 5, 4])
