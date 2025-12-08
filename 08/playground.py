EXAMPLE = {"file": "example.txt", "connections": 10}
INPUT = {"file": "input.txt", "connections": 1000}
run = EXAMPLE
# run = INPUT


class Point:
    def __init__(self, coords: list[str]):
        assert len(coords) == 3, f"There are not three coordinates in {coords}"
        self.X = int(coords[0])
        self.Y = int(coords[1])
        self.Z = int(coords[2])


with open(run["file"]) as f:
    points: list[Point] = [Point(line.strip().split(",")) for line in f.readlines()]
