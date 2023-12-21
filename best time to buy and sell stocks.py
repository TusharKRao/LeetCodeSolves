def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    max = min = prices[0]
    profit = 0
    for item in prices:
        if item <= min:
            max = min = item
        elif item > max:
            max = item
        if max - min > profit:
            profit = max - min
    return profit