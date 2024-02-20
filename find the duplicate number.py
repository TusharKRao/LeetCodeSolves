def findDuplicate(nums: List[int]) -> int:
    n = len(nums) - 1
    visited = set()
    prev = 0
    while True:
        visited.add(prev)
        next = nums[prev]
        if next in visited:
            return next
        else:
            prev = next
