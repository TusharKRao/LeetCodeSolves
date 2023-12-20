def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """

    sum = 0
    dir = 1
    if x < 0:
        dir = -1
        x = x*(-1)
    l = len(str(x))
    while l > 0:
        rem = x%10
        x = x/10
        l -= 1
        sum += rem*pow(10, l)

    if sum*dir >= pow(2, 31) - 1 or sum*dir <= -1 * pow(2, 31):
        return 0
    else:
        return sum*dir

    #fastest way is to use string conversion and then reversal post which you convert again