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

# new_greens = set()
#
#
# def flood_fill(x, y, new_greens=set()):
#     if (x, y) in greens:
#         return new_greens
#     if x < 0 or y < 0:
#         raise ValueError("Flood filling the wrong side")
#
#     new_greens.add((x, y))
#     new_greens.update(flood_fill(x - 1, y, new_greens))
#     new_greens.update(flood_fill(x, y - 1, new_greens))
#     new_greens.update(flood_fill(x + 1, y, new_greens))
#     new_greens.update(flood_fill(x, y + 1, new_greens))
#
#     return new_greens
#
#
# try:
#     greens.update(flood_fill(5000, 5000))
# except ValueError:
#     print("fuck")
# exit()

# loop thru popping from the max heap
# and do a recursive fill starting from indside the rectangle
# if you hit a 0 index without hitting a border it's invalid.
# in order for this to run efficiently the recursive fill alg will prioritize filling upper left, then left, then upper.
answer = 0
while answer == 0 and len(areas) > 0:
    area = -heapq.heappop(areas)
    for x0, x, y0, y in area_to_coords[area]:
        mid_x = int(x0 + (x - x0) / 2)
        mid_y = int(y0 + (y - y0) / 2)
        node = (mid_x, mid_y)

        q = []
        q.append(node)
        while len(q) > 0:
            n = q.pop(0)

        try:
            greens.update(flood_fill(mid_x, mid_y))
        except ValueError:
            break

        all_green = True
        for i in range(x0, x + 1):
            for j in range(y0, y + 1):
                if (i, j) not in greens:
                    all_green = False
                    break
            if not all_green:
                break
        if all_green:
            answer = area
            break
print(answer)
