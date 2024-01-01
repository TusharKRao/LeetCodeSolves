def gridTravel (m, n, memo={}):
    key = (m, n)
    if key in memo:
        return memo[key]
    if m == 0 or n == 0:
        memo[key] = 0
        return 0
    if m == 1 and n == 1:
        memo[key] = 1
        return 1
    memo[key] = gridTravel(m-1, n, memo) + gridTravel(m, n-1, memo)
    return memo[key]

print(gridTravel(18,18))