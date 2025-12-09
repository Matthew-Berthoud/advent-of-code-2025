import heapq
import math
from collections import defaultdict

EXAMPLE = {"file": "example.txt", "connections": 10}
INPUT = {"file": "input.txt", "connections": 1000}
# run = EXAMPLE
run = INPUT


def distance(a, b):
    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

    return distance


with open(run["file"]) as f:
    points: list[tuple[int, ...]] = [
        tuple([int(val) for val in line.strip().split(",")]) for line in f.readlines()
    ]

len_points = len(points)
# keys are distances, values are lists of tuples of points
distances = defaultdict(list)
dist_min_heap = []
heapq.heapify(dist_min_heap)

for i, a in enumerate(points):
    for j in range(i + 1, len_points):
        b = points[j]
        d = distance(a, b)
        distances[d].append((i, j))
        heapq.heappush(dist_min_heap, d)


circuits = defaultdict(set)
circuit_max_heap = []
heapq.heapify(circuit_max_heap)

last_connection = (0, 0)
while len(dist_min_heap) > 0:
    min_distance = heapq.heappop(dist_min_heap)
    i, j = distances[min_distance].pop()
    if circuits[i] == circuits[j] and len(circuits[i]) > 0:
        continue
    last_connection = (i, j)
    circuit = {i, j}
    circuit.update(circuits[i])
    circuit.update(circuits[j])
    for idx in circuit:
        circuits[idx] = circuit

i, j = last_connection
xi = points[i][0]
xj = points[j][0]

print(xi * xj)
