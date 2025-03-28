def prefix_reversal(x: int, i: int):
    x = str(x)
    x1 = x[0:i]
    y = x1[::-1] + x[i:]
    return int(y)


def nbrs(v: int):
    n = len(str(v)) + 1
    nbrs = set()
    for i in range(2, n):
        nbrs.add(prefix_reversal(v, i))
    return nbrs


def traverser(v: int):
    path = []
    path.append(v)
    forbidden_vertices = set()
    neigh = nbrs(v)
    select = neigh
    while bool(select):
        x = select.pop()
        path.append(x)
        for v in select:
            forbidden_vertices.add(v)
        forbidden_vertices.add(path[-2])
        neigh = nbrs(x)
        select = neigh.difference(forbidden_vertices)

    return len(path) - 1, path


v = 123
print(f"v: {v} \nThe Length of path: {traverser(v)[0]} \nPath: {traverser(v)[1]}")

v = 1234
print(f"v: {v} \nThe Length of path: {traverser(v)[0]} \nPath: {traverser(v)[1]}")
