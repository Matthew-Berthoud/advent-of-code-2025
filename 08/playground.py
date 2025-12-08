import math

EXAMPLE = {"file": "example.txt", "connections": 10}
INPUT = {"file": "input.txt", "connections": 1000}
run = EXAMPLE
# run = INPUT


def distance(a, b):
    distance = math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2 + (a[2] - b[2]) ** 2)

    return distance


with open(run["file"]) as f:
    points: list[tuple[int, ...]] = [
        tuple([int(val) for val in line.strip().split(",")]) for line in f.readlines()
    ]

distances = [[0.0] * len(points) for _ in range(len(points))]

closest_pairs = []

for i, a in enumerate(points):
    for j, b in enumerate(points):
        if a == b:
            continue
        d = distance(a, b)
        distances[i][j] = d
        k = 0
        do_it = True
        for k, (i2, j2) in enumerate(closest_pairs):
            if distances[i2][j2] < d:
                continue
            if i2 == j and j2 == i:
                do_it = False
            break
        if do_it:
            closest_pairs.insert(k, (i, j))

circuits = [set([i]) for i in range(len(points))]
count = 1
circuit_idx = -1
for a, b in closest_pairs:
    already_connected = False
    new_circuit = set((a, b))
    overlapping_circuits = []
    for i, circuit in enumerate(circuits):
        if a in circuit and b in circuit:
            already_connected = True
            break
        if a in circuit:
            overlapping_circuits.append(i)
        elif b in circuit:
            overlapping_circuits.append(i)

    if already_connected:
        continue

    assert len(overlapping_circuits) == 2
    new_circuit = new_circuit.union(circuits.pop(max(overlapping_circuits)))
    new_circuit = new_circuit.union(circuits.pop(min(overlapping_circuits)))

    circuits.append(new_circuit)
    print(f"connecting {a}: {points[a]} and {b}: {points[b]}")
    count += 1
    if count == run["connections"]:
        break

lengths = [len(c) for c in circuits]
total = 1
for _ in range(3):
    biggest = max(lengths)
    lengths.remove(biggest)
    print(biggest)
    total *= biggest

print(circuits)
print(len(circuits))
print(total)
