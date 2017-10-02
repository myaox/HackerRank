x, y, z, n  = map(int, [input() for _ in range(4)])
print([[i, j , l] for i in range(x + 1) for j in range(y + 1) for l in range(z + 1) if ((i + j + l) != n)])
