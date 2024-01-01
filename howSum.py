def howSum (s, nums, memo = {}):
    if s in memo:
        return s
    if s == 0:
        return []
    if s < 0:
        return None

    for num in nums:
        rem = s - num
        remres = howSum(rem, nums, memo)
        if remres is not None:
            remres += [num]
            memo[rem] = remres
            return remres
    return None

print(howSum(1000,[2, 3, 5]))