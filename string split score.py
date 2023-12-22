def maxScore(s):
    """
    :type s: str
    :rtype: int
    """
    max = 0
    i = 0
    while i < len(s) -1:
        if str(s[0:i+1]).count('0') + str(s[i+1:len(s)]).count('1') > max:
            max = str(s[0:i+1]).count('0') + str(s[i+1:len(s)]).count('1')
        i += 1
    return max
