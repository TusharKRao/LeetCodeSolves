def maxProductDifference(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max1 = max2 = 0
    min1 = min2 = 10001

    for num in nums:
        if num > max1:
            max1 = num
        if num < min1:
            min1 = num
    nums.remove(min1)
    nums.remove(max1)
    for num in nums:
        if num > max2:
            max2 = num
        if num < min2:
            min2 = num

    print( (max1 * max2) - (min1 * min2))


maxProductDifference([10,10,10,10])