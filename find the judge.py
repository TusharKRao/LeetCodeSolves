def findJudge(self, n: int, trust: List[List[int]]) -> int:
    visit = set()
    total = set()
    for i in range(1, n+1):
        visit.add(i)
        total.add(i)
    for item in trust:
        if item[0] in visit:
            visit.remove(item[0])
            if visit == set():
                return -1
    potential = list(visit)[0]
    for item in trust:
        if item[1] == potential and item[0] in total:
            total.remove(item[0])
    if len(list(total)) == 1:
        return potential
    else:
        return -1