def singleNumber(nums: List[int]) -> int:
    visit = set()
    dump = set()

    for item in nums:
        if item in dump:
            continue
        elif item in visit:
            visit.remove(item)
            dump.add(item)
        else:
            visit.add(item)

    return list(visit)[0]