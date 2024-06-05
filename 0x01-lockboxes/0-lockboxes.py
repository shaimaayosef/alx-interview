def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True
    queue = [0]

    while queue:
        current = queue.pop(0)
        for key in boxes[current]:
            if key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
