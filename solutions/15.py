# Problem 15

gridSize = (20, 20)
w = gridSize[0] + 1
h = gridSize[1] + 1
size = w * h
grid = [0 for n in range(size)]
grid[0] = 1

for i in range(size):
    if (i + 1) % w != 0:
        grid[i + 1] += grid[i]
    if i < size - w:
        grid[i + w] += grid[i]

print(grid[-1])
