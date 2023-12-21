def maxWidthOfVerticalArea(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """

    max = 0
    n = len(points)
    inter = []
    for item in points:
        inter.append(item[0])

    inter.sort()
    i = 1
    max = inter[1] - inter[0]
    while i < n-1:
        if inter[i+1] - inter[i] > max:
            max = inter[i+1] - inter[i]
        i += 1

    return max
