def singleNumber(nums: List[int]) -> List[int]:

    res = []
    visit = set()

    for item in nums:
        if item in visit:
            visit.remove(item)
        else:
            visit.add(item)

    for key in visit:
        res.append(key)

    return res