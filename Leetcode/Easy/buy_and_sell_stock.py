def max_profit(prices: list[int]) -> int:
    """ Function to calculate the max profit we can sell a stock for."""
    max_p = 0

    i = 0
    j = 1
    l = len(prices)

    min_price = prices[0]

    while j < l:
        if prices[j] < prices[i]:
            min_price = prices[j]
            i = j
        else:
            profit = prices[j] - min_price
            max_p = max(profit, max_p)
        j += 1

    return max_p
