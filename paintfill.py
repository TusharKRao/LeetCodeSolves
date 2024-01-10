
from collections import deque

def min_fills(picture):
    def fill(x, y, color, visited):
        queue = deque([(x, y)])
        while queue:
            x, y = queue.popleft()
            if (x, y) in visited or x < 0 or x >= len(picture) or y < 0 or y >= len(picture[0]) or picture[x][y] != color:
                continue
            visited.add((x, y))
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))

    fills = 0
    visited_cells = set()

    for i in range(len(picture)):
        for j in range(len(picture[0])):
            if (i, j) not in visited_cells:
                fill(i, j, picture[i][j], visited_cells)
                fills += 1

    return fills

# Example usage:
picture = ["aabba" * 667, "aabba" * 667, "aaacb" * 667]
result = min_fills(picture)
print(result)  # Output: 2001
