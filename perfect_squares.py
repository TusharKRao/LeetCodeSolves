
import math
def numSquares(n):
    """
    :type n: int
    :rtype: int
    """
    dp = [None] * (n+1)
    dp[0] = 0
    mex = int(math.sqrt(n))
    pool = []
    for i in range(1, mex+1):
        pool.append(i*i)
    while dp[n] is None:
        for i, item in enumerate(dp):

            if item is not None:
                for sq in pool:
                    nu = sq + i
                    if nu <= n and dp[nu] is not None:
                        dp[nu] = min(dp[nu], item + 1)
                    elif nu <= n:
                        dp[nu] = item + 1
    return dp[n]

print(numSquares(12))