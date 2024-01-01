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



print(canSum(8,[2, 3, 5]))