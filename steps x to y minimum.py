def sol(x, y):
    dp = [None]*(y*2 + 1)
    dp[x] = 0

    while dp[y] is None:
        for i, ll in enumerate(dp):
            if ll is not None:
                #minus
                new = i-1
                if i-1 >= 0 and dp[new] is not None:
                    dp[new] = min(dp[new] + 1, ll)
                elif i-1 >= 0:
                    dp[new] = ll + 1
                #double
                mult = i * 2
                if i*2 < len(dp) and dp[mult] is not None:
                    dp[mult] = min(dp[mult], ll + 1)
                elif i*2 < len(dp):
                    dp[mult] = ll + 1
    return dp[y]



#x = 4 #2
#y = 7 #5

print(sol(5, 17))