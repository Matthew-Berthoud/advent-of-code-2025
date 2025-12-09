import heapq
from collections import defaultdict

with open("example.txt") as f:
    lines = [line.strip().split(",") for line in f.readlines()]
    reds = [(int(line[0]), int(line[1])) for line in lines]


greens: set[tuple] = set()
prev_x, prev_y = reds[-1]
for cur_x, cur_y in reds:
    for y in range(min(cur_y, prev_y), max(cur_y, prev_y) + 1):
        greens.add((cur_x, y))
    for x in range(min(cur_x, prev_x), max(cur_x, prev_x) + 1):
        greens.add((x, cur_y))
    prev_x, prev_y = cur_x, cur_y

# red_set = set(reds)
# for y in range(10):
#     for x in range(15):
#         if (x, y) in red_set:
#             print("#", end="")
#         elif (x, y) in greens:
#             print("X", end="")
#         else:
#             print(".", end="")
#     print()


area_to_coords = defaultdict(set)
areas = []

# loop thru and build max heap of areas
for i, (x1, y1) in enumerate(reds):
    for j in range(i + 1, len(reds)):
        x2, y2 = reds[j]
        x0, x, y0, y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)
        area = (y - y0 + 1) * (x - x0 + 1)
        heapq.heappush(areas, -area)
        area_to_coords[area].add((x0, x, y0, y))


def fill(x, y):
    return new_greens, success


# loop thru popping from the max heap
# and do a recursive fill starting from indside the rectangle
# if you hit a 0 index without hitting a border it's invalid.
# in order for this to run efficiently the recursive fill alg will prioritize filling upper left, then left, then upper.
while len(areas) > 0:
    area = -heapq.heappop(areas)
    for x0, x, y0, y in area_to_coords[area]:
        mid_x = int(x0 + (x - x0) / 2)
        mid_y = int(y0 + (y - y0) / 2)
        point = (mid_x, mid_y)
        new_greens, success = fill(x, y)
        if not success:
            break
        greens.update(new_greens)
        for i in range(x0, x + 1):
            for j in range(x0, x + 1):
                if (i, j) not in greens:
                    success = False
                    break
            if not success:
                break
