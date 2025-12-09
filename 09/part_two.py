with open("input.txt") as f:
    lines = [line.strip().split(",") for line in f.readlines()]
    reds = [(int(line[0]), int(line[1])) for line in lines]

largest = 0
for i, (x1, y1) in enumerate(reds):
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]
        area = (abs(y2 - y1) + 1) * (abs(x2 - x1) + 1)
        largest = max(area, largest)
print(largest)
