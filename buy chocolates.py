def buyChoco(prices, money):
    """
    :type prices: List[int]
    :type money: int
    :rtype: int
    """
    prices.sort()
    if prices[0] + prices[1] <= money:
        return money - (prices[0] + prices[1])
    else:
        return money