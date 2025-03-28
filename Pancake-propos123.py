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
    forbidden_vertices.add(v)
    neigh = nbrs(v)
    select = neigh
    n = 1
    while bool(select):
        # print(f"{n}.", "path:", path)
        # print(f"{n}.", "Select:", select)
        # print(f"{n}.", "forbidden_vertices:", forbidden_vertices)
        x = select.pop()
        path.append(x)
        for u in forbidden_vertices:
            forbidden_vertices = forbidden_vertices.union(nbrs(u))
        for v in select:
            forbidden_vertices.add(v)
        forbidden_vertices.add(x)
        neigh = nbrs(x)
        select = neigh.difference(forbidden_vertices)
        n = n + 1
    # print(f"{len(path)}.", "path:", path)
    # print(f"{len(path)}.", "forbidden_vertices:", forbidden_vertices)
    # print(f"|forbidden_vertices| = {len(forbidden_vertices)}")
    return len(path) - 1, path


x = 1234
print(f"input v:{x} \nLength of path: {traverser(x)[0]}\nPath: {traverser(x)[1]}")
