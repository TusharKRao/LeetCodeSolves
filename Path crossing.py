def isPathCrossing(path):
    """
    :type path: str
    :rtype: bool
    """

    map = {
        (0,0): True,
    }

    prev = (0,0)
    curr = None

    for dir in path:
        if dir == 'N':
            curr = (prev[0], prev[1]+1)
        elif dir == 'E':
            curr = (prev[0]+1, prev[1])
        elif dir == 'W':
            curr = (prev[0]-1, prev[1])
        else:
            curr = (prev[0], prev[1]-1)

        if curr in map:
            return True
        else:
            map.update({curr: True})
            prev = curr
    return False