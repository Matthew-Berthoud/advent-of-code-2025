from collections import defaultdict

with open("input.txt") as f:
    lines = [line.strip().split(",") for line in f.readlines()]
    reds = [(int(line[0]), int(line[1])) for line in lines]

green_x_to_y = defaultdict(set)
prev_x, prev_y = reds[-1]
for cur_x, cur_y in reds:
    for y in range(min(cur_y, prev_y), max(cur_y, prev_y) + 1):
        green_x_to_y[cur_x].add(y)
    for x in range(min(cur_x, prev_x), max(cur_x, prev_x) + 1):
        green_x_to_y[x].add(cur_y)
    else:
        raise IOError("Improper input")


area_to_coords = defaultdict(list)
areas = []

# loop thru and build max heap of areas
for i, (x1, y1) in enumerate(reds):
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]
        x0, x, y0, y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

        area = (y - y0 + 1) * (x - x0 + 1)

# loop thru popping from the max heap
# and do a recursive fill starting from indside the rectangle
# if you hit a 0 index without hitting a border it's invalid.
# in order for this to run efficiently the recursive fill alg will prioritize filling upper left, then left, then upper.
