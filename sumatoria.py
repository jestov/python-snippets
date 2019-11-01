def sumatoria(n):
    if n == 0:
        return 0
    return 4*n + sumatoria(n-1)
print(sumatoria(2))
