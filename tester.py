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


def gd(m, n):
    t = [[0] * (n+1) for j in range(m+1)]
    for i in range(0, m+1):
        for j in range(0, n+1):
            if i == 0 or j == 0:
                t[i][j] = 0
    t[1][1] = 1
    #initialization complete

    for i in range(0, m+1):

        for j in range(0, n+1):

            if i+1 <= m:
                t[i+1][j] += t[i][j]
            if j+1 <= n:
                t[i][j+1] += t[i][j]

    print(t[m][n])

gd(18,18)