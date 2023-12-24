def minOperations(s: str) -> int:

    f0 = f1 = 0

    for i, item in enumerate(s):
        if i % 2 == 0:
            if s[i] != "1":
                f1 += 1
            else:
                f0 += 1
        else:
            if s[i] != "0":
                f1 += 1
            else:
                f0 += 1

    return min(f0, f1)
