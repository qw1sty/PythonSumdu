size = 7
mat = [[0]*size for _ in range(size)]

for r in range(size):
    for c in range(size):
        if r + c >= size - 1:
            mat[r][c] = 2*size - 1 - (r + c)

for row in mat:
    print(" ".join(f"{x:2d}" for x in row))
