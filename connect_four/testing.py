grid = [[],[],[],[],[],[],[]]
counter = 1
for x in range(7):
    for y in range(6):
        grid[x].append(counter)
        counter+=1
print(grid)
