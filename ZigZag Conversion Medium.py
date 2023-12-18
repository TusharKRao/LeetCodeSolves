def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """

    L = [''] * numRows
    step = 0
    direction = 1
    if numRows == 1 or numRows >= len(s):
        return s
    for item in s:
        L[step] += item
        step += 1*direction
        if step == 0 or step == numRows-1:
            direction *= -1
    return ''.join(L)