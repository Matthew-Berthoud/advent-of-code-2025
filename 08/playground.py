import math

EXAMPLE = {"file": "example.txt", "connections": 10}
INPUT = {"file": "input.txt", "connections": 1000}
run = EXAMPLE
# run = INPUT


class Point:
    def __init__(self, id: int, coords: list[str]):
        assert len(coords) == 3, f"There are not three coordinates in {coords}"
        self.id = id
        self.X = int(coords[0])
        self.Y = int(coords[1])
        self.Z = int(coords[2])
        self.distances: dict[int, float] = {}
        self.closest: list = []

    def distance(self, other):
        distance = math.sqrt(
            (self.X - other.X) ** 2 + (self.Y - other.Y) ** 2 + (self.Z - other.Z) ** 2
        )
        self.distances[other.id] = distance
        i = 0
        for i, point in enumerate(self.closest):
            if self.distances[point.id] < distance:
                continue
            else:
                break
        self.closest.insert(i, other)

        return distance

    def __str__(self):
        return f"Point: {self.id}\n\t({self.X}, {self.Y}, {self.Z})\n\tdistances: {', '.join([f'{k}: {round(v, 2)}' for k, v in self.distances.items()])}\n\tclosest: {', '.join([str(point.id) for point in self.closest])}"

    def __eq__(self, other):
        return self.X == other.X and self.Y == other.Y and self.Z == other.Z


with open(run["file"]) as f:
    points: list[Point] = [
        Point(i, line.strip().split(",")) for i, line in enumerate(f.readlines())
    ]


# distances = [[0.0] * len(points) for _ in range(len(points))]

for i, a in enumerate(points):
    for j, b in enumerate(points):
        if a == b:
            continue
        # distances[i][j] =
        d = a.distance(b)

# for line in distances:
#     print([round(val, 2) for val in line])

for point in points:
    print(point)
