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

print(howSum(7,[5, 3, 4, 7]))


def hs(s, nums):

    t = [None] * (s+1)
    t[0] = []

    for i in range(0, s):
        if t[i] is not None:
            for num in nums:
                if i + num <= s:
                    t[i + num] = t[i] + [num]

    return t[s]

print(hs(7,[5, 3, 4, 7]))
