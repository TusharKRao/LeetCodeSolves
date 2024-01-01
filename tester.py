def howSum (s, nums):

    if s == 0:
        return []
    if s < 0:
        return None

    for num in nums:
        rem = s - num
        remres = howSum(rem, nums)
        if remres is not None:
            remres += [num]
            return remres


    return None

print(howSum(300,[2, 3, 5]))
