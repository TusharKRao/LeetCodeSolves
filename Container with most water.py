def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """

    l = 0
    r = len(height) - 1
    a = 0

    if r - l > 1:
        a = min(height[l], height[r]) * (r - l)
        while l < r:
            if height[l] < height[r]:
                l = l + 1
            else:
                r = r - 1
            new_a = min(height[l], height[r]) * (r - l)
            a = max(new_a, a)
        return a
    else:
        return min(height[l], height[r])