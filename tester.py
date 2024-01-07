def canSum (s, nums, memo={}):
    if s in memo:
        return memo[s]

    if s == 0:
        memo[s] = True
        return True

    if s < 0:
        memo[s] = False
        return False

    for num in nums:
        rem = s - num
        if canSum(rem, nums):
            memo[s] = True
            return True

    memo[s] = False
    return False



print(canSum(300,[7, 14]))

def cs(sum, nums):
    t = [False] * (sum+1)
    t[0] = True

    for i in range(0, sum):
        if t[i] is True:
            for num in nums:
                if num + i < sum:
                    t[num+i] = True
    print(t[sum])

cs(300, [7,14])