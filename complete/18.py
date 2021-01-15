# Problem 18

f = open("./input/18.txt")
tree = []
for line in f.readlines():
    row = []
    for x in line.strip().split():
        row.append({"value": int(x), "sums": []})
    tree.append(row)
top = tree[0][0]
top["sums"].append(top["value"])
for i in range(len(tree) - 1):
    for j in range(len(tree[i])):
        cell = tree[i][j]
        nextCell1 = tree[i + 1][j]
        nextCell2 = tree[i + 1][j + 1]
        for sum in cell["sums"]:
            nextCell1["sums"].append(nextCell1["value"] + sum)
            nextCell2["sums"].append(nextCell2["value"] + sum)
res = 0
for cell in tree[-1]:
    res = max(res, max(cell["sums"]))
print(res)
