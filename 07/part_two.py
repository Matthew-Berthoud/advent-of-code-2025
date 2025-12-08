from collections import defaultdict

SPLITTER = "^"

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

start_line = lines.pop(0)
start_idx = start_line.find("S")
beams = set([start_idx])

# index of beam : unique paths that it represents
incoming_beams = defaultdict(int)
incoming_beams[start_idx] = 1

for line in lines:
    to_split = set()
    for i in beams:
        if line[i] == SPLITTER:
            to_split.add(i)
    for i in to_split:
        incoming = incoming_beams[i]
        incoming_beams[i - 1] += incoming
        incoming_beams[i + 1] += incoming
        incoming_beams[i] = 0

        beams.add(i - 1)
        beams.add(i + 1)
        beams.remove(i)

total = sum(incoming_beams.values())
print(total)
