def removeDuplicates(nums: List[int]) -> int:
    visit = set()
    main_idx = 0
    for idx, item in enumerate(nums):
        if item in visit:

            continue
        else:
            visit.add(item)
            nums[main_idx] = item
            main_idx += 1

    return main_idx