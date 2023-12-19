def imageSmoother(self, img):
    """
    :type img: List[List[int]]
    :rtype: List[List[int]]
    """
    final = []

    i =j = 0
    m = len(img)
    n = len(img[0])
    while i < m:
        j = 0
        rows = []
        while j < n:
            sum = 0
            units = 0
            ni = i - 1
            nj = j - 1
            c1 = 0
            while c1 < 3:
                c2 = 0
                if c1 + ni >= 0 and c1 + ni < m:
                    while c2 < 3:
                        if c2 + nj >= 0 and c2 + nj < n:
                            sum += img[c1+ni][c2+nj]
                            units += 1
                        c2 += 1
                c1 += 1
            rows.append(sum/units)
            j += 1
        final.append(rows)
        i += 1
    return final

